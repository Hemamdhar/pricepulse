import sqlite3

conn = sqlite3.connect("prices.db")
c = conn.cursor()

print("\n== PRODUCTS ==")
for row in c.execute("SELECT id, title FROM products"):
    print(row)

print("\n== PRICES ==")
for row in c.execute("SELECT * FROM prices"):
    print(row)

conn.close()
