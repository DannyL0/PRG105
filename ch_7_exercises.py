"""
    Starting Out with Python by Tony Gaddis, fifth edition
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free (green checkmark upper right)
    Submit your completed file
"""

# TODO 7.2 Lists
print("=" * 10, "Section 7.2 lists", "=" * 10)
# 1) Create a list of days of the week, assign it to the variable days, remove """ """ to test

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# 2) Create a list with 5 items, set them all to 0, use the Repetition Operator ( * )

list0 = [0] * 5
# 3) Print the contents of your days list using the for operator
for day in days:
    print(day)
# 4) Print the list item that holds the value Saturday from the days list by using its index
print(days[6])
# 5) Create a variable called size to hold the length of the list days using the len function
size = len(days)
# 6) Concatenate the two following lists together, storing the value in list3 - remove the """ """ to test


list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]
list3 = list1 + list2
print(list3)

# TODO 7.3 List Slicing
print("=" * 10, "Section 7.3 list slicing", "=" * 10)
# Slice the list days to select from Monday through Friday, inclusive, and assign the new list to work_days
# Print work_days
work_days = days[:5]
print(work_days)

# TODO 7.4 Finding items in Lists with the in Operator
print("=" * 10, "Section 7.4 using the in operator", "=" * 10)
# Use the in operator to determine whether "Tue" is in the list days
# Based on the result, display "yes, Tue is in the list" or "no, Tue is not in the list"
if "Tue" in days:
    print("yes, Tue is in the list")
else:
    print("no, Tue is not in the list")

# TODO 7.5 List Methods and Useful Built-in Functions
print("=" * 10, "Section 7.5 list methods and functions", "=" * 10)
# 1) Use append() to append the last three months of the year to the list months.
# NOTE: make sure the months are appended as individual list items
months = list(["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept"])
three_months = list(["Oct", "Nov", "Dec"])
for month in three_months:
    months.append(month)
# 2) Get the index of "May" from the months list and print it on screen
x = months.index("May")
print(f"May Index: {x}")
# 3) Sort list3 from exercise 7.2 and print the results on screen
list3.sort()
print(list3)
# 4) Reverse the order of list3
list3.reverse()
print(list3)
# 5) Delete the number 5 from list3 and print the list(remember we reversed the list)
list3.remove(5)
print(list3)
# 6) Print the maximum value from list3
maximum = max(list3)
print(maximum)

# TODO 7.6 Copying Lists
print("=" * 10, "Section 7.6 copying lists", "=" * 10)
# Copy the list months to the variable months_of_the_year
# Print the values in months_of_the_year
months_of_the_year = months.copy()
print(months_of_the_year)

# TODO 7.7 Processing lists
print("=" * 10, "Section 7.7 processing lists", "=" * 10)
# 1) Total the values in list3 and print the results
total = sum(list3)
# 2) Get the average of values in list3 and print the results
avg = sum(list3) / len(list3)
# 3) Open the file states.txt in read mode,
# -- read the contents of the file into the list states_list
# -- print the contents of states_list on screen
file = open("states.txt", "r")
states_list = file.read()
print(states_list)
file.close()
# TODO 7.8 List Comprehensions
print("=" * 10, "Section 7.8 list comprehensions", "=" * 10)
# Use list comprehension to create a new list whose values are the squares of my_list's values
# display the new list
my_list = [1, 5, 7, 22, 37, 90]
squared_numbers = [number ** 2 for number in my_list]
print(squared_numbers)
# TODO 7.9 Two-Dimensional Lists
print("=" * 10, "Section 7.9 two-dimensional lists", "=" * 10)
# 1) Create a new two-dimensional list named days_in_month
#     the outer list should have twelve elements, one for each month
#     the element for each month should be a list holding the month name and number of days
#     So, days_in_month[0][0] is January and days_in_month[0][1] is 31
days_in_month = [["January", 31], ["February", 28], ["March", 31], ["April", 30], ["May", 31], ["June", 30], ["July", 31], ["August", 30], ["September", 31], ["October", 30], ["November", 31], ["December", 30]]
# 2) Print the contents of the entire list
for contents in days_in_month:
    print(contents)
# 3) Print just the values for index 3,0 and 3,1
print(days_in_month[3][0], days_in_month[3][1])

# TODO 7.10 Tuples
print("=" * 10, "Section 7.10 tuples", "=" * 10)
# Create a tuple using the months list as its data source
column = [row[0] for row in days_in_month]
print(column)

output = tuple(column)
print(output)
