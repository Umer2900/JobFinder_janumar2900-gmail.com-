import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect('recruitment.db')
    c = conn.cursor()
    
    # Create tables
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE,
        username TEXT,
        password TEXT,
        user_type TEXT,
        created_at TIMESTAMP
    )''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS resumes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        filename TEXT,
        file_content BLOB,
        upload_date TIMESTAMP,
        analysis TEXT,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )''')
    
    conn.commit()
    conn.close()

# Initialize the database when the module is imported
init_db()



def delete_account(user_id):
    conn = sqlite3.connect('recruitment.db')
    c = conn.cursor()
    
    # Delete associated resumes first due to foreign key constraint
    c.execute("DELETE FROM resumes WHERE user_id = ?", (user_id,))
    
    # Delete the user
    c.execute("DELETE FROM users WHERE id = ?", (user_id,))
    
    conn.commit()
    conn.close()



