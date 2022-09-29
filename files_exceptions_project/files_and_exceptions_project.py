
print("This program will total and average numbers in your data file.")
filename = input("Enter the name of your data file: ")

try:
    file = open(filename, 'r')  # opening file
    total = 0  # running total
    count = 0
    invalid = 0  # keeps up with the mistakes which get taken out of count and avg later

    for line in file.readlines():
        line = line.rstrip("\n")
        count += 1

        try:
            i = float(line)
            total += i
            print(i)

        except ValueError:  # specific error if the number was incorrect
            invalid += 1
            print(f"Line {count} with a value of {line}\nwas invalid.")

    print(f"\nTotal: {total:,.2f}")  # Printing output for total, count and average
    print(f"Number of entries: {count - invalid}")
    print(f"Average: {(total / (count - invalid)):,.2f}")

except IOError:
    print(f"Unable to access the file: {filename}")  # this error runs instead of everything nested in the try: if the filename is wrong

file = open("sales_error-1.txt", "r")
total = 0
count = 0
