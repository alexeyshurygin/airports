# database_setup.py
import sqlite3

def setup_database():
    conn = sqlite3.connect('airports.db')
    with open('data_dump.sql', 'r') as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_database()
