"""
    Starting Out with Python by Tony Gaddis, fifth edition
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free (green checkmark upper right)
    Submit your completed file
"""
import sqlite3

# TODO 14.1 - 14.3 Opening a database connection with SQLite
print("=" * 10, "Section 14.1-14.3 opening a database connection", "=" * 10)

# establish a connection to an SQL database named dogs.db using dogs_connection as a variable
# Note: A new database should be created if it does not yet exist

dogs_connection = sqlite3.connect('dogs.db')
dogs_cursor = dogs_connection.cursor()

# create a cursor for working with your database named dogs_cursor

# NOTE: the following statement will delete the Dogs table if it exists
# This statement is included for testing purposes to ensure a clean slate
# each time you re-run your program (remove the # )

# dogs_cursor.execute("""DROP TABLE IF EXISTS Dogs""")

# TODO 14.4 Creating a Table
print("=" * 10, "Section 14.4 creating a table", "=" * 10)
# the following variable will be used in your execute command
table_structure = """CREATE TABLE IF NOT EXISTS Dogs (DogID INTEGER PRIMARY KEY NOT NULL, DogName TEXT, OwnerName TEXT, Breed TEXT)"""
dogs_cursor.execute(table_structure)
dogs_connection.commit()

# use the cursor variable to execute the SQL command in table_structure

# commit the changes using the database connection variable dogs_connection


# TODO 14.5 Adding data to a table
print("=" * 10, "Section 14.5 adding data to a table", "=" * 10)
# complete the following statement to add a total of four records to the table
# the first record has been added for you (remove the # from each line)
# dogs_cursor.execute("""INSERT INTO Dogs (DogName, OwnerName, Breed)
#                    VALUES ("Donovan", "Ben", "Golden Retriever"),
#                    """)
dogs_cursor.execute("""INSERT INTO Dogs (DogName, OwnerName, Breed) VALUES ("Donovan", "Ben", "Golden Retriever"), ("Sparky", "Ron", "Pug"),
("Rex", "Kevin", "Poodle"), ("Spinach", "Calvin", "Chihuahua")""")
dogs_connection.commit()

# commit your changes to make them visible to other database users


# TODO 14.6 Querying data with SELECT
print("=" * 10, "Section 14.6 querying data with SELECT", "=" * 10)
# write an execute statement to select all columns (fields) from the Dogs table
dogs_cursor.execute('SELECT * FROM Dogs')
row = dogs_cursor.fetchall()
for line in row:
    print(line)
# fetch all the results into a list variable

# use a for loop to display the results


# TODO 14.6-14.7 updating specific records
print("=" * 10, "Section 14.6-14.7 updating specific records", "=" * 10)
# add a WHERE clause to the following statement to select the dog with DogID 2
# (remove the # to test)
# dogs_cursor.execute("""SELECT * FROM Dogs""")
dogs_cursor.execute("""SELECT * FROM Dogs WHERE DogID = 2""")
print(dogs_cursor.fetchone())

dogs_cursor.execute('''UPDATE Dogs Set OwnerName = "Unknown" WHERE DogID == 2''')

dogs_cursor.execute("""SELECT * FROM Dogs WHERE DogID = 2""")
print(dogs_cursor.fetchone())


dogs_connection.commit()
dogs_connection.close()
# fetch and display the record found

# write an execute statement to update the record with DogID 2 to have OwnerName "Unknown"

# Select, fetch and display the updated record with DogID 2


# commit your changes (changes are only visible to your program until committed)

# close your connection to the database
