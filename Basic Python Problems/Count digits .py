def count_v1(n):
    return len(str(n))

def count_v2(n):
    c = 0
    while n!=0:
        c = c+1
        n = n//10
    return c
def count_v3(n):
    if n==0:
        return 0
    else:
        return 1+count_v3(n//10)

n = int(input("Enter n value: "))
print(f"number = {n} and count of digits = {count_v1(n)}")
print(f"number = {n} and count of digits = {count_v2(n)}")
print(f"number = {n} and count of digits = {count_v3(n)}")