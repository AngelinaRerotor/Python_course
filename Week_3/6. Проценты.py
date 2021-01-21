P = float(input())
X = int(input())
Y = int(input())
s = X * 100 + Y
sumY = s + (s * P) / 100
n1 = int(sumY / 100)
n2 = int(sumY % 100)
print(n1, '{0:.0f}'.format(n2))
