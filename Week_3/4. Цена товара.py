x = float(input())
x1 = x % 1
x2 = int(x - x1)
x1 *= 100
print(x2, '{0:.0f}'.format(x1))
