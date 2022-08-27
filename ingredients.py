#  Smoked salmon & spinach gratin
#  https://www.bbcgoodfood.com/recipes/swedish-smoked-salmon-spinach-gratin

# Ingredient variables
spinach = 1.2  # kg
butter = 15  # grams
salmon = 6  # fillets
cream = 300  # ml
servings = 6

#  Original ingredient list
print("Original ingredient list\n")
print(f"Spinach = {spinach}kg")
print(f"Butter = {butter}g")
print(f"Salmon = {salmon} fillets, skin removed (about 140g each)")
print(f"Cream = {cream}ml")
print(f"Serving size = {servings} servings\n \n")

# input
number_of_servings = float(input("Please enter the amount of servings you'd like: "))

# calculations
spinach_ratio = (spinach * number_of_servings) / servings
butter_ratio = (butter * number_of_servings) / servings
salmon_ratio = (salmon * number_of_servings) / servings
cream_ratio = (cream * number_of_servings) / servings

# output
print("\nSmoked Salmon & Spinach Gratin\n")
print(f"Spinach = {spinach_ratio:.1f}kg")
print(f"Butter = {butter_ratio:.1f}g")
print(f"Salmon = {salmon_ratio:.1f} fillets, skin removed (about 140g each)")
print(f"Cream = {cream_ratio:.1f}ml")
print(f"Serving  = {number_of_servings:.1f} servings")



