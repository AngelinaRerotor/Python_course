N = int(input())
hour = N // 60
min = N % 60
print(hour % 24, min % 60)
