def evenorodd_v1(n):
    return n%2 == 0
def evenorodd_v2(n):
    return (n&1)==0
n = int(input("Enter any number: "))
print(evenorodd_v1(n))
print(evenorodd_v2(n))