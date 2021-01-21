N = int(input())
d1 = N // 10**3
d2 = N % 10**3 // 10**2
d3 = N % 10**3 % 10**2 // 10**1
d4 = N % 100**3 % 10**2 % 10**1
if d4 == d1 and d3 == d2:
    print(1)
else:
    print(10)
