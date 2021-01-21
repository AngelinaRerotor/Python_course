def power(a, n):
    if a > 0:
        return a * (a**(n - 1))


a = float(input())
n = int(input())
print(power(a, n))
