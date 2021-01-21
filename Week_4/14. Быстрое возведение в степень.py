def brr(a, n):
    if n % 2 == 0:
        return ((a**2)**(n / 2))
    if n % 2 != 0:
        return (a * (a**(n - 1)))


a = float(input())
n = int(input())
print(brr(a, n))
