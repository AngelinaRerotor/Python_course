a = list(map(int, input().split()))
j = []
for i in a:
    if i > 0:
        j += [i]
print(min(j))
