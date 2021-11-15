class Matrix:
    def __init__(self, *args, **kwargs):
        """
        kwargs['filename']
        kwargs['list']
        """
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
        # # file = open(filename, "r")
        # # lines = file.read().getlines()
        # # with open(filename, 'r') as f:
        # #     matrix_rows = f.readlines()
        # # for row in matrix_rows:
        # #     if
        # #     matrix_list.append(row)
        # with open(filename, 'r') as f:
        #     for row in f:
        #         matrix_list.append(row)
        # # matrix_list = list(map(lambda s: list(map(float, s[:-1].split(' '))), matrix_list))
        # self.read_as_list(matrix_list)
        # list_of = map(lambda s: list(map(float, s[:-1].split(' '))), matrix_list)
        # matrix_list = list(list_of)
        with open(filename, 'r') as f:
            matrix_rows = f.readlines()
        for row in matrix_rows:
            if row.endswith('\n'):
                row_1 = row[:-1]
                matrix_list.append(row_1)
            else:
                matrix_list.append(row)
        self.read_as_list(matrix_list)

    def __str__(self):
        s = f'colums = {self.shape[0]}\nrows = {self.shape[1]}'
        return s

    def write_to_file(self, filename):
        with open(filename, 'w') as f:
            line = f.readline()
            f.write(line)

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
            for i in self._rows:
                for j in self._columns:
                    result[i][j] = self._matrix[i][j] + other._matrix[i][j]
            return result
        else:
            print("Matrix shapes not equal")
            return

    def __mul__(self, other):  # *
        if self._rows == other._rows and self._columns == other._columns:
            result = []
            for i in self._rows:
                for j in self._columns:
                    result[i][j] = self._matrix[i][j] * other._matrix[i][j]
            return result
        else:
            print("Matrix shapes not equal")
            return

    def __matmul__(self, other):  # @
        if self._columns == other._rows:
            result = []
            for i in range(self._rows):
                # iterate through columns of Y
                for j in range(other._columns):
                    # iterate through rows of Y
                    for k in range(other._rows):
                        result[i][j] += self._matrix[i][k] * other[k][j]
            return result
        else:
            print("First matrix columns not equal to second matrix rows")
            return


matrix_1 = Matrix(filename='matrix.txt')
print(matrix_1.shape)
