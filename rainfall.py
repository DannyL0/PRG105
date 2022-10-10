filename = 'rainfall-totals.txt'
data = []
total_rainfall = 0  # running total
month_data = []
counter = 0
file = open(filename, 'r')

for line in file:
    month_data = (line.strip()).split(' ')
    rainfall = month_data[1]  # the [1] pulls the numbers from the list and leaves the month names alone

    rainfall = rainfall.replace('.', '')  # replace '.' in rainfall with ''

    if rainfall.isdigit():
        counter += 1

        month_data[1] = float(month_data[1])  # convert monthData[1] to float to avoid error

        total_rainfall += month_data[1]

        data.append(month_data)

    else:

        print(f"Bad numeric data found for entry: {month_data[0]} {month_data[1]}")  # monthData[0] is month name and monthData[1] is the number

file.close()

avg_rainfall = total_rainfall / counter  # calculate the avg rainfall, counter helps since bad values are not added to the total number of months

print(f"\n{counter} good values were found.")
print(f"Total Rainfall: {total_rainfall: .1f}.")  # print the total and average rainfall
print(f"Average Rainfall: {avg_rainfall: .1f}.")
