s = input()
a = s.find('f')
b = s.rfind('f')
if a != -1 and b != -1:
    if a == b:
        print(a)
    else:
        print(a, b)
elif a == -1 and b != -1:
    print(b)
elif a == -1 and b == -1:
    print('')
