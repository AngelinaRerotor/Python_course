def perimeter(a, a1, b, b1, c, c1):
    ab = ((b - a)**2 + (b1 - a1)**2)**0.5
    bc = ((c - b)**2 + (c1 - b1)**2)**0.5
    ac = ((c - a)**2 + (c1 - a1)**2)**0.5
    p = ab + bc + ac
    return p


a = float(input())
a1 = float(input())
b = float(input())
b1 = float(input())
c = float(input())
c1 = float(input())
print('{0:.7}'.format(perimeter(a, a1, b, b1, c, c1)))
