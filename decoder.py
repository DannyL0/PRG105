alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
         'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g',
         'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
         'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ', ',', '.', '!']

code = ['R', 'j', 'v', 'm', 'F', 'x', '_', 'V', '?', 'f', 'k', '2', ';', '3', '&', '4', '>', '5', '6', '7',
        '8', '9', '|', ',', "'", '.', '!', 'A', '^', ':', "a" 'C', '$', 'D', 'p' 'E', 'F', '1', 'G', '%', 'I',
        '*', 'o', 'n', '0', "b", '~', 'B', 'q', '/', '}', '`', '{', 'v', '@', 'W', 'S', ']',
        'Z', "g", '#', '+', 'h', '[', 'z', ')', '-', '<', '(', 'L']

decryption = []

print("This program will decode a coded text file.")

filename = input("What is the name of the file to decode? ")

try:
    file = open(filename, "r")
    data = file.readlines()

    for letter in data:
        decryption.append(alpha[code.index(letter.strip())])

    file.close()

    print(''.join(decryption))


except NameError:
    print("This is an invalid filename")
