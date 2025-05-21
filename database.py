import sqlite3
from datetime import datetime

DB_NAME = "prices.db"

def create_tables():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT,
            title TEXT,
            image TEXT
        )
    ''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS prices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER,
            price REAL,
            timestamp TEXT,
            FOREIGN KEY(product_id) REFERENCES products(id)
        )
    ''')

    conn.commit()
    conn.close()

def insert_product(url, title, image):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("SELECT id FROM products WHERE url = ?", (url,))
    result = c.fetchone()

    if result:
        product_id = result[0]
    else:
        c.execute("INSERT INTO products (url, title, image) VALUES (?, ?, ?)", (url, title, image))
        conn.commit()
        product_id = c.lastrowid

    conn.close()
    return product_id

def insert_price(product_id, price):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    timestamp = datetime.now().isoformat()
    c.execute("INSERT INTO prices (product_id, price, timestamp) VALUES (?, ?, ?)",
              (product_id, price, timestamp))
    conn.commit()
    conn.close()
if __name__ == "__main__":
    create_tables()
    print("Database & tables created!")