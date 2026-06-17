# ATLAS 🚀

> **AI Tutoring & Learning Assistance System**
> 학생을 위한 AI 기반 학습 보조 및 학습 관리 시스템


<p align="left">
  <img src="https://img.shields.io/badge/Python-3.11-blue?style=flat-square&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/AI-Tutor-green?style=flat-square" alt="AI">
  <img src="https://img.shields.io/badge/Database-SQLite-lightgrey?style=flat-square&logo=sqlite" alt="SQLite">
  <img src="https://img.shields.io/badge/API-DeepSeek-orange?style=flat-square" alt="DeepSeek">
</p>


---

# 📌 프로젝트 소개 (Introduction)

**ATLAS**는 인공지능 기술을 활용한 학습 지원 시스템입니다.

학생들이 AI와 대화하며 학습할 수 있도록 설계되었으며,
질문 응답, 학습 기록 저장, AI 퀴즈 생성, 학습 데이터 관리 기능을 제공합니다.

본 시스템은 Python 기반으로 개발되었으며,
DeepSeek API를 활용하여 AI 학습 도우미 기능을 구현하였습니다.


---

# ✨ 주요 기능 (Features)


## 🔐 사용자 관리 시스템

- 사용자 회원가입
- 사용자 로그인
- 개인 학습 데이터 관리


## 🤖 AI Tutor

사용자가 학습 관련 질문을 입력하면
AI가 자동으로 답변을 제공합니다.

기능:

- 실시간 AI 질문 응답
- 학습 내용 설명
- 문제 해결 도움


## 💾 학습 기록 저장

SQLite 데이터베이스를 사용하여
사용자의 학습 내용을 저장합니다.

저장 정보:

- 사용자
- 질문 내용
- AI 답변
- 시간 기록


## 📝 AI Quiz 생성

사용자가 원하는 학습 주제를 입력하면
AI가 자동으로 퀴즈를 생성합니다.

포함 내용:

- 문제
- 선택지
- 정답
- 해설


## 📊 Dashboard

사용자의 학습 활동을 통계로 표시합니다.

제공 정보:

- AI 대화 횟수
- Quiz 생성 횟수


---

# 🛠️ 기술 스택 (Technology Stack)


## 개발 언어

Python 3.11


## GUI 개발

CustomTkinter

현대적인 Python GUI 인터페이스 구현


## 데이터베이스

SQLite3

사용자 정보 및 학습 기록 저장


## AI 모델

DeepSeek API

AI 대화 및 콘텐츠 생성 기능 제공


---

# 📂 프로젝트 구조 (Project Structure)


ATLAS/
│
├── main.py
│
├── atlas.db
│
├── ai
│ └── openai_client.py
│
├── database
│ ├── db.py
│ └── init.py
│
├── gui
│ ├── login_page.py
│ ├── register_page.py
│ ├── tutor_page.py
│ ├── history_page.py
│ ├── quiz_page.py
│ └── dashboard_page.py
│
├── config
│ └── user_session.py
│
└── README.md