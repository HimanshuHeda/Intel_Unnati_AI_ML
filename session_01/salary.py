# Problem1: Basic Salary Calculation
# You are working on a payroll system where you need to calculate the gross salary of an
# employee based on the following:
#  Basic Salary (input by the user, as a string, e.g., &quot;50000&quot;)
#  House Rent Allowance (HRA): 20% of Basic Salary
#  Dearness Allowance (DA): 10% of Basic Salary
#  Gross Salary is calculated as:
# Gross Salary=Basic Salary+HRA+DA\text{Gross Salary} = \text{Basic Salary} + \text{HRA} +
# \text{DA}Gross Salary=Basic Salary+HRA+DA
# Write a Python script that:
# 1. Takes the Basic Salary as a string input from the user.
# 2. Converts it to an appropriate numeric type.
# 3. Performs the necessary arithmetic




basic_salary_str = input("Enter the Basic Salary: ")

basic_salary = float(basic_salary_str)
hra = basic_salary * 0.20
da = basic_salary * 0.10

gross_salary = basic_salary + hra + da

print("Basic Salary: ", basic_salary)
print("House Rent Allowance (HRA): ", hra)
print("Dearness Allowance (DA): ", da)
print("Gross Salary: ", gross_salary)