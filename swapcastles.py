CELL_NOT_EXIST = 0
CELL_EMPTY = 1
CELL_CASTLE_W = 2
CELL_CASTLE_B = 3

'''
All the squares on the board:
    |00|01|02|03|04|
    |10|11|12|13|14|
    |20|21|22|23|24|
    |30|31|32|33|34|
Of these squares; 01, 02, 03, 11, 12, and 13 are (by default) non-existent cells.
'''

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
    display()
    index, moves = 0, ""
    while board != complete_board:
        index, moves = search()
    print("The moves are")
    for i in range(0, len(moves), 4):
        print("\t", moves[i:i+2], "to", moves[i+2:i+4])
    print("Solved in", index, "turns.")
    display()


def breadth_first_searcher():
    setter = set()
    bfs_list = [[0, ""]]
    def search():
        if len(bfs_list) == 0: return [-1, ""]
        
        index, moves = bfs_list.pop(0)
        reset_board()
        play_moves_in_board(moves)
        if settable(board) in setter: return [index, moves]
        if board == complete_board:
            return [index, moves]
        bfs_list.extend([index+1, moves] for moves in get_all_moves(moves))
        setter.add(settable(board))
        return [index, moves]

    return search


def settable(board):
    s = ""
    for cell_row in board:
        for cell in cell_row:
            s += str(cell)
    return s


def reset_board():
    global board
    board = [[CELL_CASTLE_W, CELL_NOT_EXIST, CELL_NOT_EXIST, CELL_NOT_EXIST, CELL_CASTLE_B],
             [CELL_CASTLE_W, CELL_NOT_EXIST, CELL_NOT_EXIST, CELL_NOT_EXIST, CELL_CASTLE_B],
             [CELL_CASTLE_W, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_CASTLE_B],
             [CELL_CASTLE_W, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_CASTLE_B]]


def play_moves_in_board(moves: str):
    moveset = [moves[i:i+4] for i in range(0, len(moves), 4)]
    for move in moveset:
        source = int(move[0]), int(move[1])
        destination = int(move[2]), int(move[3])
        board[source[0]][source[1]], board[destination[0]][destination[1]] = \
                board[destination[0]][destination[1]], board[source[0]][source[1]]


def get_all_moves(moves: str):
    next_moves = []

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == CELL_EMPTY or board[i][j] == CELL_NOT_EXIST:
                continue
            next_moves.extend(get_next_if_move(i, j, moves))

    return next_moves


def get_next_if_move(i: int, j: int, moves: str):
    nexts = []
    
    for next_i in range(i-1, -1, -1):
        if board[next_i][j] != CELL_EMPTY:
            break
        nexts.append(moves + f"{i}{j}{next_i}{j}")

    for next_i in range(i+1, len(board)):
        if board[next_i][j] != CELL_EMPTY:
            break
        nexts.append(moves + f"{i}{j}{next_i}{j}")

    for next_j in range(j-1, -1, -1):
        if board[i][next_j] != CELL_EMPTY:
            break
        nexts.append(moves + f"{i}{j}{i}{next_j}")

    for next_j in range(j+1, len(board[i])):
        if board[i][next_j] != CELL_EMPTY:
            break
        nexts.append(moves + f"{i}{j}{i}{next_j}")

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
