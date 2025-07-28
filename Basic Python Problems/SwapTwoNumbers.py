# Program to swap two numbers with and without using a temporary variable
def swap_withTemp(a, b):
    """
    Swaps two integers using temp variable.
    """
    print("\n[Swap using temp variable]")
    print(f"Before swap: a = {a}, b = {b}")
    temp=a  # Value of a gets stored in temp
    a=b     # a takes the value of b
    b=temp  # b takes the original value of a that had been stored in temp
    print(f"After swap: a = {a}, b = {b}")


def swap_arithmetic(a, b):
    """
    Swaps two integers using arithmetic operations (no temp variable).
    """
    print("\n[Arithmetic Swap]")
    print(f"Before swap: a = {a}, b = {b}")
    a = a + b  # Step 1: a now becomes the sum of both
    b = a - b  # Step 2: b becomes the original value of a
    a = a - b  # Step 3: a becomes the original value of b
    print(f"After swap: a = {a}, b = {b}")


def swap_xor(a, b):
    """
    Swaps two integers using XOR bitwise operations (no temp variable).
    Uses properties:
    - a ^ a = 0
    - a ^ 0 = a
    - XOR is reversible
    """
    print("\n[XOR Swap]")
    print(f"Before swap: a = {a}, b = {b}")
    a = a ^ b  # Step 1: a = a ^ b (info of both a and b now in a)
    b = a ^ b  # Step 2: b = (a ^ b) ^ b = a  (because b ^ b = 0, and a ^ 0 = a)
    a = a ^ b  # Step 3: a = (a ^ b) ^ a = b  (original b value is restored)
    print(f"After swap: a = {a}, b = {b}")


# Input from user
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

# Perform swaps using all three methods
swap_withTemp(a, b)
swap_arithmetic(a, b)
swap_xor(a, b)
