"""らいふフォルダの md を Mem0（customer_raifu）へ投入する一時スクリプト。"""

from __future__ import annotations

import os
import re
import sys
import time
from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent
load_dotenv(ROOT / ".env")

sys.path.insert(0, str(ROOT))
from memory import add_memory, get_all_memories, search_memory  # noqa: E402

USER_ID = "customer_raifu"
# このファイル: 02_活動基盤/実務/navikun/ → Vault直下は parents[3]
# 旧パス …/AI関連/らいふ は廃止。いまの置き場に相対で合わせる。
_VAULT_ROOT = Path(__file__).resolve().parents[3]
SOURCE_DIR = Path(
    os.environ.get(
        "RAIFU_SOURCE_DIR",
        str(_VAULT_ROOT / "02_活動基盤" / "実務" / "お客さん情報" / "らいふギャラリー"),
    )
)
MAX_CHUNK = 1800


def _clean(text: str) -> str:
    text = text.replace("\r\n", "\n")
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def _chunk_markdown(name: str, body: str) -> list[tuple[str, str]]:
    """見出し単位で分割。長すぎる場合はさらに切る。"""
    body = _clean(body)
    parts = re.split(r"(?=^##\s)", body, flags=re.M)
    chunks: list[tuple[str, str]] = []
    for i, part in enumerate(parts):
        part = part.strip()
        if not part:
            continue
        heading = ""
        m = re.match(r"^##\s+(.+)$", part, flags=re.M)
        if m:
            heading = m.group(1).strip()
        label = f"{name}" + (f" / {heading}" if heading else "")
        if len(part) <= MAX_CHUNK:
            chunks.append((label, part))
            continue
        # さらに段落で切る
        paras = part.split("\n\n")
        buf = ""
        n = 0
        for p in paras:
            if len(buf) + len(p) + 2 > MAX_CHUNK and buf:
                n += 1
                chunks.append((f"{label} ({n})", buf.strip()))
                buf = p
            else:
                buf = f"{buf}\n\n{p}" if buf else p
        if buf.strip():
            n += 1
            chunks.append((f"{label} ({n})", buf.strip()))
    return chunks


# 会話ですぐ使える要点（店舗概要ベース）
SEED_FACTS = [
    "顧客はリサイクルショップ「らいふギャラリー（ライフギャラリー）」。オーナーは山本君（元プロボクサー）。宮脇とは友人で、2012年頃からサイト・集客の相談を継続している。",
    "らいふギャラリーの特徴：買取・販売はリアル店舗が中心。「アットホーム」「安心感」を大事にする。女性スタッフが買取対応するなどお客さんの不安を減らす工夫がある。ゴミを商品に変える社会貢献という志がある。",
    "オーナー山本君の性格：運が良く、おもしろく、真面目でおっとり。幸せそうなゆるい雰囲気。自分を信じている。新しいことへの取り組みは苦手気味で、周りが動き出してから動き出す傾向がある。ITが苦手で、いまだに多くの業務を手書きで処理している。",
    "オーナー山本君の補足：1976年生まれ、春日井市在住。趣味・副業で株式投資（テクニカル分析を取り入れてから成績向上）。たまに韓国へ商品買い出しをする。",
    "現在の案件（2026年）：らいふギャラリー向けのAI導入コンサルが進行中。2026年7月3日の打ち合わせではSEO・課題改善・方向性に手応えがあった。",
    "プロジェクト方針：名古屋市内でベビー用品販売（おちゃのこネット）でSEO上位の実績がある。買取特化サイトを新規構築し、販売サイトとの相乗効果を狙う。ターゲットは愛知県全域のローカルSEO。",
    "買取サイトの技術方針：WordPress＋Welcart。買取実績を1商品1ページで登録。買取価格は掲載しない。おちゃのこCSVのミラーサイト判定を避けるため、AI段階生成・店舗独自データ・人工的ゆらぎ・予約投稿（1日5〜10件）を使う。",
    "一次情報SEO：スタッフ日報や勉強メモを3行入力→AIで1500字コラム化。地域名・査定エピソード・清掃メンテナンス・テレビ出演実績などでE-E-A-Tを高める。",
    "ナビくんへの対応方針：山本君はITが苦手なので専門用語を避け、焦らせず、短い言葉で親しみやすく進行する。新しい施策は一気に押し切らず、周りが動き出すペースに合わせて提案する。",
]


def main() -> None:
    if not SOURCE_DIR.is_dir():
        raise SystemExit(f"フォルダがありません: {SOURCE_DIR}")

    uploaded = 0
    failed = 0

    print("=== seed facts ===")
    for i, fact in enumerate(SEED_FACTS, 1):
        try:
            add_memory(
                USER_ID,
                fact,
                metadata={"source": "seed", "customer": "raifu", "index": i},
            )
            uploaded += 1
            print(f"OK seed {i}/{len(SEED_FACTS)}")
        except Exception as exc:  # noqa: BLE001
            failed += 1
            print(f"FAIL seed {i}: {exc}")
        time.sleep(0.4)

    files = sorted(SOURCE_DIR.glob("*.md"))
    print(f"=== files: {len(files)} ===")
    for path in files:
        text = path.read_text(encoding="utf-8")
        chunks = _chunk_markdown(path.name, text)
        print(f"-- {path.name}: {len(chunks)} chunks --")
        for j, (label, chunk) in enumerate(chunks, 1):
            payload = f"【らいふギャラリー資料：{label}】\n{chunk}"
            try:
                add_memory(
                    USER_ID,
                    payload,
                    metadata={
                        "source": path.name,
                        "customer": "raifu",
                        "chunk": j,
                        "label": label[:120],
                    },
                )
                uploaded += 1
                print(f"OK {path.name} {j}/{len(chunks)}")
            except Exception as exc:  # noqa: BLE001
                failed += 1
                print(f"FAIL {path.name} {j}: {exc}")
            time.sleep(0.5)

    print("=== verify search ===")
    try:
        results = search_memory(USER_ID, "山本君 らいふギャラリー 性格", limit=3)
        print(f"search hits: {len(results)}")
        for r in results[:3]:
            mem = r.get("memory") or r.get("data") or str(r)
            print("-", str(mem)[:120].replace("\n", " "))
    except Exception as exc:  # noqa: BLE001
        print("search verify failed:", exc)

    try:
        all_mem = get_all_memories(USER_ID)
        print(f"total memories for {USER_ID}: {len(all_mem)}")
    except Exception as exc:  # noqa: BLE001
        print("get_all failed:", exc)

    print(f"DONE uploaded={uploaded} failed={failed}")


if __name__ == "__main__":
    main()
