"""
🤖 AI 智能聊天机器人
使用 Anthropic Claude API + Gradio 构建的对话式 AI 助手
"""

import os
import gradio as gr
from anthropic import Anthropic

# ============================================================
# 🔧 配置区域 —— 你可以在这里自定义你的机器人
# ============================================================

# 机器人的名字
BOT_NAME = "小智"

# 机器人的性格设定（系统提示词）
SYSTEM_PROMPT = f"""你是一个名叫{BOT_NAME}的 AI 助手。
你的特点是：
- 友好、热情、乐于助人
- 回答简洁清晰，善于用简单的语言解释复杂概念
- 适当使用 emoji 让对话更生动
- 如果不确定答案，会诚实地说不知道
"""

# 使用的模型
MODEL = "claude-sonnet-4-20250514"


# ============================================================
# 🧠 核心逻辑
# ============================================================

def create_client():
    """创建 Anthropic API 客户端"""
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError(
            "❌ 请设置环境变量 ANTHROPIC_API_KEY\n"
            "   Linux/Mac:  export ANTHROPIC_API_KEY='你的密钥'\n"
            "   Windows:    set ANTHROPIC_API_KEY=你的密钥"
        )
    return Anthropic(api_key=api_key)


def chat(user_message, history):
    """
    处理用户消息并返回 AI 回复

    参数:
        user_message: 用户输入的消息
        history: 历史对话记录 [{"role": "user/assistant", "content": "..."}]

    返回:
        AI 的回复文本
    """
    client = create_client()

    # 把历史记录转换为 API 需要的格式
    messages = []
    for msg in history:
        messages.append({"role": msg["role"], "content": msg["content"]})

    # 加入当前用户消息
    messages.append({"role": "user", "content": user_message})

    # 调用 Claude API
    response = client.messages.create(
        model=MODEL,
        max_tokens=1024,
        system=SYSTEM_PROMPT,
        messages=messages,
    )

    # 提取回复文本
    reply = response.content[0].text
    return reply


# ============================================================
# 🎨 Gradio 界面
# ============================================================

def build_app():
    """构建 Gradio 聊天界面"""

    with gr.Blocks(
        title=f"{BOT_NAME} - AI 聊天机器人",
        theme=gr.themes.Soft(),
    ) as app:

        gr.Markdown(
            f"""
            # 🤖 {BOT_NAME} — AI 智能聊天机器人
            > 基于 Claude API 构建，随时为你解答问题！
            """
        )

        chatbot = gr.ChatInterface(
            fn=chat,
            type="messages",
            examples=[
                "你好！介绍一下你自己",
                "用简单的语言解释什么是人工智能",
                "帮我写一首关于春天的短诗",
                "Python 有哪些适合初学者的学习资源？",
            ],
            retry_btn="🔄 重新生成",
            undo_btn="↩️ 撤回",
            clear_btn="🗑️ 清空对话",
        )

        gr.Markdown(
            """
            ---
            💡 **提示**: 你可以点击上方的示例问题快速开始对话
            """
        )

    return app


# ============================================================
# 🚀 启动
# ============================================================

if __name__ == "__main__":
    app = build_app()
    app.launch(
        server_name="0.0.0.0",  # 允许外部访问
        server_port=7860,
        share=False,  # 设为 True 可生成公网链接
    )
