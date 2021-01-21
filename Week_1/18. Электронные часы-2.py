N = int(input())
hour = N // 3600 % 24
min1 = (N % 3600) // 60 // 10
min2 = (N % 3600) // 60 % 10
sec1 = (N % 3600) % 60 // 10
sec2 = (N % 3600) % 60 % 10
print(hour, str(min1)+str(min2), str(sec1)+str(sec2), sep=':')
