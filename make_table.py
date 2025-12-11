import sqlite3

conn = sqlite3.connect('products.db')
cursor = conn.cursor()

cursor.execute("CREATE TABLE products (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, price INTEGER)")

cursor.execute("INSERT INTO products (name, price) VALUES ('iPhone 15', 999)")
cursor.execute("INSERT INTO products (name, price) VALUES ('MacBook Pro', 1999)")
cursor.execute("INSERT INTO products (name, price) VALUES ('AirPods Pro', 249)")

conn.commit()
conn.close()