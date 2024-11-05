# 4. Reverse a number using a for loop.

def reverse_number(number):
    # Initialize the reversed number to 0
    reversed_num = 0
    # Make a copy of the original number to manipulate
    original_number = number

    # Use a for loop to reverse the number
    for digit in str(original_number):
        # Update the reversed number
        reversed_num = reversed_num * 10 + int(digit)

    return reversed_num

# Example usage
num = 12345
reversed_num = reverse_number(num)
print(f"The reverse of {num} is {reversed_num}.")

