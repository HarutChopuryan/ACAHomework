#### Transpose and reshape the matrix ####

class Matrix:
    def __init__(self, matrix):
        self._matrix = matrix

    def traspose(self):
        zipped_rows = zip(*self._matrix)
        transpose_matrix = [list(row) for row in zipped_rows]
        return transpose_matrix

    def reshape(self, r, c):
        if r * c != len(self._matrix) * len(self._matrix[0]):
            print("Enter correct rows and columns")
            return
        array_of_matrix = []
        reshaped_matrix = []
        for row in self._matrix:
            for item in row:
                array_of_matrix.append(item)
        for row in range(r):
            reshaped_matrix.append(array_of_matrix[row * c: (row + 1) * c])
        return reshaped_matrix


matrix_1 = Matrix([[1, 3], [5, 9], [4, 5]])
print(matrix_1.traspose())
print(matrix_1.reshape(2, 3))

#### Battleship ####

class Battleship:

    def __init__(self, board):
        if not board:
            self._board = 0
        self._count = 0
        self._board = board
        self._row = len(board)
        self._col = len(board[0])

    def countBattleships(self):
        for i in range(self._row):
            for j in range(self._col):
                if self._board[i][j] == ".":
                    continue
                if i > 0 and self._board[i - 1][j] == "X":
                    continue
                if j > 0 and self._board[i][j - 1] == "X":
                    continue
                self._count += 1

        return self._count

board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
battle = Battleship(board)
print(battle.countBattleships())

#### Find All Numbers Disappeared in an Array ####

def find_disappeared_numbers_in_array(nums):
    length_of_nums = len(nums)
    all_numbers = set(range(1, length_of_nums + 1))

    for num in nums:
        if num in all_numbers:
            all_numbers.remove(num)

    return list(all_numbers)

nums = [1, 1, 1]
print(find_disappeared_numbers_in_array(nums))

#### Keyboard row ####

def findWords(words):
    keyboard_rows = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
    single_row_words = []
    for word in words:
        for row in keyboard_rows:
            if all(letter in row for letter in word.lower()):
                single_row_words.append(word)
    return single_row_words

words = ["Hello","Alaska","Dad","Peace"]
print(findWords(words))