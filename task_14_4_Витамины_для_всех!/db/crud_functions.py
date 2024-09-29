import sqlite3


def initiate_db():
    conn = sqlite3.connect('./db/Products.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')
    cursor.execute('DELETE FROM Products')
    for i in range(1, 5):
        cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
                       (f'Витамины №{i}', f'Описание витаминов №{i}', i * 150))
    conn.commit()
    conn.close()


def get_all_products():
    conn = sqlite3.connect('./db/Products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    conn.close()
    return products
