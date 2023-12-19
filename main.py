# import copy



def evaluate(board):
    # return 1 if X's win
    # return -1 if O's win
    # return 0 if neither

    # Определяем выигрышные комбинации
    lines = [
        [(0, 0), (0, 1), (0, 2)],
        #xxx
        #---
        #---
        [(1, 0), (1, 1), (1, 2)],
        #---
        #xxx
        #---
        [(2, 0), (2, 1), (2, 2)],
        #---
        #---
        #xxx        
        [(0, 0), (1, 0), (2, 0)],
        #x--
        #x--
        #x--
        [(0, 1), (1, 1), (2, 1)],
        #-x-
        #-x-
        #-x-
        [(0, 2), (1, 2), (2, 2)],
        #--x
        #--x
        #--x
        [(0, 0), (1, 1), (2, 2)],
        #x--
        #-x-
        #--x
        [(0, 2), (1, 1), (2, 0)]
        #--x
        #-x-
        #x--
        ]

    for line in lines:
        symbols = [board[i][j] for i, j in line]
        if symbols == ['X', 'X', 'X']:
            return 1
        elif symbols == ['O', 'O', 'O']:
            return -1
    return 0


def count_on_board(item: str, board: list):
    size = len(board)

    count = 0

    for i in range(size):
        for j in range(size):
            if board[i][j] == item:
                count += 1

    return count


def whos_step(board: list):
    count_X = count_on_board('X', board)
    count_O = count_on_board('O', board)

    if count_O == count_X:
        return 'X'
    return 'O'


def minimax(board, depth, is_maximizing):
    global best_score
    global best_move
    # board is play ground
    # depth - how many steps available
    # is_maximizing -

    result = evaluate(board)

    if result != 0:
        return result

    if depth == 0:
        return 0

    if is_maximizing:
        best_score = -float('inf')

    we_play_as = whos_step(board)

    if we_play_as == 'X':
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth - 1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
                    return best_score
                else:
                    best_score = float('inf')
    else:
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth - 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)

    return best_score


def find_best_move(board):
    global best_score
    global best_move
    best_score = -float('inf')
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                depth = 5 - count_on_board('X', board)
                score = minimax(board, depth, False)
                # Устанавливаем глубину анализа
                board[i][j] = ' '

                # # ---
                # if score == 1:
                #     # we win
                #     return (i, j)
                # # ---

                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move


# Пример использования
# board = [
#     [' ', ' ', ' '],
#     [' ', ' ', ' '],
#     [' ', ' ', ' ']
#     ]
# board = [
#     ['X', 'O', 'X'],
#     ['O', 'X', 'O'],
#     [' ', ' ', ' ']
#     ]
board = [
    ['X', 'O', 'X'],
    ['O', ' ', ' '],
    [' ', ' ', ' ']
    ]

print("Считаем, что ходим за крестики")

print("Текущее поле:")
print("  0 1 2")
print(f"0 {board[0][0]} {board[0][1]} {board[0][2]}")
print(f"1 {board[1][0]} {board[1][1]} {board[1][2]}")
print(f"2 {board[2][0]} {board[2][1]} {board[2][2]}")
best_score = 0
best_move = find_best_move(board)
print(f"The best move is {best_move}")
