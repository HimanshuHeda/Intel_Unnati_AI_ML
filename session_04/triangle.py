# 2. Determine if a triangle is right-angled.

def is_right_angled_triangle(a, b, c):
    # Sort the sides to ensure c is the longest
    sides = sorted([a, b, c])
    
    # Apply the Pythagorean theorem
    return sides[2]**2 == sides[0]**2 + sides[1]**2

# Get user input
try:
    side1 = float(input("Enter the length of side 1: "))
    side2 = float(input("Enter the length of side 2: "))
    side3 = float(input("Enter the length of side 3: "))

    if is_right_angled_triangle(side1, side2, side3):
        print("The triangle is right-angled.")
    else:
        print("The triangle is not right-angled.")

except ValueError:
    print("Please enter valid numerical values for the sides.")