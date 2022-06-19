# Домашнеее задание, урок-10, задание-1
import copy

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        s = ''
        for i in range(len(self.matrix)):
            s = s + '\t'.join(map(str,self.matrix[i])) + '\n'
        return s

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix):
            return None
        res = copy.deepcopy(self.matrix)
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                res[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return Matrix(res)

    @property
    def test(self, other=[[1,2,4],[3,4,5],[5,6,6]]):
        res = self.matrix.copy()
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
               res[i][j] = self.matrix[i][j] + other[i][j]
        print(res)

l1 = [[1,2,4],[3,4,5],[5,6,6]]
l2 = [[11,21,41],[31,41,51],[51,61,61]]
m = Matrix(l1)
s = Matrix(l2)
print(m)
print(s)
z = m + s
print('z - сумма матриц; ', type(z))
print(z)

