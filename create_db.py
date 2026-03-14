import sqlite3

conn = sqlite3.connect("database.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS students(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
room_no TEXT,
email TEXT,
due_date INTEGER,
fee_status TEXT
)
""")

conn.commit()
conn.close()

print("Table ready")