file = open("tale_of_two_cities.txt")

dictionary = dict()

for line in file:

    line = line.strip()
    words = line.split()

    for word in words:

        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1

print("Words seen only once:\n")
for key in list(dictionary.keys()):
    if dictionary[key] == 1:
        print(key)
