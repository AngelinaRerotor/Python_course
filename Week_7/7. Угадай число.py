n = int(input())
mySet = set(range(1, n + 1))
s = input()
while s != 'HELP':
    ans = input()
    if ans == 'YES':
        mySet &= set(map(int, s.split()))
    elif ans == 'NO':
        mySet -= set(map(int, s.split()))
    s = input()
mySet = list(mySet)
mySet.sort()
print(*mySet)
