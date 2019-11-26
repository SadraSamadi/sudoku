class Sudoku:

    def __init__(self, puzzle):
        self.puzzle = puzzle

    def solve(self):
        stack = [self.puzzle]
        while stack:
            puzzle = stack.pop()
            if self.conflict(puzzle):
                continue
            if self.solved(puzzle):
                self.puzzle = puzzle
                return True
            for i in range(1, 10):
                state = self.next(puzzle, i)
                stack.append(state)
        return False

    def conflict(self, puzzle):
        for i in range(9):
            row = [0] * 9
            col = [0] * 9
            reg = [0] * 9
            for j in range(9):
                a = puzzle[i][j]
                b = puzzle[j][i]
                c = puzzle[3 * (i // 3) + j // 3][3 * (i % 3) + j % 3]
                if a:
                    row[a - 1] += 1
                if b:
                    col[b - 1] += 1
                if c:
                    reg[c - 1] += 1
            for j in range(9):
                if row[j] > 1 or col[j] > 1 or reg[j] > 1:
                    return True
        return False

    def solved(self, puzzle):
        for i in range(9):
            for j in range(9):
                if not puzzle[i][j]:
                    return False
        return True

    def next(self, puzzle, number):
        state = []
        flag = False
        for i in range(9):
            row = []
            for j in range(9):
                if flag or puzzle[i][j]:
                    row.append(puzzle[i][j])
                else:
                    row.append(number)
                    flag = True
            state.append(row)
        return state

    def print(self):
        for i in range(9):
            print(' ---' * 9)
            for j in range(9):
                c = self.puzzle[i][j]
                s = ' ' if c == 0 else c
                print('| %s ' % s, end='')
            print('|')
        print(' ---' * 9)
