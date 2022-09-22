def divisible_five(number):  # These three functions are for calculation
    if number % 5 == 0:
        print(f"{number} is divisible by five")
    else:
        print(f"{number} is not divisible by five")


def divisible_three(number):
    if number % 3 == 0:
        print(f"{number} is divisible by three")
    else:
        print(f"{number} is not divisible by three")


def divisible_two(number):
    if number % 2 == 0:
        print(f"{number} is divisible by two")
    else:
        print(f"{number} is not divisible by two")


def main():  # Start of the code
    num = int(input("Enter a whole number between 20 and 100: "))
    valid(num)


def valid(num):
    while num < 20 or num > 100:  # While loop to verify correct number
        print("That is not a valid value")
        num = int(input("Enter a whole number between 20 and 100: "))

    if 20 <= num <= 100:  # If statement to get all the divisible functions running
        divisible_two(num)
        divisible_three(num)
        divisible_five(num)
    return num


main()  # Calling first function of the code
