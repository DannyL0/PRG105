days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

steps = []

for day in range(len(days)):
    number_steps = int(input(f"Please enter the number of steps taken on {days[day]}: "))  # Needs to be int or else the sum command won't work
    steps.append(number_steps)
print(f"\nYou walked a total of {sum(steps):,.0f} steps during the week")
print(f"That was an average of {(sum(steps))/ (len(days)) :,.0f} steps a day!")

for maximum in range(len(steps)):
    if steps[maximum] == max(steps):
        print(f"The maximum steps you took were {steps[maximum]} on \n---{days[maximum]}")
for minimum in range(len(steps)):
    if steps[minimum] == min(steps):
        print(f"The minimum steps you took were {steps[minimum]} on: \n---{days[minimum]}")
