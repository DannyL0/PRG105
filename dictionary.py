dictionary = {'uno': 'one', 'dos': 'two', 'tres': 'three', 'quatro': 'four',
              'cinco': 'five', 'seis': 'six', 'siete': 'seven', 'ocho': 'eight', 'nueve': 'nine', 'diez': 'ten', }
counter = 0
spanish = dictionary.keys()

for line in dictionary:
    user_answer = input(f"What is the equivalent of {line}: ")
    if dictionary[line] == user_answer:
        counter += 1
        print("Correct")
    else:
        print(f"Incorrect. The correct answer is {dictionary[line]}")

print(f"\nYour final score is {counter}/10")
if counter >= 9:
    print("A")
elif counter >= 8:
    print("B")
elif counter >= 7:
    print("C")
elif counter >= 6:
    print("D")
else:
    print("F")
