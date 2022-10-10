print("This program accepts a phrase and returns the acronym.")

user_phrase = input("Please enter a phrase to convert: ")

list_creation = user_phrase.split()  # This is to separate each word into a list ex. ['word1', 'word2', 'word3'] etc..

store_acronym = ''  # Used to store the first letters from the for loop

for line in list_creation:
    store_acronym = store_acronym + line[0]

upper_acronym = store_acronym.upper()  # Need this otherwise if the user does not input a capital it will not look correct

print(upper_acronym)
