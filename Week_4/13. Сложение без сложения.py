def rsum(a, b):
    if b == 0:
        return a
    return rsum(a + 1, b - 1)


a = int(input())
b = int(input())
print(rsum(a, b))
