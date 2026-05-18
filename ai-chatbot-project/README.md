# 🤖 小智 — AI 智能聊天机器人

基于 **Claude API + Gradio** 构建的对话式 AI 助手，界面美观、代码简洁，非常适合 AI 入门项目。

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)

## ✨ 功能亮点

- 💬 多轮对话，支持上下文记忆
- 🎨 Gradio 提供美观的聊天界面
- 🔧 可自定义机器人名字和性格
- 📝 内置示例问题，一键体验

## 📸 项目截图

启动后在浏览器打开 `http://localhost:7860` 即可看到聊天界面。

## 🚀 快速开始

### 1. 克隆项目

```bash
git clone https://github.com/你的用户名/ai-chatbot-project.git
cd ai-chatbot-project
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 设置 API 密钥

去 [Anthropic Console](https://console.anthropic.com/) 注册并获取 API Key，然后设置环境变量：

```bash
# Linux / Mac
export ANTHROPIC_API_KEY='你的密钥'

# Windows CMD
set ANTHROPIC_API_KEY=你的密钥

# Windows PowerShell
$env:ANTHROPIC_API_KEY="你的密钥"
```

### 4. 启动运行

```bash
python app.py
```

打开浏览器访问 **http://localhost:7860** 即可开始聊天！

## 🔧 自定义你的机器人

打开 `app.py`，修改顶部的配置区域：

```python
# 机器人的名字
BOT_NAME = "小智"

# 机器人的性格设定
SYSTEM_PROMPT = """你是一个名叫小智的 AI 助手..."""
```

你可以把它改成任何你想要的角色，比如英语老师、代码助手、故事讲述者等。

## 📁 项目结构

```
ai-chatbot-project/
├── app.py              # 主程序（聊天逻辑 + 界面）
├── requirements.txt    # Python 依赖
├── .gitignore          # Git 忽略规则
└── README.md           # 项目说明（就是这个文件）
```

## 📄 License

MIT License — 随意使用和修改。
