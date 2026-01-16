import sqlite3
conn = sqlite3.connect('points.db')
cursor = conn.cursor()

query = """
    CREATE TABLE IF NOT EXISTS points(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    city NOT NULL,
    name NOT NULL
);
"""
cursor.execute(query)
conn.commit()
conn.close()