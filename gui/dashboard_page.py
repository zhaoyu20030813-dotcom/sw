import customtkinter as ctk

from config.user_session import get_user
from database.db import (
    get_chat_count,
    get_quiz_count
)


class DashboardPage(ctk.CTk):


    def __init__(self):

        super().__init__()


        self.title("ATLAS Dashboard")
        self.geometry("700x500")


        username = get_user()


        self.title_label = ctk.CTkLabel(
            self,
            text=f"Welcome {username}",
            font=("Arial",30)
        )

        self.title_label.pack(pady=30)



        chat = get_chat_count(username)

        quiz = get_quiz_count(username)



        self.chat_label = ctk.CTkLabel(
            self,
            text=f"Chat Records: {chat}",
            font=("Arial",22)
        )

        self.chat_label.pack(pady=20)



        self.quiz_label = ctk.CTkLabel(
            self,
            text=f"Quiz Records: {quiz}",
            font=("Arial",22)
        )

        self.quiz_label.pack(pady=20)



        self.back_button = ctk.CTkButton(
            self,
            text="Back",
            command=self.back
        )

        self.back_button.pack(pady=30)



    def back(self):

        self.withdraw()


        from gui.tutor_page import TutorPage


        tutor = TutorPage()

        tutor.mainloop()