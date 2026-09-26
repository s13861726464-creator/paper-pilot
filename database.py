import sqlite3

conn = sqlite3.connect("paperpilot.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL
)
""")
cursor.execute("SELECT id, title FROM tasks")

rows = cursor.fetchall()

print(rows)
conn.commit()
conn.close()