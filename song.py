# For this assignment, you will be providing the logic (plan) for the following program:
#
# Use loops to make all the lyrics of "99 bottles of beer on the wall"  print on the screen. Adjust the last two verses for correct grammar:

bottles = 99

while bottles > 2:
    print(str(bottles) + " bottles of beer on the wall")
    print(str(bottles) + " bottles of beer")
    print("take one down, pass it around")
    print(str(bottles - 1) + " bottles of beer on she wall\n")
    bottles = bottles - 1
while bottles == 2:
    print(str(bottles) + " bottles of beer on the wall")
    print(str(bottles) + " bottles of beer")
    print("take one down, pass it around")
    print(str(bottles - 1) + " bottle of beer on the wall\n")
    bottles = bottles - 1
while bottles == 1:
    print(str(bottles) + " bottle of beer on the wall")
    print(str(bottles) + " bottle of beer")
    print("take one down, pass it around")
    print(str(bottles - 1) + " bottles of beer on the wall\n")
    bottles = bottles - 1
