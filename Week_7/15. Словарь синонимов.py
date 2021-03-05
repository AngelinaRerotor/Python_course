n = int(input())
myDict1 = {}
myDict2 = {}
while n != 0:
    i = list(map(str, input().split()))
    myDict1[i[0]] = i[1]
    myDict2[i[1]] = i[0]
    n = n - 1

s = str(input())
if s in myDict1:
    print(myDict1[s])
elif s in myDict2:
    print(myDict2[s])
