n = int(input())
new = n
new2 = 0
while n != 0:
    if new > new2:
        (new, new2) = (new2, new)
    n = int(input())
    if n > new:
        new = n
print(new)
