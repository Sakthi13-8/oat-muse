import sqlite3

def init_db():
    conn = sqlite3.connect("oatmuse.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_name TEXT,
        email TEXT,
        phone TEXT,
        address TEXT,
        total REAL
    )
    """)

    conn.commit()
    conn.close()