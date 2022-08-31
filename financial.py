# For this assignment, you will be providing the logic (plan) for the following program:
# You are writing a program to determine if a student is eligible for financial aid for the next semester. To qualify, the student must either be a new student or a current student with a GPA of 2.0 or higher.  Additionally, the student may not have a criminal record for drugs, must enroll in a minimum of six credit hours of classes, and must have a gross yearly income of less than $50,000.  You will gather information from the student, and you will let them know if they are eligible for financial aid or not.
#   Hint: this is a bunch of different types of if statements, not an if-elif-else chain
#   Hint: Assume the student qualifies and test for disqualification.

returning_student = input("Are you a returning student? True or False? ")
current_gpa = float(input("Please enter your GPA: "))

criminal_record = input("Do you have a criminal record for drugs? True or False? ")
credit_hours = int(input("Enter the amount of credit hours you will be enrolling in: "))
salary = int(input("Enter your gross salary income: "))

if returning_student == "True" or current_gpa >= 2.0:
    if criminal_record == "True":
        print("Not eligible for financial aid.")
    elif credit_hours < 6:
        print("Not eligible for financial aid.")
    elif salary > 50000:
        print("Not eligible for financial aid.")
    else:
        print("\nYou are eligible for financial aid.")
else:
    print("\nYou do not meet the base requirements.")
