import sqlite3


class DataBase:
    def __init__(self, db_name='users.db'):
        self.connect = sqlite3.connect(db_name)
        self.cursor = self.connect.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR (40) NOT NULL,
                email TEXT UNIQUE NOT NULL,
                age INTEGER
            )
    """)

        self.connect.commit()

    def add_user(self, user):
        self.cursor.execute("INSERT INTO users (name, email, age) VALUES (?,?,?)", (user.name, user.email, user.age))

        self.connect.commit()

    def get_user(self, email):
        self.cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        return self.cursor.fetchone()
    
    def get_all(self):
        self.cursor.execute("SELECT name, age FROM users")
        return self.cursor.fetchall()

    def close(self):
        self.connect.close()