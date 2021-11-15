from functools import reduce

class Matrix:

    def __init__(self, **kwargs):
        if 'filename' in kwargs:
            self.read_from_file(kwargs['filename'])
        elif 'list' in kwargs:
            self.read_as_list(kwargs['list'])

    def read_as_list(self, matrix_list):
        if len(matrix_list) == 0:
            self._matrix = []
            self._columns = 0
            self._rows = 0
            return

        columns_count_0 = len(matrix_list[0])
        if not all(len(row) == columns_count_0 for row in matrix_list):
            raise ValueError('Got incorrect matrix')

        self._matrix = matrix_list
        self._rows = len(self._matrix)
        self._columns = columns_count_0

    def read_from_file(self, filename):
        matrix_list = []
        with open(filename, 'r') as f:
            matrix_rows = f.readlines()
        for row in matrix_rows:
            if row.endswith('\n'):
                row_1 = row[:-1]
                numbers = [float(x) for x in row_1.split(' ')]
                matrix_list.append(numbers)
            else:
                matrix_list.append([float(x) for x in row.split(' ')])
        self.read_as_list(matrix_list)

    def __str__(self):
        s = '---------MATRIX---------\n'
        s += '\n'.join(str(row) for row in self._matrix)
        s += '\n'
        s += f'colums = {self.shape[0]}\nrows = {self.shape[1]}'
        s += '\n------------------------\n'
        return s

    def write_to_file(self, filename):
        with open(filename, 'w') as f:
            for row in self._matrix:
                f.write(' '.join([str(num) for num in row]) + '\n')

    @property
    def traspose(self):
        zipped_rows = zip(*self._matrix)
        transpose_matrix = [list(row) for row in zipped_rows]
        return transpose_matrix

    @property
    def shape(self):
        return self._columns, self._rows

    def __add__(self, other):  # +
        if self._rows == other._rows and self._columns == other._columns:
            result = []
            for i in range(self._rows):
                row = []
                for j in range(self._columns):
                    row.append(self._matrix[i][j] + other._matrix[i][j])
                result.append(row)
            return result
        else:
            print("Matrix shapes not equal")
            return

    def __mul__(self, other):  # *
        if self._rows == other._rows and self._columns == other._columns:
            result = []
            for i in range(self._rows):
                row = []
                for j in range(self._columns):
                    row.append(self._matrix[i][j] * other._matrix[i][j])
                result.append(row)
            return result
        else:
            print("Matrix shapes not equal")
            return

    def __matmul__(self, other):  # @
        if self._columns == other._rows:
            result = []
            for i in range(self._rows):
                row = []
                # iterate through columns of Y
                for j in range(other._columns):
                    # iterate through rows of Y
                    sum = 0
                    for k in range(other._rows):
                        sum += self._matrix[i][k] * other._matrix[k][j]
                    row.append(sum)
                result.append(row)
            return result
        else:
            print("First matrix columns not equal to second matrix rows")
            return

    @property
    def trace(self):
        if self._rows != self._columns:
            print("No trace")
            return
        trace = 0
        for i in range(self._rows):
            trace += self._matrix[i][i]
        return trace

    @property
    def determinant(self):
        if self._rows != self._columns:
            print("No determinant")
            return
        posdet = 0
        for i in range(self._rows):
            posdet += reduce((lambda x, y: x * y), [self._matrix[(i + j) % self._rows][j] for j in range(self._rows)])
        negdet = 0
        for i in range(self._rows):
            negdet += reduce((lambda x, y: x * y), [self._matrix[(self._rows - i - j) % self._rows][j] for j in range(self._rows)])
        return posdet - negdet


matrix_1 = Matrix(filename='matrix1.txt')
matrix_2 = Matrix(filename='matrix2.txt')
matris_sum = matrix_1 + matrix_2
matrix_mul = matrix_1 * matrix_2
matrix_matmul = matrix_1 @ matrix_2
print(matrix_1)
print(f"Matrix transpose: {matrix_1.traspose}")
print(f"Matrix shape: {matrix_1.shape}")
print(f"Matrix trace: {matrix_1.trace}")
print(f"Matrix determinant: {matrix_1.determinant}")
print("Matrix sum")
print(matris_sum)
print("Matrix mul")
print(matrix_mul)
print("Matrix matmul")
print(matrix_matmul)
matrix_3 = Matrix(list=matrix_matmul)
matrix_3.write_to_file('matrix3.txt')