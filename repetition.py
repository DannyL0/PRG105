current_age = int(input("How old are you: "))
retire = int(input("What age will you retire: "))
income = int(input("Enter your yearly income: "))
percentage = int(input("What percent of your income do you save: "))
savings = int(input("How much money do you have in savings: "))
print("This projection assumes 3% raise each year and a 6% yearly return on investment.")

print(f'{"Year":<9} {"Income":^20} {"Savings Contribution":^25} {"Total Savings":^25}')
for year in range(retire-current_age):
    contribution = (income * (percentage/100))
    savings = (savings * 1.06)
    savings += contribution
    print(f'{year+1:>2}   {" ":^10} {income:,.0f} {" ":^21} {contribution:,.0f} {" ":^15} {savings:,.0f}')
    income = (income * 1.03)
