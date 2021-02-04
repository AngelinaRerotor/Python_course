a = [i for i in input().split()]
result = []
for i in range(len(a)-1):
    if i % 2 == 0:
        result.append(a[i+1])
        result.append(a[i])
if len(a) % 2 != 0:
    result.append(a[-1])
print(' '.join(result))
