"""
    Starting Out with Python by Tony Gaddis, fifth edition
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free (green checkmark upper right)
    Submit your completed file
"""

# TODO 11.1 Introduction to Inheritance
print("=" * 10, "Section 11.1 inheritance", "=" * 10)


# You are going to create a Dwelling class based on the
# Automobile sample from the chapter

# 1) Create the class Dwelling, the __init__ method should accept number_of_rooms, square_feet, floors
class Dwelling:

    def __init__(self, rooms, size, floors):
        self.number_of_rooms = rooms
        self.square_feet = size
        self.floors = floors

    # 2) Add mutators for all of the data attributes (number_of_rooms, square_feet, floors)

    def set_rooms(self, rooms):
        self.number_of_rooms = rooms

    def set_size(self, size):
        self.square_feet = size

    def set_floors(self, floors):
        self.floors = floors

    # 3) Add accessors for all of the data attributes

    def get_rooms(self):
        return self.number_of_rooms

    def get_size(self):
        return self.square_feet

    def get_floors(self):
        return self.floors


# 4) Create the class SingleFamilyHome as a sub-class of Dwelling
# The __init__ method should accept number_of_rooms, square_feet, floors, garage_type, yard_size
# -- Call the __init__ of superclass Dwelling and pass the required arguments, remember to include self
# -- Initialize the garage_type and yard_size attributes
class SingleFamilyHome(Dwelling):

    def __init__(self, rooms, size, floors, garage, yard):
        super().__init__(rooms, size, floors)
        self.garage_type = garage
        self.yard_size = yard

    # 5) Create the mutator and accessor methods for the garage_type and yard_size attributes
    def set_garage_type(self, garage):
        self.garage_type = garage

    def set_yard_size(self, yard):
        self.yard_size = yard

    def get_garage_type(self):
        return self.garage_type

    def get_yard_type(self):
        return self.yard_size


# Demonstrate the SingleFamilyHome class, no need to import because you are in the same file
# 6) Create a main function.
# 7) In main, create an object from the Single_family_home class with the following information:
#            6 rooms, 1200 square feet, 1 floor, single car garage, .25 acres
def main():
    home_obj = SingleFamilyHome(6, 1200, 1, 'Single Car Garage', .25)
    # 8) Display the data using the accessor methods
    print(f"The number of rooms: {home_obj.get_rooms()}")
    print(f"The square footage of the home: {home_obj.get_size()}")
    print(f"The number of floors: {home_obj.get_floors()}")
    print(f"The type of garage: {home_obj.get_garage_type()} ")
    print(f"This home is on {home_obj.get_yard_type()} acres of land")


# 9) Call the main function
main()

# TODO 11.2 Polymorphism
print("=" * 10, "Section 11.2 polymorphism", "=" * 10)


# 1) Type in the mammal class from program 11-9, lines 1 - 22
class Mammal:
    def __init__(self, species):
        self.__species = species

    def show_species(self):
        print('I am a', self.__species)

    def make_sound(self):
        print('Grrrrr')


# 2) Create a Mouse class as a sub-class of the mammal class following the Dog example
class Mouse(Mammal):
    def __init__(self):
        Mammal.__init__(self, 'Mouse')

    def make_sound(self):
        print('Squeek!')


# 3) Create a Sheep class as a sub-class of the mammal class following the Cat Example
class Sheep(Mammal):
    def __init__(self):
        Mammal.__init__(self, 'Sheep')

    def make_sound(self):
        print('Baa')


# 4) Follow the example in program 11-10 (no need to import, use main2 instead of main
#    because there is already a main on this page) use the Mouse and Sheep class that you created

def main2():
    mammal = Mammal('regular animal')
    mouse = Mouse()
    sheep = Sheep()
    print('Here are some animals and')
    print('the sounds they make.')
    print('--------------------------')
    show_mammal_info(mammal)
    print()
    show_mammal_info(mouse)
    print()
    show_mammal_info(sheep)


def show_mammal_info(creature):
    creature.show_species()
    creature.make_sound()


if __name__ == '__main__':
    main2()
