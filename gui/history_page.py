import customtkinter as ctk

from database.db import get_chat_history
from config.user_session import get_user


class HistoryPage(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.title("ATLAS History")
        self.geometry("800x600")


        self.label = ctk.CTkLabel(
            self,
            text="Learning History",
            font=("Arial", 28)
        )

        self.label.pack(pady=20)


        self.history_box = ctk.CTkTextbox(
            self,
            width=700,
            height=450
        )

        self.history_box.pack(pady=20)


        self.back_button = ctk.CTkButton(
            self,
            text="Back",
            command=self.back_to_tutor
        )

        self.back_button.pack(pady=10)


        self.load_history()



    def load_history(self):

        username = get_user()

        records = get_chat_history(username)


        if not records:

            self.history_box.insert(
                "end",
                "No history yet."
            )

            return


        for item in records:

            question = item[0]
            answer = item[1]
            time = item[2]


            text = f"""
Time:
{time}

Question:
{question}

AI Answer:
{answer}

---------------------

"""


            self.history_box.insert(
                "end",
                text
            )



    def back_to_tutor(self):

        self.withdraw()

        from gui.tutor_page import TutorPage

        tutor = TutorPage()

        tutor.mainloop()