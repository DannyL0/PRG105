class Person:
    def __init__(self, name, age, address, phone):
        self.__name = name
        self.__age = age
        self.__address = address
        self.__phone = phone

    # getters

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone

    # mutators

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_address(self, address):
        self.__address = address

    def set_phone(self, phone):
        self.__phone = phone

    def __str__(self):
        return f"{self.__name}, age {self.__age}\n{self.__address}\n{self.__phone}"


person1 = Person("Danny", "22", "1234 St", "123-456-7894\n")
person2 = Person("Bob", "45", "754 Drive", "485-164-9765\n")
person3 = Person("Sam", "15", "117 Ct", "986-589-1245\n")

print(person1)
print(person2)
print(person3)
