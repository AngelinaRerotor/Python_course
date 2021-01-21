n = int(input())
d1 = n % 10
d2 = n % 100 // 10
d3 = n // 100
s = (d1 + d2 + d3)
print(s)
