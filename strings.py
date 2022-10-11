try:
    file1 = open("accounts.txt")
    file2 = open("over90.txt")

    accounts = []
    over90 = []

    for i in file1:  # this reads data from accounts.txt
        line = i.strip().split(",")
        accounts.append(line)
    for i in file2:  # this reads data from over90.txt
        line = i.strip()
        over90.append(line)
    print("These are the accounts that are currently overdue:\n")
    for line_over90 in over90:  # this compares first column of accounts.txt and matches it to over90
        for line_accounts in accounts:
            if line_accounts[0] == line_over90:
                print(",".join(line_accounts))
except FileNotFoundError:
    print("This file does not exist.")
