# Program to find the greatest among three numbers

# Input: Three numbers from the user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# Compare using if-elif-else statements
if a >= b and a >= c:
    greatest = a
elif b >= a and b >= c:
    greatest = b
else:
    greatest = c

# Output the result
print(f"The greatest number is: {greatest}")
