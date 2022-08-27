#  variables

net_income = float(input("Please enter your net monthly income: "))
monthly_housing = float(input("Enter how much you spend monthly on housing: "))
monthly_transportation = float(input("Enter how much you spend monthly on transportation: "))
monthly_phone_bill = float(input("Enter how much you spend monthly on your phone bill: "))
monthly_utilities = float(input("Enter how much you spend monthly on utilities: "))
monthly_clothing = float(input("Enter how much you spend monthly on clothing: "))
total_bills = float((monthly_clothing + monthly_utilities + monthly_transportation + monthly_housing + monthly_phone_bill))
#  calculations
housing_ratio = (monthly_housing / net_income)
transportation_ratio = (monthly_transportation / net_income)
phone_bill_ratio = (monthly_phone_bill / net_income)
utilities_ratio = (monthly_utilities / net_income)
clothing_ratio = (monthly_clothing / net_income)

#  display
print(f"\nHousing takes up {housing_ratio:.2%} of your monthly income")
print(f"Transportation takes up {transportation_ratio:.2%} of your monthly income")
print(f"Your phone bill takes up {phone_bill_ratio:.2%} of your monthly income")
print(f"Utilities takes up {utilities_ratio:.2%} of your monthly income")
print(f"Clothing takes up {clothing_ratio:.2%} of your monthly income\n")
print(f"You have ${net_income - total_bills:,} left from your income after paying your monthly expenses")

