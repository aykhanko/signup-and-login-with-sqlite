import sqlite3

class Users():
    def __init__(self):
        self.file_name = "users.db"
        self.connect()

    def connect(self):
        self.con = sqlite3.connect(self.file_name)
        self.cursor = self.con.cursor()

    def disconnect(self):
        self.con.close()
    
    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users_data (
        name TEXT,
        surname TEXT,
        email TEXT,
        password TEXT,
        salt TEXT
        )''')

        self.con.commit()
    
    def add_user(self,name, surname, email, password, salt):
        self.cursor.execute('''
        INSERT INTO users_data (name, surname, email, password, salt)
        VALUES (?, ?, ?, ?, ?)''',
        (name, surname, email, password, salt))

        self.con.commit()

    def users_info(self,name):
        self.cursor.execute("SELECT password, salt FROM users_data WHERE name = ?", (name,))
        user_info = self.cursor.fetchone()
        return user_info
    
    def names(self):
        self.cursor.execute('''SELECT name FROM users_data''')
        names = self.cursor.fetchall()
        return names
    
    def emails(self):
        self.cursor.execute('''SELECT email FROM users_data''')
        emails = self.cursor.fetchall()
        return emails
    
    
users = Users()
users.create_table()
users.disconnect()