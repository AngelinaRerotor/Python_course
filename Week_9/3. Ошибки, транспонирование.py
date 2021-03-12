from sys import stdin


class MatrixError(BaseException):
    def __init__(self, m1, m2):
        self.matrix1 = m1
        self.matrix2 = m2


class Matrix:
    @staticmethod
    def transposed(obj):
        return Matrix([[obj.my_list[j][i] for j in range(len(obj.my_list))]
                       for i in range(len(obj.my_list[0]))])

    def __init__(self, my_list):
        self.my_list = [line[:] for line in my_list]

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, line)) for line in self.my_list])

    def size(self):
        return len(self.my_list), len(self.my_list[0])

    def __add__(self, other):
        if len(self.my_list) == len(other.my_list):
            ri, rj = range(len(self.my_list)), range(len(self.my_list[0]))
            return Matrix([[self.my_list[i][j] + other.my_list[i][j]
                            for j in rj] for i in ri])
        else:
            raise MatrixError(self, other)

    def __mul__(self, skal):
        ri, rj = range(len(self.my_list)), range(len(self.my_list[0]))
        return Matrix([[self.my_list[i][j] * skal for j in rj] for i in ri])

    def transpose(self):
        self.my_list = [[self.my_list[j][i] for j in range(len(self.my_list))]
                        for i in range(len(self.my_list[0]))]
        return Matrix(self.my_list)

    __rmul__ = __mul__


exec(stdin.read())
