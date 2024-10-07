# Problem3: Simple Interest Calculator
# Write a Python program that calculates the Simple Interest based on the formula:
#       SI = P * R * T / 100
# Where:
#  P is the Principal amount (input as a string by the user)
#  R is the Rate of interest (input as a string by the user)
#  T is the Time period in years (input as a string by the user)

# Your program should:
# 1. Take the Principal, Rate of interest, and Time as inputs from the user (as strings).
# 2. Typecast these inputs to appropriate numeric types.
# 3. Calculate the Simple Interest.
# 4. Print the result.

P = float(input("Enter the Principal : "))
R = float(input("Enter the Rate : "))
T = float(input("Enter the Time : "))

SI = P * R * T / 100

print("The Simple Interest is : ", SI)