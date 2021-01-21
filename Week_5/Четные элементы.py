a = list(map(int, input().split()))

for i in map(int, a):
    if i % 2 != 1:
        print(i, end=' ')
