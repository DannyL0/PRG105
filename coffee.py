import sqlite3

try:
    conn = sqlite3.connect('coffee.db')
    cur = conn.cursor()
    cur.execute(
        """CREATE TABLE IF NOT EXISTS Coffee(ProductID INTEGER PRIMARY KEY NOT NULL, Product TEXT, Category TEXT, Supplier TEXT)""")
    conn.commit()
    try:
        file = open('coffeehouse_supplies.csv', 'r')
        count = 0
        for line in file:
            count += 1
            value = line.strip().split(',')
            cur.execute("""INSERT INTO Coffee(Product, Category, Supplier) VALUES (?, ?, ?)""",
                        (value[0], value[1], value[2]))
        print(f"Number of records added: {count}")
        conn.commit()
        conn.close()
    except IOError:
        print("Couldn't access coffeehouse_supplies.csv")


except sqlite3.Error as err:
    print(f"%SQL error encountered: {err}")
