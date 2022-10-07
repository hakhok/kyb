
def draw_board(board):
    print('\n')
    for i, row in enumerate(board):
        print(i+1, end="")
        for number in row:
            if number == 0:
                print('|-', end="")
            elif number == 1:
                print(f'|X', end="")
            else:
                print(f'|O', end="")
        print('|')
    print('  1 2 3')
    
def winner_check(b):
    for row in b:
        if row[0]==row[1] and row[1]==row[2]:
            if row[0] != 0:
                return row[0]
    for i in range(3):
        if b[0][i]==b[1][i] and b[1][i]==b[2][i]:
            if b[0][i] != 0:
                return b[0][i]
    if b[0][0]==b[1][1] and b[1][1]==b[2][2]:
        if b[0][0] != 0:
            return b[0][0]
    if b[2][0]==b[1][1] and b[1][1]==b[0][2]:
        if b[1][1] != 0:
            return b[1][1]

def input_name():
    player_1 = input("Player 1 name: ")
    player_2 = input("Player 2 name: ")
    return [player_1, player_2]

def check_free_spot(spot, b):
    i, j = spot
    if b[j-1][i-1] != 0:
        return False
    return True

def player_input():
    try:
        i = input("Place your piece: [x y]")
        i = i.split(' ')
        if 0 < int(i[0]) < 4:
            if 0 < int(i[1]) < 4:
                return [int(i[0]), int(i[1])]
            else:
                print("Skriv koordinatet på formen: 1 1")
        else:
            print("Skriv koordinatet på formen: 1 1")
    except:
        print("Skriv koordinatet på formen: 1 1")

def main():
    players = input_name()
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    player = 2
    draw_board(board)
    while not winner_check(board):
        if player==1: player = 2
        else: player = 1
        print(f"\n{players[player-1]} sin tur:")
        spot = player_input()
        while not spot:
            spot = player_input()
        while not check_free_spot(spot, board):
            print("Spot taken, choose another spot")
            spot = player_input()
            while not spot:
                spot = player_input()
        board[spot[1]-1][spot[0]-1] = player
        draw_board(board)
    draw_board(board)
    print(f"Vinneren er: {players[player-1]}")

main()
