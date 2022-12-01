import sqlite3

conn = sqlite3.connect("pets.db")
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS Owners (OwnerID INTEGER PRIMARY KEY NOT NULL, OwnerName TEXT, OwnerPhone TEXT)""")
cur.execute("""CREATE TABLE IF NOT EXISTS Pets (PetID INTEGER PRIMARY KEY NOT NULL, PetName TEXT, PetType TEXT, PetBreed TEXT, OwnerID INTEGER, FOREIGN KEY (OwnerID) REFERENCES Owners(OwnerID))""")
conn.commit()

owners_file = open("Owners.txt", "r")
pets_file = open("Pets.txt", "r")

for line in owners_file:
    data = line.strip().split(",")
    cur.execute("INSERT INTO Owners(OwnerName, OwnerPhone) VALUES(?, ?)", (data[0], data[1]))

for line in pets_file:
    data = line.strip().split(",")
    cur.execute("INSERT INTO Pets(PetName, PetType, PetBreed, OwnerID) VALUES(?, ?, ?, ?)", (data[0], data[1], data[2], data[3]))

conn.commit()


cur.execute("SELECT * FROM Owners")
results = cur.fetchall()
for row in results:
    print(f"\nOwner Name: {row[1]}, Phone: {row[2]}")
    cur.execute("SELECT * FROM Pets WHERE OwnerID == ?", (row[0],))
    for pet in cur.fetchall():
        print(f"--{pet[1]} is a {pet[3]} {pet[2]}")
