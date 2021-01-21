a1, b1, c1 = int(input()), int(input()), int(input())
a2, b2, c2 = int(input()), int(input()), int(input())
s1 = a1 * b1 * c1
s2 = a2 * b2 * c2
if s1 > s2:
    if (a1 >= a2 and b1 >= b2 and c1 >= c2) or \
        (a1 >= a2 and b1 >= c2 and c1 >= b2) or \
        (a1 >= b2 and b1 >= a2 and c1 >= c2) or \
        (a1 >= b2 and b1 >= c2 and c1 >= a2) or \
        (a1 >= c2 and b1 >= b2 and c1 >= a2) or \
            (a1 >= c2 and b1 >= a2 and c1 >= b2):
        print('The first box is larger than the second one')
    else:
        print('Boxes are incomparable')
if s1 < s2:
    if (a1 <= a2 and b1 <= b2 and c1 <= c2) or \
         (a1 <= a2 and b1 <= c2 and c1 <= b2) or \
         (a1 <= b2 and b1 <= a2 and c1 <= c2) or \
         (a1 <= b2 and b1 <= c2 and c1 <= a2) or \
         (a1 <= c2 and b1 <= b2 and c1 <= a2) or \
            (a1 <= c2 and b1 <= a2 and c1 <= b2):
        print('The first box is smaller than the second one')
    else:
        print('Boxes are incomparable')
if s1 == s2:
    if (a1 == a2 and b1 == b2 and c1 == c2) or \
        (a1 == a2 and b1 == c2 and c1 == b2) or \
        (a1 == b2 and b1 == a2 and c1 == c2) or \
        (a1 == b2 and b1 == c2 and c1 == a2) or \
        (a1 == c2 and b1 == b2 and c1 == a2) or \
            (a1 == c2 and b1 == a2 and c1 == b2):
        print('Boxes are equal')
    else:
        print('Boxes are incomparable')
        