import sqlite3

try:
    conn = sqlite3.connect("auth.db")
    print("SQLite connected successfully")
    conn.close()
except sqlite3.Error as e:
    print(f"SQLite error: {e}")

