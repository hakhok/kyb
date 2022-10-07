import PySimpleGUI as sg


board = [
    ["r", "n", "b", "q", "K", "b", "n", "r"],
    ["p"]*8,
    [None]*8,
    [None]*8,
    # [None]*3+["P"]+[None]*4,
    # [None]*8,
    # [None]*8,
    [None]*8,
    [None]*8,
    ["P"]*8,
    ["R", "N", "B", "Q", "k", "B", "N", "R"]
]
board2 = [
    ["r", "n", "b", "q", "K", "b", "n", "r"],
    ["p"]*8,
    # [None]*8,
    # [None]*8,
    # # [None]*3+["P"]+[None]*4,
    # # [None]*8,
    # # [None]*8,
    # [None]*8,
    # [None]*8,
    ["P"]*8,
    ["R", "N", "B", "Q", "k", "B", "N", "R"]
]

layout = []
for i, row in enumerate(board):
    r=[]
    for j, piece in enumerate(row):
        if piece:
            if piece.isupper():
                c = sg.Button(piece, size=(3, 2), button_color = ('black', 'white'), key=f'{i}{j}')
            else:
                c = sg.Button(piece, size=(3, 2), button_color = ('white', 'black'), key=f'{i}{j}')

        else: 
            c = sg.Button(" ", size=(3, 2))
        r.append(c)
    layout.append(r)
layout.append([sg.Exit()])
layout2 = []
for i, row in enumerate(board):
    r=[]
    for j, piece in enumerate(row):
        if piece:
            if piece.isupper():
                c = sg.Button(piece, size=(3, 2), button_color = ('black', 'white'), key=f'{i}{j}')
            else:
                c = sg.Button(piece, size=(3, 2), button_color = ('white', 'black'), key=f'{i}{j}')

        else: 
            c = sg.Button(" ", size=(3, 2))
        r.append(c)
    layout2.append(r)
layout2.append([sg.Exit()])

window = sg.Window("Chess", layout, element_padding=(1,1), default_element_size=(40,40))
while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, "Exit"):
        break
    for i, row in enumerate(board):
        for j, piece in enumerate(row):
            if event == f'{i}{j}':
                window[f'{i}{j}'].update("aa", button_color = ('black','red'))  
    