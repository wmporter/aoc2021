def make_board(rows):
    board = []
    for row in rows:
        board.append(list(map(int, row.strip().split())))
    return board

def mark_board(board, number):
    for i in range(5):
        for j in range(5):
            if board[i][j] == number:
                board[i][j] = -1
                return True
    return False

def mark_all_boards(boards, number):
    for b in boards:
        marked = mark_board(b, number)
        if marked:
            if check_board(b):
                return sum_board(b)
    return -1

def check_board(board):
    winning = [-1] * 5
    if winning in board:
        return True
    for col in range(5):
        if winning == get_col(board, col):
            return True
    return False

def get_col(board, col):
    return [row[col] for row in board]

def sum_board(board):
    sum = 0
    for row in board:
        for num in row:
            if num != -1:
                sum += num
    return sum

boards = []
with open("input") as f:
    input = f.readlines()

numbers = map(int, input.pop(0).strip().split(","))

while '\n' in input:
    input.remove('\n')

while input:
    boards.append(make_board(input[:5]))
    input = input[5:]

for number in numbers:
    t = mark_all_boards(boards, number)
    if t > -1:
        print("total =", number * t)
        break
