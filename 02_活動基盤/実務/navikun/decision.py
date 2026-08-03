"""介入する／しないの判定ロジック。"""

from __future__ import annotations

import re

from state_store import get_intervention, is_thinking

# 考えるモードを起動するキーワード
THINKING_TRIGGERS = [
    r"考え中",
    r"週末に見ます",
    r"忙しい",
    r"また後で",
    r"ちょっと待って",
]
_thinking_re = re.compile("|".join(THINKING_TRIGGERS))

# 停滞とみなす短文パターン
STAGNATION_PATTERNS = [
    r"^了解(です|しました)?[。！!]?$",
    r"^(わ|分)かりました[。！!]?$",
    r"^ありがとう(ございます)?[。！!]?$",
    r"^検討します[。！!]?$",
    r"^承知(しました|です)[。！!]?$",
    r"^OK[。！!]?$",
    r"^はい[。！!]?$",
]
_stagnation_re = re.compile("|".join(STAGNATION_PATTERNS), re.IGNORECASE)

# 直接コマンド
DIRECT_COMMANDS = {
    "リサーチして": "research",
    "アイデア出して": "idea",
    "まとめて": "summarize",
    "どう思う": "opinion",
    "介入レベル": "set_level",
}


def looks_like_thinking(text: str) -> bool:
    return bool(_thinking_re.search(text))


def is_stagnant(messages: list[str], threshold: int = 3) -> bool:
    """直近メッセージが threshold 件以上連続で短文パターンなら停滞。"""
    if len(messages) < threshold:
        return False
    recent = messages[-threshold:]
    return all(_stagnation_re.match(m.strip()) for m in recent)


def parse_direct_command(text: str) -> tuple[str | None, str]:
    """メンション後のテキストから直接コマンドを判定。
    戻り値: (コマンド種別 or None, 残りのテキスト)
    """
    cleaned = text.strip()
    for trigger, cmd in DIRECT_COMMANDS.items():
        if trigger in cleaned:
            rest = cleaned.split(trigger, 1)[1].strip()
            return cmd, rest
    return None, cleaned


def should_intervene(
    channel_id: str,
    user_id: str,
    is_mention: bool,
) -> bool:
    """メッセージ受信時に介入すべきかを返す。
    沈黙検知は時計係が担当するので、ここでは停滞のみ判定する。
    """
    if is_thinking(channel_id, user_id) and not is_mention:
        return False

    level = get_intervention(channel_id)
    if level == "quiet" and not is_mention:
        return False

    return True
