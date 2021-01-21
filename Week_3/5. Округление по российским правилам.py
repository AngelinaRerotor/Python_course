x = float(input())
x1 = x % 1
if x1 >= 0.5:
    x = int(x) + 1
else:
    x = int(x)
print(x)
