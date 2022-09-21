
def main():

    print("Select one of the menu options below to find out more") # Menu
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
    print("You chose Monte Cristo")

def ruben():
    print("You chose Ruben")


def sub():
    print("You chose Submarine")


def grilled_cheese():
    print("You chose Grilled Cheese")


def gyro():
    print("You chose Gyro")


main()
