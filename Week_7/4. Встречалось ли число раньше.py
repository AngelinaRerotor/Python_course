a = list(map(int, input().split()))
mySet = set()
for i in a:
    if i in mySet:
        print("YES")
    else:
        mySet.add(i)
        print("NO")
