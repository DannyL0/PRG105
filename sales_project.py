total_sales = 0.0
entire_week = "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"
daily_sales = 0.0
# input

for week in entire_week:
    daily_sales = float(input(f"Enter the sales for {week}: "))
    total_sales += daily_sales

# output
average = total_sales / 7
print(f"Your total sales for the entire week is ${total_sales:,.2f}")
print(f"Your average amount of sales per day is ${average:,.2f}")
