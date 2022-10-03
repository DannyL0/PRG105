def main():
    people = int(input("How many students to do you need to enter grades for? "))

    students = []

    for line in range(people):
        data = [input("Enter the name of the student: "), input("Enter the student's final letter grade: ")]
        students.append(data)
    print(students)

    file = open("grades.txt", "w")
    for position in students:
        list1 = str(position)
        file.write(f"{list1}\n")
    file.close()


main()
