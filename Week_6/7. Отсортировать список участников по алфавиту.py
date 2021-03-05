in_file = open('input.txt', 'r', encoding='utf8')
out_file = open('output.txt', 'w', encoding='utf8')
children_list = []
for i in in_file:
    children_list.append(i.split())
children_list.sort()
for now in children_list:
    now.pop(2)
    print(*now, file=out_file)
in_file.close()
out_file.close()
