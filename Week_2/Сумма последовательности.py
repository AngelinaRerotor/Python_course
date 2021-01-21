now = int(input())
i = 0
while now > 0:
    i += now
    now = int(input())
    if now == 0:
        continue
print(i)
