s = input()
a = s.find('f')
if a != -1:
    s1 = s[a+1:]
    a1 = s1.find('f')
    if a1 != -1:
        print(a + 1 + a1)
    else:
        print(-1)
else:
    print(-2)
