import customtkinter as ctk

from ai.openai_client import ask_gpt
from config.user_session import get_user
from database.db import save_chat


class TutorPage(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.title("ATLAS AI Tutor")
        self.geometry("900x650")

        ctk.set_appearance_mode("dark")


        username = get_user()


        self.title_label = ctk.CTkLabel(
            self,
            text=f"Welcome, {username}",
            font=("Arial", 28)
        )

        self.title_label.pack(pady=20)



        self.question_box = ctk.CTkTextbox(
            self,
            width=700,
            height=150
        )

        self.question_box.pack(pady=10)



        self.ask_button = ctk.CTkButton(
            self,
            text="Ask AI",
            command=self.ask_ai
        )

        self.ask_button.pack(pady=10)



        self.history_button = ctk.CTkButton(
            self,
            text="History",
            command=self.open_history
        )

        self.history_button.pack(pady=10)



        self.quiz_button = ctk.CTkButton(
            self,
            text="Quiz",
            command=self.open_quiz
        )

        self.quiz_button.pack(pady=10)

        self.dashboard_button = ctk.CTkButton(
            self,
            text="Dashboard",
            command=self.open_dashboard
        )

        self.dashboard_button.pack(pady=10)



        self.answer_box = ctk.CTkTextbox(
            self,
            width=700,
            height=250
        )

        self.answer_box.pack(pady=10)



    def ask_ai(self):

        question = self.question_box.get(
            "1.0",
            "end"
        )


        self.answer_box.delete(
            "1.0",
            "end"
        )


        self.answer_box.insert(
            "end",
            "Thinking..."
        )


        try:

            answer = ask_gpt(question)


        except Exception as e:

            answer = "AI Error: " + str(e)



        # 保存聊天记录
        save_chat(
            get_user(),
            question,
            answer
        )


        self.answer_box.delete(
            "1.0",
            "end"
        )


        self.answer_box.insert(
            "end",
            answer
        )



    def open_history(self):

        self.withdraw()


        from gui.history_page import HistoryPage


        history = HistoryPage()

        history.mainloop()



    def open_quiz(self):

        self.withdraw()


        from gui.quiz_page import QuizPage


        quiz = QuizPage()

        quiz.mainloop()

    def open_dashboard(self):

        self.withdraw()

        from gui.dashboard_page import DashboardPage

        dashboard = DashboardPage()

        dashboard.mainloop()