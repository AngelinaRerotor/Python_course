from sys import stdin


class Matrix:
    def __init__(self, my_list):
        self.my_list = [line[:] for line in my_list]

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, line)) for line in self.my_list])

    def size(self):
        return len(self.my_list), len(self.my_list[0])

    def __add__(self, other):
        ri, rj = range(len(self.my_list)), range(len(self.my_list[0]))
        return Matrix([[self.my_list[i][j] + other.my_list[i][j] for j in rj]
                       for i in ri])

    def __mul__(self, skal):
        ri, rj = range(len(self.my_list)), range(len(self.my_list[0]))
        return Matrix([[self.my_list[i][j] * skal for j in rj] for i in ri])

    __rmul__ = __mul__


exec(stdin.read())
