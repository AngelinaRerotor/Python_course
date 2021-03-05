a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*sorted(list(set(a) & set(b))))
