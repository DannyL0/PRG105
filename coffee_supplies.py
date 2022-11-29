import sqlite3

try:
    conn = sqlite3.connect('coffee.db')
    cur = conn.cursor()
    cur.execute('SELECT Category FROM Coffee')
    results = cur.fetchall()

    categories = []
    for category in results:
        if category[0] not in categories:
            categories.append(category[0])

    print("CATEGORY----------Product--------Supplier")
    categories.sort()
    for category in categories:
        print(category)
        cur.execute('SELECT * FROM Coffee WHERE Category == ?', (category,))
        product_list = cur.fetchall()
        for product in product_list:
            print(f"----------{product[1]:20}---{product[3]}")

    conn.commit()
    conn.close()
except sqlite3.Error as err:
    print(f"%SQL error encountered: {err}")
