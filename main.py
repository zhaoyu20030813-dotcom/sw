from database.db import (
    create_database,
    create_chat_table,
    create_quiz_table
)

from gui.login_page import LoginPage


create_database()

create_chat_table()

create_quiz_table()


app = LoginPage()

app.mainloop()