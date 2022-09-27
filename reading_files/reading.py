file = open("sales_totals.txt", "r")
total = 0
count = 0

for line in file:
    line = line.rstrip("\n")
    count += 1
    i = float(line)  # converting to float
    total += i  # finding total
    print(i)
print(f"Total: {total:,.2f}")
print(f"Number of entries: {count}")
print(f"Average: {(total/count):,.2f}")
