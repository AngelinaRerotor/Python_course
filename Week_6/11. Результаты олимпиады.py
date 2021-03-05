n = int(input())
data = []
i = 0
while i < n:
    newData = list(map(str, input().split()))
    newData[1] = int(newData[1])
    data.append(tuple(newData))
    i += 1

data.sort(key=lambda x: (-x[1]))
for i in data:
    print(i[0])
