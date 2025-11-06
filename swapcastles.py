import copy

CELL_NOT_EXIST = 0
CELL_EMPTY = 1
CELL_CASTLE_W = 2
CELL_CASTLE_B = 3

board = [[CELL_CASTLE_W, CELL_NOT_EXIST, CELL_NOT_EXIST, CELL_NOT_EXIST, CELL_CASTLE_B],
         [CELL_CASTLE_W, CELL_NOT_EXIST, CELL_NOT_EXIST, CELL_NOT_EXIST, CELL_CASTLE_B],
         [CELL_CASTLE_W, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_CASTLE_B],
         [CELL_CASTLE_W, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_CASTLE_B]]

complete_board = [[CELL_CASTLE_B, CELL_NOT_EXIST, CELL_NOT_EXIST, CELL_NOT_EXIST, CELL_CASTLE_W],
                  [CELL_CASTLE_B, CELL_NOT_EXIST, CELL_NOT_EXIST, CELL_NOT_EXIST, CELL_CASTLE_W],
                  [CELL_CASTLE_B, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_CASTLE_W],
                  [CELL_CASTLE_B, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_CASTLE_W]]


def main():
    search = breadth_first_searcher()
    iteration = 0
    display()
    while board != complete_board:
        iteration += 1
        search()
    print(iteration)
    display()


setter = set()
def breadth_first_searcher():
    bfs_list = [[0, board]]
    def search():
        global board
        if len(bfs_list) == 0: return
        index, board = bfs_list.pop(0)
        if settable(board) in setter: return
        if board == complete_board:
            print("complete in", index)
            return
        bfs_list.extend([index+1, next_board] for next_board in get_next_boards())
        setter.add(settable(board))

    return search


def settable(board):
    s = ""
    for cell_row in board:
        for cell in cell_row:
            s += str(cell)
    return s


def get_next_boards():
    next_boards = []

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == CELL_EMPTY or board[i][j] == CELL_NOT_EXIST:
                continue
            next_boards.extend(get_next_if_move(i, j))

    return next_boards


def get_next_if_move(i: int, j: int):
    nexts = []
    
    for next_i in range(i-1, -1, -1):
        if board[next_i][j] != CELL_EMPTY:
            break
        next = copy.deepcopy(board)
        next[next_i][j], next[i][j] = next[i][j], CELL_EMPTY

        nexts.append(next)

    for next_i in range(i+1, len(board)):
        if board[next_i][j] != CELL_EMPTY:
            break
        next = copy.deepcopy(board)
        next[next_i][j], next[i][j] = next[i][j], CELL_EMPTY
        nexts.append(next)

    for next_j in range(j-1, -1, -1):
        if board[i][next_j] != CELL_EMPTY:
            break
        next = copy.deepcopy(board)
        next[i][next_j], next[i][j] = next[i][j], CELL_EMPTY
        nexts.append(next)

    for next_j in range(j+1, len(board[i])):
        if board[i][next_j] != CELL_EMPTY:
            break
        next = copy.deepcopy(board)
        next[i][next_j], next[i][j] = next[i][j], CELL_EMPTY
        nexts.append(next)

    return nexts


def display():
    for cell_row in board:
        for cell in cell_row:
            if cell == CELL_EMPTY:
                print(" ", end="")
            elif cell == CELL_NOT_EXIST:
                print("-", end="")
            elif cell == CELL_CASTLE_W:
                print("w", end="")
            elif CELL_CASTLE_B:
                print("b", end="")
        print()


if __name__ == "__main__":
    main()
