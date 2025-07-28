# Program to print Fibonacci sequence up to n terms

# Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, ...
# Each number is the sum of the previous two numbers

def fibonacci(n):
    a, b = 0, 1  # First two terms
    for _ in range(n):
        print(a, end=" ")  # Print the current term
        a, b = b, a + b     # Move to the next term

# Take input from the user
n = int(input("Enter the number of terms: "))

# Call the function
fibonacci(n)
