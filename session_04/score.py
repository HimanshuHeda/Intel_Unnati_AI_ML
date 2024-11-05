# 1. Find the grade: If a score is above 90, it gets an A; if it's between 80 and 90, it gets a B; if it's
# between 70 and 80, it gets a C; if it's between 40 and 70, it gets a D; and if it's below 40, it fails.

def get_grade(score):
    if score > 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 40:
        return "D"
    else:
        return "F"

# Example usage:
score = float(input("Enter the score: "))
grade = get_grade(score)
print(f"The grade is: {grade}")