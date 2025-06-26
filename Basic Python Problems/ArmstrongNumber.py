def armstrong(n):
    s = 0
    t = n
    pow = len(str(n))
    while n != 0:
        d = n % 10
        s = s + d ** pow
        n = n // 10
    return s == t
for i in range(1, 1000+1):
    if armstrong(i):
        print(f"{i} is an Armstrong number")
    else:
        print(f"{i} is not an Armstrong number")