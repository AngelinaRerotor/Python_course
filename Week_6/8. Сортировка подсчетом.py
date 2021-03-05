def CountSort(list):
    grades = [0] * 101
    for i in list:
        grades[i] += 1
    for j in range(101):
        print((str(j) + ' ') * grades[j], end='')


myList = list(map(int, input().split()))
CountSort(myList)
