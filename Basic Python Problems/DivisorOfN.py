
def divisors(n):
    L = []
    for i in range(1,n+1):
        if n%i == 0:
            L.append(i)
    return L

n = int(input("Enter n value: "))
print(f"n = {n} and divisors : {divisors(n)} ")