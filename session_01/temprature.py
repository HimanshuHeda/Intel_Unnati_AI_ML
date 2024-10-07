# Problem2: Temperature Converter
# Write a Python program that:
# 1. Takes the temperature in Celsius as input from the user (string input).
# 2. Converts the temperature from Celsius to Fahrenheit using the formula:
#   F = 9/5 *c + 32
# 3. Prints the converted temperature in Fahrenheit.



celsius = input("Enter the temperature in Celsius: ")

celsius = float(celsius)
fahrenheit = 9/5 * celsius + 32

print("The temperature in Fahrenheit is:", fahrenheit)