import customtkinter as ctk
from database.db import register_user



class RegisterPage(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("ATLAS Register")
        self.geometry("500x450")

        self.label = ctk.CTkLabel(
            self,
            text="Create Account",
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

        self.confirm_entry = ctk.CTkEntry(
            self,
            placeholder_text="Confirm Password",
            show="*",
            width=250
        )
        self.confirm_entry.pack(pady=10)

        self.register_button = ctk.CTkButton(
            self,
            text="Register",
            command=self.register_user_account
        )
        self.register_button.pack(pady=20)

        self.back_button = ctk.CTkButton(
            self,
            text="Back To Login",
            command=self.back_to_login
        )
        self.back_button.pack(pady=10)

    def register_user_account(self):

        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm = self.confirm_entry.get()

        if password != confirm:
            print("Passwords do not match")
            return

        success = register_user(username, password)

        if success:

            self.register_button.configure(
                state="disabled"
            )

            self.after(
                100,
                self.back_to_login
            )


        else:

            print("Username Already Exists")


    def back_to_login(self):

        self.withdraw()

        from gui.login_page import LoginPage

        login_window = LoginPage()
        login_window.mainloop()