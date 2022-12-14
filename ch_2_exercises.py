"""
#     Starting Out with Python by Tony Gaddis, fifth edition
#     Complete all of the TODO directions
#     The number next to the TODO represents the chapter
#     and section in your textbook that explain the required code
#     Your file should compile error free (green checkmark upper right)
#     Submit your completed file
# """
#
# # TODO 2.3 display string output
print("=" * 10, "Section 2.3 string output", "=" * 10)
# # Write two lines of code:
# # the first one displays your name
# # the second displays your major
print("Danny Lara")
print("Computer Science")
#
# # TODO 2.3 using quotes
print("=" * 10, "Section 2.3 using quotes", "=" * 10)
# # Write a statement that displays:
# # The dog says "woof!"
print('The dog says "woof!"')
#
# # TODO 2.5 working with variables and printing their values
print("=" * 10, "Section 2.5 printing variable values", "=" * 10)
# # 1) Declare a variable named age, and set the initial value to your age
# # 2) Print the variable value
# # 3) Print the word age with a space and the variable value, example: age 25
# # 4) Assign 42 to the age variable
# # 5) Print the word age with a space and the new variable value, example: age 42
age = 22
print(age)
age = 42
print(f"age {age}")
#
#
# # TODO 2.6 keyboard input
print("=" * 10, "Section 2.6 keyboard input", "=" * 10)
# # 1) Use an input statement to ask the user to enter their name; assign the result to a variable called name
# # 2) Print a line that uses the variable to greets the user by name. Example: Hello, Meri
name = input("Enter your name: ")
print(f"Hello, {name}")
#
# # TODO 2.6 - 2.7 numeric input, performing calculations
print("=" * 10, "Section 2.6-2.7 numeric input and calculations", "=" * 10)
# # 1) Get the user to enter their age; store it as an integer. Use int() to convert the string to an integer.
# # 2) Print the age in a sentence using a comma in the print statement to separate items
# #    (when using a comma in a print statement, you can mix numbers and strings)
# #    example: "This year you are ", age
# # 3) Add 1 to the age: age = age + 1
# # 4) Print the result using the age in a full sentence
age = int(input("Enter your age: "))
print(f"This year you are, {age}")
print(f"Next year you'll be, {age + 1}")

# # TODO 2.7 performing calculations
print("=" * 10, "Section 2.7 performing calculations", "=" * 10)
#  1) Calculate 7 divided by 2; print the equation and the result
#  2) Calculate the remainder of 7 divided by 2 using the modulus operator; print the equation and the result
divide = (7/2)
modulus = (7 % 2)
print(f"7/2 = {divide}")
print(f"The remainder of 7/2 = {modulus}")


# TODO 2.7 data conversion
print("=" * 10, "Section 2.7 data conversion", "=" * 10)
# Write the equations as described below, the addition equation has been done as a sample
# Note: you don't need to assign the result to a variable when the result will only be displayed
# Sample:
# 0) Write an equation that adds an integer to an integer, display the equation and the result with a print statement
print("2 + 2 = " + str(2 + 2))

# 1) Write an equation that divides an integer by an integer, display the equation and the result with a print statement
print(f"8 / 2 = {int(8 / 2)}")
# 2) Write an equation that divides a float by a float, display the equation and the result with a print statement
print(f"10.5 / 5.5 = {float(10.5/5.5)}")
# 3) Write an equation that divides a float by an integer, display the equation and the result with a print statement
print(f"10.5/5 = {(10.5/5)}")

# TODO 2.8 Concatenating strings (Displaying Multiple Items with the + Operator)
print("=" * 10, "Section 2.8 concatenating strings", "=" * 10)
# 1) Have the user enter their name using an input statement
# 2) Greet the user using a print statement; concatenate "Hello" and their name into one string
name = input("Enter your name: ")
print("Hello " + str(name))

# TODO 2.9 Using print statement options
print("=" * 10, "Section 2.9 print statement options", "=" * 10)
# Modify the following code to display on one line, WITHOUT merging the lines of code.
# The words should be separated by a hyphen. The result should look like this: one-two-three
# DO NOT MERGE INTO ONE LINE OF CODE, use print statement options to get the desired result.
print('one-', end='')
print('two-', end='')
print('three')

# TODO 2.9 Using escape codes
print("=" * 10, "Section 2.9 escape codes", "=" * 10)
# Modify the following line of code to add tabs between the days of the week
print("Sunday\tMonday\tTuesday\tWednesday\tThursday\tFriday\tSaturday")


# TODO 2.10 Formatting numbers
print("=" * 10, "Section 2.10 formatting numbers", "=" * 10)
# Modify the print statement to format the value in the variable number using a format specifier.
#  - to display a minimum field width of 30
#  - to include commas
#  - to use a precision of two decimal places to the right of the decimal point
# example result:
#               6,548,974,897.57
number = 6548974897.5687979797
print(f'{number:.2f}')


# TODO 2.10 Formatting percentage
print("=" * 10, "Section 2.10 formatting a percentage", "=" * 10)
# Print the variable percentage using a percentage format with a precision of 2
# example result: 76.54%
percentage = .7654
print(f'{percentage:.2%}')


# TODO 2.11 Named Constants
print("=" * 10, "Section 2.11 Named Constants", "=" * 10)
# You have been given the following information:
TAX_RATE = 0.09
amount = 34.12
# Complete the following: multiply the amount by the named constant
tax_owed = amount * TAX_RATE
# Complete the following to display the result using a currency format (2 decimal places)
print(f"Tax: ${tax_owed:.2f}")
