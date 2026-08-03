"""NotebookLM 自動化で使う例外"""


class RateLimitError(RuntimeError):
    """NotebookLM の1日チャット上限に達した"""
