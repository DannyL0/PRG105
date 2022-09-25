pi = 3.14


def validation(choice):
    if choice == 1 or choice == 2 or choice == 3 or choice == 4 or choice == 5:
        return True
    else:
        return False


def area_rectangle(width, height):
    return width * height


def area_triangle(base, height):
    return 0.5 * base * height


def area_square(side):
    return side * side


def area_circle(radius):
    return pi * (radius * radius)


flag = 0

while flag != 5:
    print("This program will find the area of a shape for you.")
    print("1. Rectangle\n2. Triangle\n3. Square\n4. Circle\n5. Quit")
    choice = int(input("Please enter the number of your selection: "))
    if validation(choice):
        if choice == 1:
            width = int(input("Enter the width of the rectangle in cm: "))
            height = int(input("Enter the height of the rectangle in cm: "))
            area = area_rectangle(width, height)
            print(f"The area of the rectangle is {area:.2f} square cm")
        elif choice == 2:
            base = int(input("Enter base of triangle in cm: "))
            height = int(input("Enter height of the triangle in cm: "))
            area = area_triangle(base, height)
            print(f"The area of the triangle is {area:.2f} square cm")
        elif choice == 3:
            side = int(input("Please enter the length of one side of the square in cm: "))
            area = area_square(side)
            print(f"The area of the square is {area:.2f} square cm")
        elif choice == 4:
            radius = int(input("Please enter the length of the radius of the circle: "))
            area = area_circle(radius)
            print(f"The area of the circle is {area:.2f} square cm")
        else:
            if choice == 5:
                print("Goodbye")
                flag = 5
        print()
    else:
        print("That is not a valid number")
        print()
        continue
