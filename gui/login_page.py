import customtkinter as ctk
from database.db import register_user, login_user
from gui.register_page import RegisterPage


class LoginPage(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("ATLAS Login")
        self.geometry("500x400")

        self.label = ctk.CTkLabel(
            self,
            text="ATLAS Login",
            font=("Arial", 24)
        )
        self.label.pack(pady=20)

        self.username_entry = ctk.CTkEntry(
            self,
            placeholder_text="Username",
            width=250
        )
        self.username_entry.pack(pady=10)

        self.password_entry = ctk.CTkEntry(
            self,
            placeholder_text="Password",
            show="*",
            width=250
        )
        self.password_entry.pack(pady=10)

        self.login_button = ctk.CTkButton(
            self,
            text="Login",
            command=self.login
        )
        self.login_button.pack(pady=20)

        self.goto_register_button = ctk.CTkButton(
            self,
            text="Create Account",
            command=self.open_register_page
        )
        self.goto_register_button.pack(pady=10)

    def login(self):

        username = self.username_entry.get()
        password = self.password_entry.get()

        user = login_user(username, password)

        if user:

            from config.user_session import set_user

            set_user(username)

            print("Login Success")

            self.withdraw()

            from gui.tutor_page import TutorPage

            tutor = TutorPage()
            tutor.mainloop()

        else:
            print("Login Failed")


    def register_user_account(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        register_user(username, password)

        print("User Registered")

    def open_register_page(self):

        self.withdraw()

        register_window = RegisterPage()
        register_window.mainloop()
