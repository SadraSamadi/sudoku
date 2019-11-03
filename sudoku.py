from copy import deepcopy


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
            for i in range(9):
                state = self.next(puzzle, i + 1)
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
                if a != 0:
                    row[a - 1] += 1
                if b != 0:
                    col[b - 1] += 1
                if c != 0:
                    reg[c - 1] += 1
            for j in range(9):
                if row[j] > 1 or col[j] > 1 or reg[j] > 1:
                    return True
        return False

    def solved(self, puzzle):
        for i in range(9):
            for j in range(9):
                if puzzle[i][j] == 0:
                    return False
        return True

    def next(self, puzzle, number):
        state = deepcopy(puzzle)
        for i in range(9):
            for j in range(9):
                if state[i][j] == 0:
                    state[i][j] = number
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
