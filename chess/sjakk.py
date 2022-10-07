"""Complete chess game. Under development."""

# Setup
import PySimpleGUI as sg

board = [
    ["r", "n", "b", "q", "k", "b", "n", "r"],
    ["p"]*8,
    [None]*8,
    [None]*8,
    # [None]*3+["P"]+[None]*4,
    # [None]*8,
    # [None]*8,
    [None]*8,
    [None]*8,
    ["P"]*8,
    ["R", "N", "B", "Q", "K", "B", "N", "R"]
]

board_test = [
    ["k", None, None, None, None, None, None, "R"],
    # ["p"]*8,
    [None]*8,
    # [None]*3+["P"]+[None]*4,
    [None]*8,
    [None, "Q", None, None, None, None, None, None],
    [None]*8,
    [None]*8,
    [None]*8,
    [None, None, None, None, "K", None, None, None]
    # ["P"]*8,
    # ["R", "N", "B", "Q", "K", "B", "N", "R"]
]

pos_to_coor = [
    ["a","b","c","d","e","f","g","h"],
    ["8","7","6","5","4","3","2","1"]
]
pieces = ["p","r", "n", "b", "q", "k"]
king_pos_w = [7, 4]
king_pos_b = [0, 4]

# Functions
def get_piece(loc):
    """Get piece type from location"""
    return board[loc[0]][loc[1]]

def user_input(text, inp=None):
    """Get user input of what piece to move where"""
    if inp is None:
        inp_str = f"{text}: "
        inp = input(inp_str)
    if inp == "c" or inp == "C":
        return None
    j = ord(inp[0])-97
    i = 8-int(inp[1])

    return [i,j]

def move_piece(loc, new_loc):
    """Moves piece to a chosen location"""
    global king_pos_w
    global king_pos_b
    if get_piece(loc) == "K":
        king_pos_w = new_loc
    if get_piece(loc) == "k":
        king_pos_b = new_loc
    piece = board[loc[0]][loc[1]]
    board[new_loc[0]][new_loc[1]] = piece
    board[loc[0]][loc[1]] = None

def print_board(legal_moves = []):
    """Prints the chess board with the pieces"""
    print("   A B C D E F G H")
    for i, row in enumerate(board):
        print(pos_to_coor[1][i] + " \x1B[4m", end="")
        for j, piece in enumerate(row):
            if piece:
                print("|"+piece, end="")
            else:
                if [i, j] in legal_moves:
                    print("|*", end="")
                else:
                    print("| ", end="")
        print("|\x1B[0m", end="")
        print("", pos_to_coor[1][i])
    print("   A B C D E F G H")

def get_color(piece):
    """Return a number based on piece color"""
    if piece:
        if piece.isupper():
            return 1
        return -1
    return None

def get_steps_to_border(loc):
    """Count the steps from the piece the the board border"""
    i, j = loc
    piece_color = get_color(get_piece(loc))
    if piece_color == 1:
        down = 7-i
        up = i
        right = 7-j
        left = j
    else:
        down = i
        up = 7-i
        right = j
        left = 7-j
    return [up, down, left, right]

def get_legal_moves(loc):
    """Get the legal moves of a piece"""
    i = loc[0]
    j = loc[1]
    piece = get_piece(loc)
    if piece is None:
        return []
    piece_color = get_color(piece)
    legal_moves = []
    # ["r", "n", "b", "q", "k", "b", "n", "r"]
    if piece.lower() == "p":
        if get_piece([i-1*piece_color, j]) is None:
            legal_moves.append([i-1*piece_color, j])
            if (piece_color==1 and i == 6) or (piece_color==-1 and i==1):
                legal_moves.append([i-2*piece_color, j])
        moves = [[i-1*piece_color, j-1], [i-1*piece_color, j+1]]

        for move in moves:
            try:
                if get_piece(move) and piece_color == get_color(get_piece(move))*-1:
                    legal_moves.append(move)
            except:
                pass
    if piece.lower() == "r" or piece.lower() == "q":
        rook_moves = []
        up, down, left, right = get_steps_to_border(loc)
        # up
        try:
            i = 1
            move = [loc[0]-i*piece_color, loc[1]]
            while i<=up+1 and get_piece(move) is None:
                rook_moves.append(move)
                i += 1
                move = [loc[0]-i*piece_color, loc[1]]
            if get_color(get_piece(move)) == piece_color*-1:
                rook_moves.append(move)
        except:
            pass
        # down
        try:
            i = 1
            move = [loc[0]+i*piece_color, loc[1]]
            while i<=down+1 and get_piece(move) is None:
                rook_moves.append(move)
                i += 1
                move = [loc[0]+i*piece_color, loc[1]]
            if get_color(get_piece(move)) == piece_color*-1 and move[i]>0:
                rook_moves.append(move)
        except:
            pass
        # right
        try:
            i = 1
            move = [loc[0], loc[1]+i*piece_color]
            while i<=right+1 and get_piece(move) is None:
                rook_moves.append(move)
                i += 1
                move = [loc[0], loc[1]+i*piece_color]
            if get_color(get_piece(move)) == piece_color*-1 and move[1]<=7:
                rook_moves.append(move)
        except:
            pass
        # left
        try:
            i = 1
            move = [loc[0], loc[1]-i*piece_color]
            while i<=left+1 and get_piece(move) is None:
                rook_moves.append(move)
                i += 1
                move = [loc[0], loc[1]-i*piece_color]
            if get_color(get_piece(move)) == piece_color*-1 and move[1]<=7:
                rook_moves.append(move)
        except:
            pass

        for move in rook_moves:
                if move[0]>=0 and move[1]>=0:
                    if get_piece(move) is None or get_color(get_piece(move)) == piece_color*-1:
                        legal_moves.append(move)
    if piece.lower() == "n":
        knight_moves = [
            [i+2, j+1], [i+1, j+2],
            [i-2, j+1], [i-1, j+2],
            [i-2, j-1], [i-1, j-2],
            [i+2, j-1], [i+1, j-2]
        ]
        for move in knight_moves:
            if move[0]>=0 and move[1]>=0:
                try:
                    if get_piece(move) is None or get_color(get_piece(move)) == piece_color*-1:
                        legal_moves.append(move)
                except:
                    pass
    if piece.lower() == "b" or piece.lower() == "q":
        up, down, left, right = get_steps_to_border(loc)
        bishop_moves = []
        # up right
        try:
            i = 1
            move = [loc[0]-i*piece_color, loc[1]+i*piece_color]
            while i<=up+1 and get_piece(move) is None:
                bishop_moves.append(move)
                i += 1
                move = [loc[0]-i*piece_color, loc[1]+i*piece_color]
            if get_color(get_piece(move)) == piece_color*-1:
                bishop_moves.append(move)
        except:
            pass
        # down right
        try:
            i = 1
            move = [loc[0]+i*piece_color, loc[1]+i*piece_color]
            while i<=down+1 and get_piece(move) is None:
                bishop_moves.append(move)
                i += 1
                move = [loc[0]+i*piece_color, loc[1]+i*piece_color]
            if get_color(get_piece(move)) == piece_color*-1 and move[i]>0:
                bishop_moves.append(move)
        except:
            pass
        # up left
        try:
            i = 1
            move = [loc[0]-i*piece_color, loc[1]-i*piece_color]
            while i<=left+1 and get_piece(move) is None:
                bishop_moves.append(move)
                i += 1
                move = [loc[0]-i*piece_color, loc[1]-i*piece_color]
            if get_color(get_piece(move)) == piece_color*-1 and move[1]<=7:
                bishop_moves.append(move)
        except:
            pass
        # down left
        try:
            i = 1
            move = [loc[0]+i*piece_color, loc[1]-i*piece_color]
            while i<=left+1 and get_piece(move) is None:
                bishop_moves.append(move)
                i += 1
                move = [loc[0]+i*piece_color, loc[1]-i*piece_color]
            if get_color(get_piece(move)) == piece_color*-1 and move[1]<=7:
                bishop_moves.append(move)
        except:
            pass
        for move in bishop_moves:
            if move[0]>=0 and move[1]>=0:
                if get_piece(move) is None or get_color(get_piece(move)) == piece_color*-1:
                    legal_moves.append(move)
    if piece.lower() == "k":
        king_moves = [
            [i+1, j+1], [i+1, j], [i+1, j-1],
            [i, j+1], [i, j-1],
            [i-1, j+1], [i-1, j-1], [i-1, j]
        ]
        for move in king_moves:
            if move[0]>=0 and move[1]>=0:
                try:
                    if get_piece(move) is None or get_color(get_piece(move)) == piece_color*-1:
                        legal_moves.append(move)
                except:
                    pass
    return legal_moves

def upgarade_pawn(loc):
    """Upgrade the pawn to a new piece"""
    piece_color = get_color(get_piece(loc[0]))
    print(f"Pawn on {pos_to_coor[0][loc[0][0]]}, {pos_to_coor[1][loc[0][1]]} can be upgraded.")
    new_piece = "0"
    while new_piece not in pieces:
        new_piece = input("What piece do you want? ").lower()
    if piece_color == 1:
        board[loc[0][0]][loc[0][1]] = new_piece.upper()
    else:
        board[loc[0][0]][loc[0][1]] = new_piece.lower()

def check_for_checkmate(color):
    """Check if the player is in check or checkmate"""
    if color == 1:
        oponent_pieces = pieces
        king_pos = king_pos_w
    else:
        oponent_pieces = []
        for piece in pieces:
            oponent_pieces.append(piece.upper())
        king_pos = king_pos_b
    oponent_legal_moves = []
    for i, row in enumerate(board):
        for j, piece in enumerate(row):
            if get_color(piece)==color*-1:
                for move in get_legal_moves([i,j]):
                    oponent_legal_moves.append(move)
    king_legal_moves = get_legal_moves(king_pos)
    check = False
    for move in oponent_legal_moves:
        if move == king_pos:
            check = True
    if check:
        moves_to_pop = []
        for i, move in enumerate(king_legal_moves):
            if move in oponent_legal_moves:
                moves_to_pop.append(move)
        for move in moves_to_pop:
            king_legal_moves.pop(king_legal_moves.index(move))
    print(king_legal_moves)
    if not king_legal_moves and check:
        return True
    return False

def check_for_check(color):
    """Check if the player is in check"""
    if color == 1:
        oponent_pieces = pieces
        king_pos = king_pos_w
    else:
        oponent_pieces = []
        for piece in pieces:
            oponent_pieces.append(piece.upper())
            king_pos = king_pos_b

    for i, row in enumerate(board):
        for j, piece in enumerate(row):
            if piece in oponent_pieces:
                try:
                    if king_pos in get_legal_moves([i, j]):
                        return True
                except:
                    pass
    return False

def print_last_move(loc, new_loc):
    """Print the last move a player did"""
    print("Last move: ", end="")
    print(f"{pos_to_coor[0][loc[1]]}{pos_to_coor[1][loc[0]]}", end="")
    print(" to ", end="")
    print(f"{pos_to_coor[0][new_loc[1]]}{pos_to_coor[1][new_loc[0]]}")

def main():
    """Main loop"""
    color = 1
    print("\nTurn: White (P)")
    while not check_for_checkmate(color):
        where_to_move = None
        while where_to_move is None:
            print_board()
            piece_to_move = user_input("Choose a piece")
            legal_moves = get_legal_moves(piece_to_move)
            print_board(legal_moves)
            where_to_move = user_input("Where to move? (c to cancel move)")
            if where_to_move not in legal_moves:
                print("You can't move there")
                where_to_move = None
        move_piece(piece_to_move, where_to_move)
        if color == 1:
            color = -1
            print("\nTurn: Black (p)")
        else:
            color = 1
            print("\nTurn: White (P)")
        print_last_move(piece_to_move, where_to_move)

def gui_main():
    """Main function for running the game with a GUI"""
    layout = []
    layout.append([sg.Text('Turn: White', key="turn")])
    layout.append([sg.Text('Last move:', key="last_move")])
    for i, row in enumerate(board):
        new_row=[]
        for j, piece in enumerate(row):
            if piece:
                if piece.isupper():
                    new_column = sg.Button(
                        piece, size=(3, 2), button_color = ('black', 'white'), key=f'{i}{j}'
                        )
                else:
                    new_column = sg.Button(
                        piece, size=(3, 2), button_color = ('white', 'black'), key=f'{i}{j}'
                        )
            else:
                new_column = sg.Button(
                    " ", size=(3, 2), button_color = ('white', 'white'), key=f'{i}{j}'
                    )
            new_row.append(new_column)
        layout.append(new_row)
    layout.append([sg.Exit(), sg.Text('', key="check")])
    window = sg.Window("Chess", layout, element_padding=(1,1), default_element_size=(40,40))
    pice_to_move = None
    where_to_move = None
    legal_moves = []
    player = 1
    player_color = {
        1: "White",
        -1: "Black"
    }
    while not check_for_checkmate(player):
        event, _ = window.read()
        if event in (sg.WINDOW_CLOSED, "Exit"):
            break
        for i, row in enumerate(board):
            for j, piece in enumerate(row):
                if event == f'{i}{j}':
                    if pice_to_move is None:
                        pice_to_move = [i, j]
                        legal_moves = get_legal_moves(pice_to_move)
                        for i_, row in enumerate(board):
                            for j_, piece in enumerate(row):
                                try:
                                    if [i_, j_] in legal_moves:
                                        window[f'{i_}{j_}'].update(
                                            button_color=('black', 'yellow'))
                                except:
                                    pass
                    elif [i,j] in legal_moves and get_color(get_piece(pice_to_move))==player:
                        where_to_move = [i,j]
                        piece = get_piece(pice_to_move)
                        move_piece(pice_to_move, where_to_move)
                        if piece.isupper():
                            window[f'{where_to_move[0]}{where_to_move[1]}'].update(f"{piece}", button_color = ('black','white'))
                        else:
                            window[f'{where_to_move[0]}{where_to_move[1]}'].update(f"{piece}", button_color = ('white','black'))
                        window[f'{pice_to_move[0]}{pice_to_move[1]}'].update(" ", button_color = ('black','white'))
                        for m in legal_moves:
                            if m != where_to_move:
                                if get_piece(m) is not None and get_piece(m).islower():
                                    window[f'{m[0]}{m[1]}'].update(button_color = ('white','black'))
                                else:
                                    window[f'{m[0]}{m[1]}'].update(button_color = ('black','white'))
                        
                        try:
                            last_pos_str = "Last move: "+f"{pos_to_coor[0][pice_to_move[1]]}{pos_to_coor[1][pice_to_move[0]]}"+" to "+f"{pos_to_coor[0][where_to_move[1]]}{pos_to_coor[1][where_to_move[0]]}"
                            window['last_move'].update(f'{last_pos_str}')
                            if check_for_check(player*-1):
                                window['check'].update('Youre in check!')
                            else:
                                window['check'].update('')
                            if player == 1:
                                window['turn'].update('Turn: Black')
                                player = -1
                            else:
                                window['turn'].update('Turn: White')
                                player = 1

                        except:
                            pass
                        pice_to_move = None
                        where_to_move = None
                        legal_moves = []
                    else:
                        for m in legal_moves:
                            if m != where_to_move:
                                if get_piece(m) is not None and get_piece(m).islower():
                                    window[f'{m[0]}{m[1]}'].update(button_color = ('white','black'))
                                else:
                                    window[f'{m[0]}{m[1]}'].update(button_color = ('black','white'))
                        try:
                            last_pos_str = "Last move: "+f"{pos_to_coor[0][pice_to_move[1]]}{pos_to_coor[1][pice_to_move[0]]}"+" to "+f"{pos_to_coor[0][where_to_move[1]]}{pos_to_coor[1][where_to_move[0]]}"
                            window['last_move'].update(f'{last_pos_str}')
                        except:
                            pass
                        pice_to_move = None
                        where_to_move = None
                        legal_moves = []
    print(f"{player_color[player*-1]} won!")

if __name__== "__main__":
    gui_main()
    # main()
