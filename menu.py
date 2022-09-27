def main():

    print("Select one of the menu options below to find out more")  # Menu
    print("A.  Monte Cristo\nB.  Ruben\nC.  Submarine\nD.  Grilled Cheese\nE.  Gyro")

    choice = str(input("Please enter the letter of your choice: ")).upper()

    if choice == "A":
        monte_cristo()
    elif choice == "B":
        ruben()
    elif choice == "C":
        sub()
    elif choice == "D":
        grilled_cheese()
    elif choice == "E":
        gyro()


def monte_cristo():
    print("Egg dipped ham and cheese sandwich\nPan or deep fried")


def ruben():
    print("Grilled sandwich of corned beef and swiss cheese served on rye bread")


def sub():
    print("Sandwich consisting of a long roll split down the middle with your choice of meats and veggies")


def grilled_cheese():
    print("Grilled cheesed\naccompanied with a side of fries")


def gyro():
    print("Gyro served on a handmade pita with gyros sauce, tomatoes and onions")


main()
