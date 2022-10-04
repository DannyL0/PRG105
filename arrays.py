alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
         'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g',
         'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
         'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ', ',', '.', '!']

code = ['R', 'j', 'v', 'm', 'F', 'x', '_', 'V', '?', 'f', 'k', '2', ';', '3', '&', '4', '>', '5', '6', '7',
        '8', '9', '|', ',', "'", '.', '!', 'A', '^', ':', "a" 'C', '$', 'D', 'p' 'E', 'F', '1', 'G', '%', 'I',
        '*', 'o', 'n', '0', "b", '~', 'B', 'q', '/', '}', '`', '{', 'v', '@', 'W', 'S', ']',
        'Z', "g", '#', '+', 'h', '[', 'z', ')', '-', '<', '(', 'L']

encryption = []

phrase = input("Enter a phrase to encode:")

for position in phrase:
    encryption.append(code[alpha.index(position)])

print(encryption)

f = open("encryption.txt", "w")
for character in encryption:
    f.write(character + "\n")
f.close()
