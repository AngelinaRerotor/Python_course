A = int(input())
B = int(input())
C = int(input())
if (A + B) % 2 == 1 or (B + C) % 2 == 1 or (A + C) % 2 == 1:
    print('YES')
else:
    print('NO')
