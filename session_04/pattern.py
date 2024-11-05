# 5. Print the following pattern:

# *
# * *
# * * *
# * * * *
# * * * * *

def print_pattern(n):
    for i in range(1, n + 1):
        # Print '*' i times, separated by a space
        print('* ' * i)

# Number of rows for the pattern
rows = 5
print_pattern(rows)