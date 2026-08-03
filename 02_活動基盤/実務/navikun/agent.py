"""LangGraph エージェント — 最初は薄く「判定 → 返信生成」の2ノード。"""

from __future__ import annotations

from typing import TypedDict

import google.generativeai as genai
from langgraph.graph import END, StateGraph

from config import settings
from prompts import SYSTEM_PROMPT


class AgentState(TypedDict, total=False):
    channel_id: str
    user_id: str
    user_message: str
    command: str | None
    command_arg: str
    recent_messages: list[str]
    memories: list[str]
    response: str


def decide(state: AgentState) -> AgentState:
    """何をすべきか決める（今は素通し。後から分岐を足せる）。"""
    return state


def generate_reply(state: AgentState) -> AgentState:
    """Gemini を直接呼んで返信を生成する。"""
    if not settings.gemini_api_key:
        state["response"] = "すみません、今うまく返答できません。少し待ってからもう一度お願いします。"
        return state

    memories_text = ""
    if state.get("memories"):
        memories_text = (
            "\n\n## 案件・お客さんの資料（背景メモ。今の話し相手その人ではない）\n"
            + "\n".join(f"- {m}" for m in state["memories"])
            + "\n\n※ 上記はらいふギャラリー案件のメモです。"
            "話し相手が宮脇さんなら「宮脇さん」、山本さん本人なら「山本さん」と呼んでください。"
            "韓国への買い出しなど補足事項は、今の話題に必要なとき以外は出さないでください。"
        )

    user_content = state.get("user_message", "")
    if state.get("command"):
        user_content = (
            f"[指示: {state['command']}] {state.get('command_arg', '')}\n\n"
            f"元のメッセージ: {user_content}"
        )

    prompt = (
        f"{SYSTEM_PROMPT}{memories_text}\n\n"
        f"## 今のメッセージ（話し相手。宮脇さんの可能性が高い）\n{user_content}"
    )

    genai.configure(api_key=settings.gemini_api_key)
    model = genai.GenerativeModel(settings.gemini_model)
    response = model.generate_content(
        prompt,
        generation_config=genai.types.GenerationConfig(
            max_output_tokens=512,
            temperature=0.7,
        ),
    )

    try:
        text = (response.text or "").strip()
    except Exception:
        text = ""

    state["response"] = text or "すみません、うまく言葉が出ませんでした。もう一度お願いできますか？"
    return state


# --- グラフ構築 ---
graph_builder = StateGraph(AgentState)
graph_builder.add_node("decide", decide)
graph_builder.add_node("generate_reply", generate_reply)

graph_builder.set_entry_point("decide")
graph_builder.add_edge("decide", "generate_reply")
graph_builder.add_edge("generate_reply", END)

graph = graph_builder.compile()


def run_agent(
    channel_id: str,
    user_id: str,
    user_message: str,
    command: str | None = None,
    command_arg: str = "",
    recent_messages: list[str] | None = None,
    memories: list[str] | None = None,
) -> str:
    """エージェントを実行して返信テキストを返す。"""
    result = graph.invoke({
        "channel_id": channel_id,
        "user_id": user_id,
        "user_message": user_message,
        "command": command,
        "command_arg": command_arg,
        "recent_messages": recent_messages or [],
        "memories": memories or [],
        "response": "",
    })
    return result.get("response", "")
