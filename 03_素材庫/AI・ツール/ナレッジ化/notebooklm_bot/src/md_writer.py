from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from .config_loader import AppConfig


@dataclass
class VideoEntry:
    no: str
    title: str
    url: str


def parse_urls_file(path: Path) -> list[VideoEntry]:
    entries: list[VideoEntry] = []
    for i, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = line.strip()
        if not line or "|" not in line:
            continue
        title, url = line.split("|", 1)
        entries.append(VideoEntry(no=f"{i:03d}", title=title.strip(), url=url.strip()))
    return entries


def sanitize_filename(title: str, max_len: int = 30) -> str:
    safe = title.replace("/", "／").replace("\\", "＼").strip()
    if len(safe) > max_len:
        safe = safe[:max_len]
    return safe


def build_md_filename(video: VideoEntry) -> str:
    return f"{video.no}_{sanitize_filename(video.title)}.md"


# NotebookLM UI が混入しやすい記号・行
_UI_NOISE_LINE = re.compile(
    r"^(more_horiz|keyboard_arrow_down|keyboard_arrow_up|search|arrow_forward|"
    r"chevron_right|chevron_left|dock_to_right|dock_to_left|tune|share|settings|"
    r"photo_spark|landscape_2|play_arrow|video_youtube|link|language|search_spark)$"
)
_STANDALONE_CITATION_NUM = re.compile(r"^\d{1,3}$")
_PUNCT_ONLY_LINE = re.compile(r"^[。、・…\s]+$")
_PREAMBLE_LINE = re.compile(
    r"^ソース「.+」に基づき、ご指定の形式でMarkdownを出力"
)
# ゆっくり解説などの字幕由来：日本語の単語間に不自然なスペースが入る
_CJK_CHAR = r"[ぁ-んァ-ヶー一-龠々〆ヵヶ]"
_CJK_SPACED = re.compile(rf"({_CJK_CHAR})\s+({_CJK_CHAR})")
_SUMMARY_ONE_LINE = re.compile(
    r"テーマ：(.*?)\s+結論：(.*?)\s+自分への使いどころ：(.*?)\s*$"
)
_SECTION_PLAIN = re.compile(r"^(\d{1,2})\.\s+(.+)$")
_STEP_LINE = re.compile(r"^\d+\.\s+[^:\n]{1,40}:\s*.+")
_H4_LABELS = frozenset({"ポイント", "注意点", "手順", "例"})
_SUB_LABEL_LINE = re.compile(r"^#{1,6}\s*(手順|ポイント|注意点|例)")


def fix_spaced_japanese(text: str) -> str:
    """日本語文字の間に入った不自然なスペースを除去する（字幕・文字起こし由来）。"""
    # 単語間の通常スペース（1〜2箇所）と区別：4箇所以上なら字幕由来とみなす
    if len(_CJK_SPACED.findall(text)) < 4:
        return text
    prev = None
    cur = text
    while prev != cur:
        prev = cur
        cur = _CJK_SPACED.sub(r"\1\2", cur)
    return cur


def _is_main_section_header(line: str) -> bool:
    m = _SECTION_PLAIN.match(line.strip())
    if not m:
        return False
    title = m.group(2).strip()
    if _STEP_LINE.match(line.strip()):
        return False
    if line.strip().startswith("#"):
        return False
    return len(title) >= 12 or "：" in title or len(title) >= 30


def _normalize_sub_label(line: str) -> str | None:
    stripped = line.strip()
    if stripped in _H4_LABELS:
        return f"**{stripped}**"
    m = _SUB_LABEL_LINE.match(stripped)
    if m:
        return f"**{m.group(1)}**"
    if stripped.startswith("**") and stripped.endswith("**"):
        inner = stripped[2:-2].split("（", 1)[0].strip()
        if inner in _H4_LABELS:
            return f"**{inner}**"
    return None


def _tighten_sub_labels(text: str) -> str:
    """小項目ラベルの直前の空行を除去する。"""
    lines = text.splitlines()
    out: list[str] = []
    for line in lines:
        norm = _normalize_sub_label(line)
        if norm is not None:
            while out and out[-1].strip() == "":
                out.pop()
            out.append(norm)
            continue
        out.append(line)
    return "\n".join(out)


def format_structured_ai_note(text: str) -> str:
    """AI向けノート：H3/H4見出しと章間の空行を補正する。"""
    m = _SUMMARY_ONE_LINE.search(text)
    if m:
        text = (
            f"テーマ：{m.group(1).strip()}\n"
            f"結論：{m.group(2).strip()}\n"
            f"自分への使いどころ：{m.group(3).strip()}\n\n"
            + text[m.end() :].lstrip()
        )

    out: list[str] = []
    in_mokuji = False

    def emit_blank() -> None:
        if out and out[-1].strip() != "":
            out.append("")

    def emit_heading(level: int, title: str) -> None:
        emit_blank()
        out.append(f"{'#' * level} {title}")

    for raw in text.splitlines():
        line = raw.rstrip()
        stripped = line.strip()
        if not stripped:
            if out and out[-1].strip() != "":
                out.append("")
            in_mokuji = False
            continue

        sub_label = _normalize_sub_label(stripped)
        if sub_label is not None:
            in_mokuji = False
            while out and out[-1].strip() == "":
                out.pop()
            out.append(sub_label)
            continue

        if stripped.startswith("#"):
            if stripped.startswith("### 目次"):
                in_mokuji = True
            else:
                in_mokuji = False
            emit_blank()
            out.append(stripped)
            continue

        if stripped == "構造化詳細ノート":
            emit_heading(2, "構造化詳細ノート")
            continue
        if stripped == "目次":
            in_mokuji = True
            emit_heading(3, "目次")
            continue
        if stripped.startswith("用語・固有名詞一覧"):
            in_mokuji = False
            emit_heading(3, stripped)
            continue
        if stripped.startswith("触れられたトピック一覧"):
            in_mokuji = False
            emit_heading(3, stripped)
            continue

        if _is_main_section_header(stripped):
            in_mokuji = False
            m_sec = _SECTION_PLAIN.match(stripped)
            assert m_sec
            emit_heading(3, f"{m_sec.group(1)}. {m_sec.group(2).strip()}")
            continue

        if in_mokuji and not stripped.startswith("-") and not stripped.startswith("|"):
            out.append(f"- {stripped}")
            continue

        if stripped in {"：", ":"}:
            continue

        if stripped.startswith("- ") or stripped.startswith("|") or stripped.startswith(">"):
            out.append(stripped)
            continue

        if _STEP_LINE.match(stripped):
            out.append(stripped)
            continue

        out.append(stripped)

    result: list[str] = []
    blank_run = 0
    for line in out:
        if line.strip() == "":
            blank_run += 1
            if blank_run <= 2:
                result.append("")
        else:
            blank_run = 0
            result.append(line)
    return _tighten_sub_labels("\n".join(result).strip() + "\n")


def clean_notebooklm_output(text: str, *, structured_ai: bool = False) -> str:
    """NotebookLM UIノイズを除去し、読みやすいMarkdownに整える。"""
    lines: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            lines.append("")
            continue
        if _UI_NOISE_LINE.match(stripped):
            continue
        if _STANDALONE_CITATION_NUM.match(stripped):
            continue
        if _PUNCT_ONLY_LINE.match(stripped):
            continue
        if _PREAMBLE_LINE.match(stripped):
            continue
        lines.append(fix_spaced_japanese(line))

    # 空行が3行以上続くのを2行までに圧縮
    result: list[str] = []
    blank_run = 0
    for line in lines:
        if line.strip() == "":
            blank_run += 1
            if blank_run <= 2:
                result.append("")
        else:
            blank_run = 0
            result.append(line.rstrip())
    body = "\n".join(result).strip() + "\n"
    if structured_ai:
        body = format_structured_ai_note(body)
    return body


def build_md_content(
    video: VideoEntry,
    channel_slug: str,
    notebooklm_body: str,
    *,
    taxonomy: str | None = None,
    structured_ai: bool = False,
) -> str:
    body = clean_notebooklm_output(notebooklm_body, structured_ai=structured_ai)
    tax_line = f"- 系統: {taxonomy}\n" if taxonomy else ""
    if body.startswith("#"):
        header = (
            f"## 基本情報\n"
            f"{tax_line}"
            f"- チャンネル: {channel_slug}\n"
            f"- URL: {video.url}\n"
            f"- 取得日: {date.today().isoformat()}\n\n"
        )
        lines = body.splitlines()
        if lines and lines[0].startswith("#"):
            return f"{lines[0]}\n\n{header}" + "\n".join(lines[1:]).lstrip()
    return (
        f"# {video.title}\n\n"
        f"## 基本情報\n"
        f"{tax_line}"
        f"- チャンネル: {channel_slug}\n"
        f"- URL: {video.url}\n"
        f"- 取得日: {date.today().isoformat()}\n\n"
        f"{body}\n"
    )


def save_video_md(config: AppConfig, video: VideoEntry, notebooklm_body: str) -> Path:
    config.output_dir.mkdir(parents=True, exist_ok=True)
    filename = build_md_filename(video)
    path = config.output_dir / filename
    taxonomy = getattr(config, "taxonomy", None)
    structured_ai = "video_note_ai" in config.prompt_file.name
    content = build_md_content(
        video,
        config.channel_slug,
        notebooklm_body,
        taxonomy=config.taxonomy,
        structured_ai=structured_ai,
    )
    path.write_text(content, encoding="utf-8")
    return path


def _youtube_video_id(url: str) -> str:
    if "v=" in url:
        return url.split("v=")[-1].split("&")[0]
    return url


def _update_index_line(line: str, video_no: str, video_id: str, md_name: str) -> str:
    """
    進捗表の1行を更新する。
    | No | タイトル | [YouTube](url) | md | 状態 |
    md列は — / 空 / 既存リンクのいずれでも上書きする。
    """
    stripped = line.strip()
    if not stripped.startswith(f"| {video_no} |"):
        return line
    if video_id not in stripped:
        return line

    row_re = re.compile(
        rf"^(\| {re.escape(video_no)} \| .+? \| \[YouTube\]\([^)]+\) \| )"
        rf"([^|]*?)( \| )([^|]*?)( \|)\s*$"
    )
    match = row_re.match(stripped)
    if not match:
        return line

    prefix, _md_col, sep, _status, suffix = match.groups()
    return f"{prefix}[{md_name}]({md_name}){sep}完了{suffix}"


def update_index(config: AppConfig, video: VideoEntry, md_path: Path) -> None:
    if not config.index_file.exists():
        return
    text = config.index_file.read_text(encoding="utf-8")
    md_name = md_path.name
    video_id = _youtube_video_id(video.url)

    new_lines = [
        _update_index_line(line, video.no, video_id, md_name)
        for line in text.splitlines()
    ]
    config.index_file.write_text("\n".join(new_lines) + "\n", encoding="utf-8")
