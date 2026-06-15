import sqlite3


def create_database():

    conn = sqlite3.connect("atlas.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    conn.commit()
    conn.close()



def register_user(username, password):

    conn = sqlite3.connect("atlas.db")
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO users(username,password) VALUES(?,?)",
            (username,password)
        )

        conn.commit()
        return True

    except sqlite3.IntegrityError:
        return False

    finally:
        conn.close()



def login_user(username,password):

    conn = sqlite3.connect("atlas.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username,password)
    )

    user = cursor.fetchone()

    conn.close()

    return user



def create_chat_table():

    conn = sqlite3.connect("atlas.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS chats(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        question TEXT,
        answer TEXT,
        time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()



def save_chat(username, question, answer):

    conn = sqlite3.connect("atlas.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO chats(username,question,answer)
        VALUES(?,?,?)
        """,
        (username,question,answer)
    )

    conn.commit()
    conn.close()

def get_chat_history(username):

    conn = sqlite3.connect("atlas.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT question, answer, time
        FROM chats
        WHERE username=?
        ORDER BY id DESC
        """,
        (username,)
    )

    data = cursor.fetchall()

    conn.close()

    return data

def create_quiz_table():

    conn = sqlite3.connect("atlas.db")

    cursor = conn.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS quiz_records(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        topic TEXT,
        quiz TEXT,
        time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)


    conn.commit()

    conn.close()



def save_quiz(username, topic, quiz):

    conn = sqlite3.connect("atlas.db")

    cursor = conn.cursor()


    cursor.execute(
        """
        INSERT INTO quiz_records(
        username,topic,quiz
        )
        VALUES(?,?,?)
        """,
        (
            username,
            topic,
            quiz
        )
    )


    conn.commit()

    conn.close()

def get_chat_count(username):

    conn = sqlite3.connect("atlas.db")

    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT COUNT(*)
        FROM chats
        WHERE username=?
        """,
        (username,)
    )


    count = cursor.fetchone()[0]


    conn.close()


    return count



def get_quiz_count(username):

    conn = sqlite3.connect("atlas.db")

    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT COUNT(*)
        FROM quiz_records
        WHERE username=?
        """,
        (username,)
    )


    count = cursor.fetchone()[0]


    conn.close()


    return count