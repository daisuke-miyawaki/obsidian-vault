"""NotebookLM UI selectors — update here when Google changes the UI."""

from __future__ import annotations

# Home / notebook list
CREATE_NOTEBOOK_SELECTORS = [
    "button.create-new-button",
    "button[aria-label='ノートブックを新規作成']",
    "button[aria-label='Create new notebook']",
    "button[aria-label='新しいノートブックを作成']",
    "mat-card[role='button']:has-text('Create new notebook')",
    "button:has-text('新規作成')",
    "button:has-text('Create new')",
]

CREATE_NOTEBOOK_TEXTS = [
    "ノートブックを新規作成",
    "新規作成",
    "Create new notebook",
    "新しいノートブック",
]

NOTEBOOK_LINK_SELECTORS = [
    "a[href*='/notebook/']",
    "mat-card[role='button']:has(h3)",
]

# Source panel (inside notebook detail page)
ADD_SOURCE_SELECTORS = [
    "button.add-source-button",
    "button[aria-label='ソースを追加']",
    "button[aria-label='Add source']",
    "button:has-text('ソースを追加')",
    "button:has-text('+ Add sources')",
    "button:has-text('Add sources')",
    "button:has-text('Upload sources')",
    '[data-testid="add-source"]',
]

ADD_SOURCE_DIALOG_SELECTORS = [
    "mat-dialog-container[role='dialog']",
    ".cdk-overlay-pane mat-dialog-container",
]

# 2026 UI: source type chips / tabs
YOUTUBE_SOURCE_SELECTORS = [
    "mat-chip:has-text('YouTube')",
    "mat-mdc-chip:has-text('YouTube')",
    "[role='button']:has-text('YouTube')",
    "button:has-text('YouTube')",
]

WEBSITE_SOURCE_SELECTORS = [
    "mat-chip:has-text('Websites')",
    "mat-mdc-chip:has-text('Websites')",
    "mat-chip:has-text('Website')",
    "mat-mdc-chip:has-text('Website')",
    "[role='button']:has-text('Websites')",
    "button:has-text('Websites')",
    "button:has-text('Website')",
]

URL_INPUT_SELECTORS = [
    "textarea[aria-label='URL を入力']",
    "textarea[placeholder='リンクを貼り付ける']",
    "textarea[aria-label='Enter URLs']",
    "textarea[aria-label*='Enter URL' i]",
    "textarea[aria-label*='URL' i]",
    "textarea[placeholder='Paste any links']",
    "textarea[placeholder*='Paste any link' i]",
]

WEBSITE_TAB_TEXTS = ["ウェブサイト", "Websites", "Website"]

INSERT_SOURCE_SELECTORS = [
    "button:has-text('挿入')",
    "button:has-text('Insert')",
]

# Chat
CHAT_INPUT_SELECTORS = [
    "textarea[placeholder*='入力' i]",
    "textarea[placeholder*='Start typing' i]",
    "textarea[placeholder*='NotebookLM' i]",
    "textarea[placeholder*='Ask' i]",
    "textarea.query-box-textarea",
    "textarea",
    "[contenteditable='true']",
]

SEND_BUTTON_SELECTORS = [
    "button.submit-button[aria-label='送信']",
    "button[aria-label='Send']",
    "button[aria-label='送信']",
    "button.submit-button",
    "button:has-text('Send')",
]

RESPONSE_CONTAINER_SELECTORS = [
    ".to-user-container .message-content",
    ".to-user-container",
    ".to-user-message-inner-content",
    ".chat-message-pair .to-user-container",
    "[data-message-author='model']",
    "[data-test-id='conversation-turn']",
    ".model-response",
]

CHAT_PAIR_SELECTOR = ".chat-message-pair"
GENERATING_STOP_SELECTORS = [
    "button[aria-label*='停止']",
    "button[aria-label*='Stop']",
]

SOURCE_ROW_SELECTORS = [
    ".single-source-container",
    "[class*='single-source']",
]

SELECT_ALL_CHECKBOX_TEXTS = [
    "すべて選択",
    "Select all",
]

NEW_CHAT_SELECTORS = [
    "button[aria-label='新しいチャット']",
    "button[aria-label='New chat']",
    "button[aria-label='チャットを新規作成']",
    "button[aria-label='Create new chat']",
]

CHAT_OPTIONS_SELECTORS = [
    "button[aria-label='チャット オプション']",
    "button[aria-label='チャットのオプション']",
    "button[aria-label='Chat options']",
]

CHAT_MENU_NEW_TEXTS = [
    "新しいチャット",
    "New chat",
]

CHAT_MENU_CLEAR_TEXTS = [
    "チャットの履歴を削除",
    "チャット履歴を削除",
    "Delete chat history",
    "チャットをクリア",
    "Clear chat",
]

NEW_CHAT_TEXTS = [
    "新しいチャット",
    "New chat",
    "チャットをクリア",
    "Clear chat",
]
