# ATLAS 🚀

> **AI Tutoring & Learning Assistance System** — 一款专为学生打造的智能 AI 辅助教学与学习管理系统。

<p align="left">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/AI-Tutor-green?style=flat-square" alt="AI">
  <img src="https://img.shields.io/badge/Database-SQLite-lightgrey?style=flat-square&logo=sqlite" alt="SQLite">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=flat-square" alt="License">
</p>

---

## 📌 项目简介 (Introduction)

**ATLAS** 是一款基于人工智能的学习助手系统。它旨在通过引入前沿的 AI 技术，为学生提供全天候的智能问答、学习辅助以及个性化的学习进度管理，打造沉浸式的智能学习体验。

## ✨ 核心特性 (Features)

* 🔐 **用户登录系统** — 完整的用户认证机制，保障个人学习数据的隐私与安全。
* 🤖 **AI 智能对话** — 集成先进的大语言模型，提供即时、精准的学术问题解答。
* 💾 **本地数据存储** — 基于 SQLite 数据库，高效管理用户信息与核心数据。
* 📊 **学习记录管理** — 自动追踪、留存用户的学习轨迹，生成个性化档案。
* 💻 **优雅图形界面** — 采用 Tkinter 打造直观、易用的 GUI 交互界面。


## 🛠️ 技术栈 (Technology Stack)

* **开发语言**：Python 3.10+
* **界面开发**：Tkinter (Python 标准 GUI 库)
* **数据存储**：SQLite 3
* **核心技术**：DeepSeek API (大语言模型集成)

## 📂 项目结构 (Project Structure)

```text
ATLAS/
├── .venv/               # Python 虚拟环境
├── src/                 # 项目核心源代码
│   ├── database/        # 数据库模型与管理
│   ├── gui/             # Tkinter 界面组件
│   └── utils/           # 工具函数与 AI 接口
├── main.py              # 项目启动主入口
└── README.md            # 项目说明文档