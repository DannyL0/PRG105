LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5
info_dict = {}


def main():

    file = open("customer-file", "r+")
    file.close()

    while True:
        menu()
        choice = int(input("Enter your selection: "))
        if choice == LOOK_UP:
            read()
        elif choice == ADD:
            create()
        elif choice == CHANGE:
            update()
        elif choice == DELETE:
            delete()
        elif choice == QUIT:
            quit()
        else:
            print("Incorrect")
            break


def menu():
    print("\n1. Look up an email by name")
    print("2. Add a new entry")
    print("3. Change a person's email")
    print("4. Delete an entry")
    print("5. Quit")


def read():
    name = input("Enter a name: ")
    if name in info_dict:
        print(f"Email: {info_dict[name]}")
    else:
        print("Person not found")


def create():
    name = input("Enter a name: ")
    address = input("Enter a email address: ")
    info_dict[name] = address
    print(f"Successfully added {info_dict[name]} to the info_dict")


def delete():
    name = input("Enter a name: ")
    if name in info_dict:
        del info_dict[name]
        print("Person was successfully deleted from the info_dict")
    else:
        print("Person is not in the info_dict")


def update():
    name = input("Enter a name: ")
    if name in info_dict:
        address = input("Enter the new email of the person\n")
        info_dict[name] = address
        print("Successfully updated email")
    else:
        print("That name is not in the database")


if __name__ == '__main__':
    main()
