"""
    Starting Out with Python by Tony Gaddis, fifth edition
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free (green checkmark upper right)
    Submit your completed file
"""

# TODO 4.2 A condition controlled loop
print("=" * 10, "Section 4.2 condition controlled loop", "=" * 10)
# Write a while loop that will change the variable in num by subtracting 1,
# then print the variable. Keep looping until num = 0, ie. while num > 0:
num = 10
# write your code here, the variable needs to exist before you start the loop
while num >= 0:
    print(num)
    num -= 1

# TODO 4.3 the For Loop
print("=" * 10, "Section 4.3 for loop", "=" * 10)
# Use a for-in loop with a list of the days of the week,
# print each day of the week
# SEE PROGRAM 4-6 FOR AN EXAMPLE
weeks = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
for day in weeks:
    print(day)

# TODO 4.3 using range() in a for loop
print("=" * 10, "Section 4.3 using range() in a for loop", "=" * 10)
# use the range function to print the numbers from 1 to 10
y = range(1, 11)
for x in y:
    print(x)

# TODO 4.3 using range() with a step value
print("=" * 10, "Section 4.3 using range() with a step value", "=" * 10)
# use the range function to print the odd numbers from 5 to 15
value = range(5, 16, 2)
for odd in value:
    print(odd)

# TODO 4.3 using the control variable in a for loop
print("=" * 10, "Section 4.3 using the control variable in a for loop", "=" * 10)
# NOTE: The terms "Control Variable" and "Target Variable" both refer to the for loop variable
# 1) Write a for loop using range(1,10) and a control variable called number
# 2) Inside the loop, print the result of number times 7
number = range(1, 10)
for target in number:
    print(target * 7)

# TODO 4.4 a running total
print("=" * 10, "Section 4.4 running total", "=" * 10)
# Use a loop to have the user enter 5 numbers, provide a total at the end
# You will need to initialize your accumulator before entering the loop
# You can assume valid integers are entered
total = 0.0
print(f"This will calculate the sum of {5} numbers you will enter")
for counter in range(5):
    numbers = int(input("Enter a number: "))
    total = total + numbers
print(f'The total of the numbers:{total} ')

# TODO 4.5 Sentinel Value
print("=" * 10, "Section 4.5 sentinel value", "=" * 10)
# Create a variable to store a total amount. Initialize it to zero.
# Initialize another variable to store a count of the numbers entered.
# Use a while loop to have the user enter test scores until
# a sentinel value of -1 is entered.
# After the loop, display the total, the count, and the average (total / count)
total_amount = 0.0
counting = 1
sentinel = -1

score = int(input("Enter a test score, -1 to end: "))
while score != sentinel:
    total_amount = total_amount + score
    counting = counting + 1
    score = int(input("Enter a test score, -1 to end: "))
average = f"{total_amount / counting:.2f}"
print(f"Your total amount is {total_amount}")
print(f"Your number count is {counting}")
print(f"Your average is {average}")

# TODO 4.6 validating data
print("=" * 10, "Section 4.6 data validation loop", "=" * 10)
# Ask the user to enter a number between 1 and 10.
# Use a while loop to force the user to repeat the
# input until the user enters a valid number. Test with
# both valid and invalid data.
values = int(input("Please enter a value between 1 and 10: "))
while 1 > values > 10:
    values = int(input("That was not a correct number, enter a value between 1 and 10: "))
print("You entered a value between 1 and 10")
