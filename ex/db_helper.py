import sqlite3
from sqlite3 import Connection
from .models import User

class Db_interaction:
    def __init__(self) -> None:
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS Users (
                        id INTEGER PRIMARY KEY, 
                        name TEXT, 
                        email TEXT)''')
        conn.close()
        
    def get_connection(self) -> Connection:
        return sqlite3.connect('example.db')
    
    def insert_user(self, user : User) -> bool:
        try:
            conn = self.get_connection()
            cursor = conn.cursor()

            cursor.execute("INSERT INTO Users (id,name, email) VALUES (?,?, ?)", (user.user_id,user.name, user.email))
            
            conn.commit()
            conn.close()
            return True
        except sqlite3.IntegrityError as e:
            print(f"Integrity Error: {e}")
            return False
        
    def get_users(self) -> list[User]:
        users:User = []
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM Users")
        rows = cursor.fetchall()
        print('rre')
        for row in rows:
            users.append(User(row[0],row[1],row[2]))

        conn.close()
        return users
