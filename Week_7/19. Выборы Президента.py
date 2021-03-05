file = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
candidates = {}
votes = 0
for name in file:
    candidates[name.strip()] = candidates.get(name.strip(), 0) + 1
    votes += 1
candList = sorted(candidates.items())
candList.sort(key=lambda x: x[1], reverse=True)

if int(candList[0][1]) > votes * 0.5:
    print(candList[0][0], file=outFile)
else:
    print(candList[0][0], candList[1][0], sep='\n', file=outFile)
