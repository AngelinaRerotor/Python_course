a = list(map(int, input().split()))

s = 0
for i in map(int, a):
    if i > 0:
        s += 1
print(s)
