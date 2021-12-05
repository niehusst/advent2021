from functools import reduce

# pt 1

boards = []
nums = []

with open('input.txt', 'r') as f:
    nums = list(map(int, f.readline().split(',')))
    
    line = f.readline()
    while line:
        if line.strip():
            # not empty
            board = []
            while line and line.strip():
                board.append(list(map(lambda x: int(x), filter(lambda x: x.strip() != '', line.split(' ')))))
                line = f.readline()
            boards.append(board)

        line = f.readline()

def allSame(arr):
    return reduce(lambda x,y: 'x' if x == y == 'x' else '', arr) == 'x'

def didWin(board):
    dim = len(board)
    for i in range(dim):
        cond = allSame(board[i]) or allSame([board[j][i] for j in range(dim)])
        if cond:
            return True
    return False

def mark(val, board):
    for i in range(len(board)):
        if val in board[i]:
            board[i][board[i].index(val)] = 'x'
            return

def calcScore(board, bingo):
    dim = len(board)
    s = 0
    for r in range(dim):
        for c in range(dim):
            if board[r][c] != 'x':
                s += board[r][c]
    return s * bingo

def partOne():
    for bingo in nums:
        for board in boards:
            mark(bingo, board)
            if didWin(board):
                print(calcScore(board, bingo))
                return

#partOne()

# pt 2

def partTwo():
    tb = len(boards)
    won = 0
    for bingo in nums:
        i = 0
        rm = []
        while i < len(boards):
            mark(bingo, boards[i])
            if didWin(boards[i]):
                won += 1
                rm.append(i)
                if won == tb:
                    print(calcScore(boards[i], bingo))
                    return
            i += 1
        for ind in sorted(rm)[::-1]:
            del boards[ind]

partTwo()
