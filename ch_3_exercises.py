"""
    Starting Out with Python by Tony Gaddis, fifth edition
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free (green checkmark upper right)
    Submit your completed file
"""

# TODO 3.1 Relational Operators


print("=" * 10, "Section 3.1 relational operators", "=" * 10)
# 1) Write a boolean expression using the variables below and a
#    greater-than sign that will evaluate to true.
#    Include the expression in a print statement to display the result.
# 2) Write a boolean expression using the variables below that
#    compares two of the variables to see if they are equal.
#    Include the expression in a print statement to display the result.
# 3) Write a boolean expression using the variables below to compare
#    two of the variables to see if they are NOT equal.
#    Include the expression in a print statement to display the result.
# 4) Write a boolean expression using the variables below that uses
#    the less than or equal to operator.
#    Include the expression in a print statement to display the result.

# variables
a = 6
b = 8
c = 5

# 1 sample answer
if a > 3:
    print(f"a > 3 = {a > 3}")
# 2
if a == b:
    print(f"a = b is {a == b}")
else:
    print(f"a = b is {a == b}")
# 3
if a != c:
    print(f"a does not equal c: {a != c}")
# 4
if a <= b:
    print(f"a less than or equal to b: {a <= b}")

# TODO 3.2 the if else statement
print("=" * 10, "Section 3.2 if-else", "=" * 10)
# Add code below to determine if age is greater than or equal to 18
# Depending on the answer, display the appropriate statement:
#    "You are old enough to vote" or "You are not old enough to vote"
# Use the if-else structure (remember to use proper indentation)
age = int(input("How old are you? "))
if age >= 18:
    print("You are old enough to vote!")
else:
    print("You are not old enough to vote.")

# TODO 3.3 comparing strings
print("=" * 10, "Section 3.3 comparing strings", "=" * 10)
# Complete the code below so that if the user input matches the password
# it will display "that is correct"; otherwise display "that is not correct"
password = "narwhals"
user_password = input("Please enter the password:  ")
if user_password == "narwhals":
    print("Password accepted")
else:
    print("Password denied")

# TODO 3.4 if - elif - else
print("=" * 10, "Section 3.4 if-elif-else", "=" * 10)
# Complete the code to accept a number between 1 and 5 from the user
# and display a roman numeral for that number. If the number entered is
# not between 1 and 5, have the else statement display "That is not a valid number"

number = int(input("Please enter a number between 1 and 5: "))
if 1 <= number <= 5:
    if number == 1:
        print("I")
    if number == 2:
        print("II")
    if number == 3:
        print("III")
    if number == 4:
        print("IV")
    if number == 5:
        print("V")
else:
    print("This is not a valid number")

# TODO 3.4 a series of conditions
print("=" * 10, "Section 3.4 multiple conditions", "=" * 10)
# Buffet prices are based on the persons age. If the person is a senior
# citizen (62 or over), the charge is $9.89. If the person is age 12-
# 61, the charge is $12.89. If it is a child of under age 3, they eat
# for free. If the child is between 3 and 11 they are charged $0.99 for
# each year of age. Complete the partial code below to determine cost.
# HINT: Organize the options in order according to age to simplify the logic.
# SEE PROGRAM 3-6 FOR AN EXAMPLE USING GRADES -- the first example shows a full
# traditional ELSE IF structure, there is also a simpler example using IF-ELIF-ELSE.

# Write the code here to determine the correct cost based on age
cost_senior = 9.89
cost_regular = 12.89
cost_baby = 0
cost_child = 0.99

customer_age = int(input("How old is the customer?   "))
if customer_age >= 62:
    print(f"Your cost for a customer who is {customer_age} years old", end=" ")
    print(f"will be ${cost_senior:.2f}")

elif customer_age >= 12:
    print(f"Your cost for a customer who is {customer_age} years old", end=" ")
    print(f"will be ${cost_regular:.2f}")
elif customer_age >= 3:
    print(f"Your cost for a customer who is {customer_age} years old", end=" ")
    print(f"will be ${cost_child * customer_age:.2f}")
else:
    print(f"Your cost for a customer who is {customer_age} years old", end=" ")
    print(f"will be free")

# TODO 3.5 Logical Operators
print("=" * 10, "Section 3.5 logical operators", "=" * 10)
# Using the variables below, create compound Boolean expressions using logical operators
# Example: d > f or e == f
d = 10
e = 10
f = 12
# 1) write a print statement using the and operator that will evaluate to true
print(e <= d and e < f)
# 2) write a print statement using the or operator that will evaluate to true
print(d > f or f > e)
# 3) write a print statement using the not operator that will evaluate to true
print(not d == f)

# TODO 3.6 Boolean variables
print("=" * 10, "Section 3.6 boolean variables", "=" * 10)
# You are programming a baby doll. If the baby doll is tired, it will close its eyes
# if it is hungry, it will cry. Write code to print  "Eyes open" or "Eyes closed" depending
# on the tired value. Then print "Crying" or "quiet" depending on the hungry variable
tired = True
hungry = False
if tired:
    print("Eyes closed")
else:
    print("Eyes open")
if hungry:
    print("Crying")
else:
    print("Quiet")
