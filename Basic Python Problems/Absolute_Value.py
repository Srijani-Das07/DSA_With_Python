def abs_v1(n):
    if n<0:
        return -n
    else:
        return n
def abs_v2(n):
    return abs(n)
n  = int(input("Enter n value: "))
print(f"Original value = {n} and Absoluter value  = {abs_v1(n)}")
print(f"Original value = {n} and Absoluter value  = {abs_v2(n)}")