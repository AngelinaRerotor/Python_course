n = int(input())
all = list()
vse = set()
tolko = set()
for i in range(n):
    p = set()
    m = int(input())
    for j in range(m):
        p.add(input())
    all.append(p)
vse = all[0]
tolko = all[0]
for i in range(1, len(all)):
    vse = vse | all[i]
    tolko = tolko & all[i]
print(len(tolko))
for i in range(len(tolko)):
    print(tolko.pop())
print(len(vse))
for i in range(len(vse)):
    print(vse.pop())
