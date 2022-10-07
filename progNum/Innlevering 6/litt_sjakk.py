"""Oppgave: Litt sjakk. Innlevering 6"""

def make_board(board_string):
    size = 5
    if len(board_string) != size**2:
        print("String is too big or to small!")
        return 0
    i = 0
    board = []
    for row in range(size):
        row = []
        for _ in range(size):
            if board_string[i]=='.':
                row.append(None)
            else:
                row.append(board_string[i])
            i += 1
        board.append(row)
    return board

def get_piece(board, x, y):
    return board[5-y][x-1]

def get_legal_moves(board, x, y):
    piece = get_piece(board, x, y)
    color = 1 # White
    if piece not in ['p', 'P']:
        print("Only supported for \"Bonde\"")
        return None
    if piece.islower():
        color = -1  # Black
    moves_list = []
    if get_piece(board, x, y+color)is None and 1<= y + color <= 5:
        moves_list.append(f"Move forward to {(x, y+color)}")
    if get_piece(board, x-color, y+color):
        if piece.islower() != get_piece(board, x-color, y+color).islower():
            moves_list.append(f"Attack {get_piece(board, x-color, y+color)} at {(x-color,y+color)}")
    if get_piece(board, x+color, y+color):
        if piece.islower() != get_piece(board, x+color, y+color).islower():
            moves_list.append(f"Attack {get_piece(board, x+color, y+color)} at {(x+color,y+color)}")
    return moves_list


board = make_board('rkn.r.p.....P..PP.PPB.K..')
legal_moves = get_legal_moves(board, 5, 5)
if legal_moves:
    for move in legal_moves:
        print(move)
