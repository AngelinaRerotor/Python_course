from sys import stdin


class Matrix:
    def __init__(self, my_list):
        self.my_list = [line[:] for line in my_list]

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, line)) for line in self.my_list])

    def size(self):
        return len(self.my_list), len(self.my_list[0])


exec(stdin.read())
