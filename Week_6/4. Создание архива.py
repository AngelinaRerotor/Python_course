myTupl = tuple(map(int, input().split()))
s, n = myTupl
data = []
while n != 0:
    i = int(input())
    data.append(i)
    n = n - 1
data_sort = sorted(data)
save_data = []
for i in data_sort:
    saved = sum(save_data)
    saved = saved + i
    if i == s:
        save_data.append(i)
        break
    if saved <= s:
        save_data.append(i)
print(len(save_data))
