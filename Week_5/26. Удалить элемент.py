a = list(map(int, input().split()))
k = int(input())
del a[k]
print(' '.join(map(str, a)))
