import pickle

LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5


def main():

    try:
        file = open("customer-file", "rb")
        info_dict = pickle.load(file)
    except(FileNotFoundError, IOError):
        print("File not found")
        info_dict = {}

    choice = 0

    while choice != QUIT:
        choice = menu()

        if choice == LOOK_UP:
            read(info_dict)
        elif choice == ADD:
            create(info_dict)
        elif choice == CHANGE:
            update(info_dict)
        elif choice == DELETE:
            delete(info_dict)
        elif choice == QUIT:
            saving(info_dict)


def menu():
    print("\n1. Look up an email by name")
    print("2. Add a new entry")
    print("3. Change a person's email")
    print("4. Delete an entry")
    print("5. Quit")
    choice = int(input("Enter your selection: "))
    while choice < 1 or choice > 5:
        choice = int(input("*Your choice was invalid*\nTry again\nEnter your selection: "))
    return choice


def read(info_dict):
    name = input("Enter a name: ")
    print(info_dict.get(name, "Person not found"))


def create(info_dict):
    name = input("Enter a name: ")
    address = input("Enter a email address: ")
    if name not in info_dict:
        info_dict[name] = address
    else:
        print("That entry already exists")


def delete(info_dict):
    name = input("Enter a name: ")
    if name in info_dict:
        del info_dict[name]
        print("Person was successfully deleted from the info_dict")
    else:
        print("Person is not in the info_dict")


def update(info_dict):
    name = input("Enter a name: ")
    if name in info_dict:
        address = input("Enter the new email of the person\n")
        info_dict[name] = address
        print("Successfully updated email")
    else:
        print("That name is not in the database")


def saving(info_dict):
    print("The database has been successfully updated")
    save_file = open('customer-file', 'wb')
    pickle.dump(info_dict, save_file)
    save_file.close()


if __name__ == '__main__':
    main()
