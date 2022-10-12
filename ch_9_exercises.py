"""
    Starting Out with Python by Tony Gaddis, fifth edition
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free (green checkmark upper right)
    Submit your completed file
"""
import pickle
# TODO 9.1 Dictionaries
print("=" * 10, "Section 9.1 dictionaries", "=" * 10)
# 1) Finish creating the following dictionary by adding three more people and birthdays
birthdays = {'Meri': 'May 16', 'Kathy': 'July 14', 'Danny': 'January 21', 'Ryan': 'March 13', 'Lisa': 'April 10'}

# 2) Use the key to retrieve and print Meri's Birthday
print(f"Meri's birthday is {birthdays['Meri']}")
# 3) Create an empty dictionary named registration
registration = {}

# You will use the following dictionary for many of the remaining exercises
miles_ridden = {'June 1': 25, 'June 2': 20, 'June 3': 38, 'June 4': 12, 'June 5': 30, 'June 7': 25}

# 1) Print the keys and the values of miles_ridden using a for loop
print('Keys: ')
for line in miles_ridden:
    print(line)
print()
print('Values: ')
for line in miles_ridden.values():
    print(line)
print()

# 2) Use the get() method to get the value for June 3 (replace the "")
#    if not found, the result should be 'Entry not found'
value = miles_ridden.get('June 3', "Entry not found")
print(value)
print()
# 3) Use the get() method to get the value for June 6 (replace the "")
#    if not found, the result should be 'Entry not found'
value2 = miles_ridden.get('June 6', 'Entry not found')
print(value2)
print()
# 4) Use the values method to print all values in the miles_ridden dictionary
print(miles_ridden.values())
print()
# 5) Use the keys method to print all keys in miles_ridden
print(miles_ridden.keys())
print()
# 6) Use the pop method to remove June 4 then print the contents of the dictionary
miles_ridden.pop('June 4')
print(miles_ridden)
print()
# 7) Use the items method to print the contents of the miles_ridden dictionary
print(miles_ridden.items())
print()
# TODO 9.2 Sets
print("=" * 10, "Section 9.2 sets", "=" * 10)
# 1) Create an empty set named my_set
my_set = set()

# 2) Create a set named days that contains the names of the days of the week
days = {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'}

# 3) Get the number of elements from the days set and print it
print(len(days))
print()
# 4) Remove Saturday and Sunday from the days set
days.remove('Saturday')
days.remove('Sunday')

# 5) Determine if 'Mon' is in the days set
temp = 0
for day in days:
    if day == 'Mon':
        temp = 1
if temp == 1:
    print("'Mon' is in the days set")
else:
    print("'Mon' is not in the days set")

# TODO 9.3 Serializing Objects (Pickling)
print("=" * 10, "Section 9.3 serializing objects using the pickle library", "=" * 10)
# 1) Import the pickle library at the top of this file

# 2) Create the output file log.dat and open it for binary writing
file = open('log', 'wb')

# 3) Pickle the miles_ridden dictionary and output it to the log file
pickle.dump(miles_ridden, file)

# 4) Close the log file
file.close()
