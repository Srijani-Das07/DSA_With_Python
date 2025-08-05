# Program to calculate factorial of a number using recursion

# Factorial definition:
# n! = n × (n−1) × (n−2) × ... × 1
# For example: 5! = 5 × 4 × 3 × 2 × 1 = 120

def factorial_recursive(n):
    if n == 0 or n == 1:  # Base case
        return 1
    return n * factorial_recursive(n - 1)  # Recursive step

def factorial_iterative(n):
    factorial=1
    for i in range(1,n+1):  # Loop from 1 to n
        factorial *= i      # Multiply each number to compute factorial
    return factorial

# Input from user
num = int(input("Enter a number: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    # Output results
    print(f"Factorial of {num} (recursive) is: {factorial_recursive(num)}")
    print(f"Factorial of {num} (iterative) is: {factorial_iterative(num)}")

