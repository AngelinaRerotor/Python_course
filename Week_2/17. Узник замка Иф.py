A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
if A <= D and (B <= E or C <= E):
    print('YES')
elif B <= D and (C <= E or A <= E):
    print('YES')
elif C <= D and (A <= E or B <= E):
    print('YES')
else:
    print('NO')
