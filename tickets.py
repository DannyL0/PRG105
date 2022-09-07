# Variables
student_cost = 5.00
veteran_cost = 7.00
sponsor_cost = 2.00
retiree_cost = 6.00
general_cost = 10.00


# output
print("PLAY PRICES PER TICKET\n1. Student $5.00\n2. Veteran $7.00\n3. Show sponsor $2.00\n4. Retiree $6.00\n5. General Public $10.00")

# input
category_choice = float(input("\nEnter the number of the category you fit for purchasing tickets: "))
total_tickets = float(input("How many tickets would you like to buy? "))

student_ticket = student_cost * total_tickets
veteran_ticket = veteran_cost * total_tickets
sponsor_ticket = sponsor_cost * total_tickets
retiree_ticket = retiree_cost * total_tickets
general_ticket = general_cost * total_tickets

if category_choice == 1:
    print("You chose student\n")
    print(f"Cost before any discounts were applied: ${student_cost * total_tickets}")
    if 4 <= total_tickets <= 8:
        print(f"Your cost after all discounts were applied: ${student_ticket * .90:.2f}")
        print(f"Your prices is ${(student_ticket * .90)/total_tickets:.2f} per ticket")
    elif total_tickets <= 15:
        print(f"Your cost after all discounts were applied: ${student_ticket * .85:.2f}")
        print(f"Your prices is ${(student_ticket * .85)/total_tickets:.2f} per ticket")
    else:
        print(f"Your cost after all discounts were applied: ${student_ticket * .80:.2f}")
        print(f"Your prices is ${(student_ticket * .80)/total_tickets:.2f} per ticket")

elif category_choice == 2:
    print("You chose Veteran\n")
    print(f"Cost before any discounts were applied: ${veteran_cost * total_tickets}")
    if 4 <= total_tickets <= 8:
        print(f"Your cost after all discounts were applied: ${veteran_ticket * .90:.2f}")
        print(f"Your prices is ${(veteran_ticket * .90)/total_tickets:.2f} per ticket")
    elif total_tickets <= 15:
        print(f"Your cost after all discounts were applied: ${veteran_ticket * .85:.2f}")
        print(f"Your prices is ${(veteran_ticket * .85)/total_tickets:.2f} per ticket")
    else:
        print(f"Your cost after all discounts were applied: ${veteran_ticket * .80:.2f}")
        print(f"Your prices is ${(veteran_ticket * .80)/total_tickets:.2f} per ticket")

elif category_choice == 3:
    print("You chose Show Sponsor\n")
    print(f"Cost before any discounts were applied: ${sponsor_cost * total_tickets}")
    if 4 <= total_tickets <= 8:
        print(f"Your cost after all discounts were applied: ${sponsor_ticket * .90:.2f}")
        print(f"Your prices is ${(sponsor_ticket * .90)/total_tickets:.2f} per ticket")
    elif total_tickets <= 15:
        print(f"Your cost after all discounts were applied: ${sponsor_ticket * .85:.2f}")
        print(f"Your prices is ${(sponsor_ticket * .85)/total_tickets:.2f} per ticket")
    else:
        print(f"Your cost after all discounts were applied: ${sponsor_ticket * .80:.2f}")
        print(f"Your prices is ${(sponsor_ticket * .80)/total_tickets:.2f} per ticket")

elif category_choice == 4:
    print("You chose Retiree\n")
    print(f"Cost before any discounts were applied: ${retiree_cost * total_tickets}")
    if 4 <= total_tickets <= 8:
        print(f"Your cost after all discounts were applied: ${retiree_ticket * .90:.2f}")
        print(f"Your prices is ${(retiree_ticket * .90)/total_tickets:.2f} per ticket")
    elif total_tickets <= 15:
        print(f"Your cost after all discounts were applied: ${retiree_ticket * .85:.2f}")
        print(f"Your prices is ${(retiree_ticket * .85)/total_tickets:.2f} per ticket")
    else:
        print(f"Your cost after all discounts were applied: ${retiree_ticket * .80:.2f}")
        print(f"Your prices is ${(retiree_ticket * .80)/total_tickets:.2f} per ticket")

elif category_choice == 5:
    print("You chose General Public\n")
    print(f"Cost before any discounts were applied: ${general_cost * total_tickets}")
    if 4 <= total_tickets <= 8:
        print(f"Your cost after all discounts were applied: ${general_ticket * .90:.2f}")
        print(f"Your prices is ${(general_ticket * .90)/total_tickets:.2f} per ticket")
    elif total_tickets <= 15:
        print(f"Your cost after all discounts were applied: ${general_ticket * .85:.2f}")
        print(f"Your prices is ${(general_ticket * .85)/total_tickets:.2f} per ticket")
    else:
        print(f"Your cost after all discounts were applied: ${general_ticket * .80:.2f}")
        print(f"Your prices is ${(general_ticket * .80)/total_tickets:.2f} per ticket")


else:
    print("You did not enter a correct number")
