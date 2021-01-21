n = int(input())
print('+___ ' * n)
for j in range(n):
    print('|', j + 1,  ' /', sep='', end=' ')
print()
print('|__\ ' * n)
print('|    ' * n)
