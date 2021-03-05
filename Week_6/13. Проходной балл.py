infile = open('input.txt', 'r', encoding='utf8')
outfile = open('output.txt', 'w', encoding='utf8')
Rate = []
n = int(infile.readline())
for i in infile:
    x = i.split()
    if int(x[-1]) >= 40 and int(x[-2]) >= 40 and int(x[-3]) >= 40:
        Rate.append(int(x[-1]) + int(x[-2]) + int(x[-3]))
Rate.sort(reverse=True)
l = Rate.index(min(Rate[:n]))
if len(Rate) <= n:
    print(0, file=outfile)
elif Rate.count(max(Rate)) > n:
    print(1, file=outfile)
elif Rate[n:].count(min(Rate[:n])) == 0:
    print(min(Rate[:n]), file=outfile)
else:
    print(min(Rate[:l]), file=outfile)
infile.close()
outfile.close()
