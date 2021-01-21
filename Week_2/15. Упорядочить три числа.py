a, b, c = int(input()), int(input()), int(input())
if a <= b <= c:
    print(a, b, c)
elif c <= b <= a:
    print(c, b, a)
elif a <= c <= b:
    print(a, c, b)
elif c <= a <= b:
    print(c, a, b)
elif b <= a <= c:
    print(b, a, c)
elif b <= c <= a:
    print(b, c, a)
