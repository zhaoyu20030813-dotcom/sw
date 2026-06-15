import customtkinter as ctk

from ai.openai_client import ask_gpt


class QuizPage(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.title("ATLAS Quiz")
        self.geometry("900x650")


        self.title_label = ctk.CTkLabel(
            self,
            text="AI Quiz Generator",
            font=("Arial", 28)
        )

        self.title_label.pack(pady=20)



        self.topic_entry = ctk.CTkEntry(
            self,
            width=500,
            placeholder_text="Enter topic"
        )

        self.topic_entry.pack(pady=10)



        self.generate_button = ctk.CTkButton(
            self,
            text="Generate Quiz",
            command=self.generate_quiz
        )

        self.generate_button.pack(pady=10)



        self.quiz_box = ctk.CTkTextbox(
            self,
            width=700,
            height=300
        )

        self.quiz_box.pack(pady=20)



        self.back_button = ctk.CTkButton(
            self,
            text="Back",
            command=self.back_to_tutor
        )

        self.back_button.pack(pady=10)



    def generate_quiz(self):

        topic = self.topic_entry.get()


        prompt = f"""
Create a quiz about {topic}.

Format:

Question:
A.
B.
C.
D.

Correct Answer:
Explanation:
"""


        try:

            result = ask_gpt(prompt)


        except Exception as e:

            result = "AI Error: " + str(e)



        self.quiz_box.delete(
            "1.0",
            "end"
        )


        self.quiz_box.insert(
            "end",
            result
        )



    def back_to_tutor(self):

        self.withdraw()


        from gui.tutor_page import TutorPage


        tutor = TutorPage()

        tutor.mainloop()