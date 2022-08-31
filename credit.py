# For this assignment, you will be providing the logic (plan) for the following program:
# Ask your user for their credit score. Tell them if they have Bad, Fair, Good, or Excellent credit:
#
# Directions:
# Create Pseudocode to plan your project. Use the following format:
#
# Data:
# BAD =300–629
# FAIR = 630-689
# GOOD = 690-719
# EXCELLENT = 720-850

user_credit_score = int(input("Enter your credit score: "))

if user_credit_score >= 720:
    print(f"With a credit score of {user_credit_score}\nYou have excellent credit.")
elif user_credit_score >= 690:
    print(f"With a credit score of {user_credit_score}\nYou have good credit.")
elif user_credit_score >= 630:
    print(f"With a credit score of {user_credit_score}\nYou have fair credit.")
else:
    print(f"With a credit score of {user_credit_score}\nYou have bad credit.")
