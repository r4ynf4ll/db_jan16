import sqlite3
conn = sqlite3.connect('points.db')
cursor = conn.cursor()

query = """
    INSERT INTO points(city,name)
    VALUES
    ('Buffalo','Bills')
"""
cursor.execute(query)
conn.commit()
conn.close()