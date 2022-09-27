file = open("address_book.txt", "a")

people = int(input("How many people do you want to add to the file? "))

for i in range(people):
    name = input("What is the name of the person? ")
    phone_number = input("What is their phone number? ")
    email = input("What is their email address? ")
    file.write(name)
    file.write(", ")
    file.write(phone_number)
    file.write(", ")
    file.write(email)
    file.write("\n")
