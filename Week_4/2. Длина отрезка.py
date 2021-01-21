def distance(a, b, c, d):
    d = ((c - a)**2 + (d - b)**2)**0.5
    return d


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
print(distance(x1, y1, x2, y2))
