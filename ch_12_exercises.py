"""
    Starting Out with Python by Tony Gaddis, fifth edition
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free (green checkmark upper right)
    Submit your completed file
"""

# TODO 12.1 simple recursion
print("=" * 10, "Section 12.1 simple recursion", "=" * 10)


# 1) Using program 12-2 as an example, create a recursive function.
#    The function should print "Hooray!" the number of times requested
#    by the parameter times_requested
def main():
    message(5)


def message(count):
    if count > 0:
        print("Hooray!")
        message(count - 1)


# 2) Call the function with a parameter value of 5.

main()
# TODO 12.2-12.3 problem solving with recursion
print("=" * 10, "Section 12.2-12.3 problem solving with recursion", "=" * 10)


# 1) Create a function that uses recursion to sum all of the numbers in a list.
#    The function should have only one parameter, the list of numbers
#    and it should return the sum of the list values.
# Hint: Each iteration should remove one item from the list.
# The recursion should end when all items have been removed from the list.
def main2():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    print(sum_numbers(numbers))


def sum_numbers(list_numbers):
    if len(list_numbers) == 1:
        return list_numbers[0]
    else:
        return list_numbers[0] + sum_numbers(list_numbers[1:])


main2()
# 2) Call the function using the numbers list as a parameter
