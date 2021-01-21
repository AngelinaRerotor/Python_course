s = input()
print(s[0:1], s[1:].replace('', '*', len(s)-1), sep='')
