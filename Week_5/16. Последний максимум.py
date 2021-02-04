a = list(map(int, input().split()))
max = a[1]
j = 0
for i in range(len(a)):
    if a[i] >= max:
        max = a[i]
        j = i
print(max, j)
