# Tic Tac Toe game with GUI
# using tkinter

# importing all necessary libraries
import random
import tkinter
from tkinter import *
from functools import partial
from tkinter import messagebox
from copy import deepcopy

# importing the pyttsx library
import pyttsx3
engine = pyttsx3.init('sapi5')  # initializes the connection and provides engine that converts text to voice
# sapi5 is a technology for voice recognition
voices = engine.getProperty('voices')  # getting details of current voice
# print(voices[0].id)
engine.setProperty('voices', voices[1].id)  # changing index, changes voices. 1 for female. 0 for female
engine.setProperty('rate', 200)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
# sign variable to decide the turn of which player
sign = 0

# Creates an empty board
global board
board = [[" " for x in range(3)] for y in range(3)]


# Check l(O/X) won the match or not
# according to the rules of the game
def winner(b, l):
    return ((b[0][0] == l and b[0][1] == l and b[0][2] == l) or
            (b[1][0] == l and b[1][1] == l and b[1][2] == l) or
            (b[2][0] == l and b[2][1] == l and b[2][2] == l) or
            (b[0][0] == l and b[1][0] == l and b[2][0] == l) or
            (b[0][1] == l and b[1][1] == l and b[2][1] == l) or
            (b[0][2] == l and b[1][2] == l and b[2][2] == l) or
            (b[0][0] == l and b[1][1] == l and b[2][2] == l) or
            (b[0][2] == l and b[1][1] == l and b[2][0] == l))


# Check if the player can push the button or not
def isfree(i, j):
    return board[i][j] == " "


# Check the board is full or not
def isfull():
    flag = True
    for i in board:
        if (i.count(' ') > 0):
            flag = False
    return flag


# Create the GUI of game board for play along with another player
def gameboard_pl(game_board, l1, l2):
    global button
    button = []
    for i in range(3):
        m = 3 + i
        button.append(i)
        button[i] = []
        for j in range(3):
            n = j
            button[i].append(j)
            get_t = partial(get_text, i, j, game_board, l1, l2)
            button[i][j] = Button(
                game_board, bd=5, command=get_t, height=4, width=8)
            button[i][j].grid(row=m, column=n)
    game_board.mainloop()


# Decide the next move of system
def pc():
    possiblemove = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == ' ':
                possiblemove.append([i, j])
    move = []
    if possiblemove == []:
        return
    else:
        for let in ['O', 'X']:
            for i in possiblemove:
                boardcopy = deepcopy(board)
                boardcopy[i[0]][i[1]] = let
                if winner(boardcopy, let):
                    return i
        corner = []
        for i in possiblemove:
            if i in [[0, 0], [0, 2], [2, 0], [2, 2]]:
                corner.append(i)
        if len(corner) > 0:
            move = random.randint(0, len(corner) - 1)
            return corner[move]
        edge = []
        for i in possiblemove:
            if i in [[0, 1], [1, 0], [1, 2], [2, 1]]:
                edge.append(i)
        if len(edge) > 0:
            move = random.randint(0, len(edge) - 1)
            return edge[move]


# Configure text on button while playing with system
def get_text_pc(i, j, gb, l1, l2):
    global sign
    if board[i][j] == ' ':
        if sign % 2 == 0:
            l1.config(state=DISABLED)
            l2.config(state=ACTIVE)
            board[i][j] = "X"
        else:
            button[i][j].config(state=ACTIVE)
            l2.config(state=DISABLED)
            l1.config(state=ACTIVE)
            board[i][j] = "O"
        sign += 1
        button[i][j].config(text=board[i][j])
    x = True
    if winner(board, "X"):
        gb.destroy()
        x = False
        speak("congratulations, you won!!")
    elif winner(board, "O"):
        gb.destroy()
        x = False
        speak("Haha! I won")
    elif (isfull()):
        gb.destroy()
        x = False
        speak("Tie Game")
    if (x):
        if sign % 2 != 0:
            move = pc()
            button[move[0]][move[1]].config(state=DISABLED)
            get_text_pc(move[0], move[1], gb, l1, l2)


# Create the GUI of game board for play along with system
def gameboard_pc(game_board, l1, l2):
    global button
    button = []
    for i in range(3):
        m = 3 + i
        button.append(i)
        button[i] = []
        for j in range(3):
            n = j
            button[i].append(j)
            get_t = partial(get_text_pc, i, j, game_board, l1, l2)
            button[i][j] = Button(
                game_board, bd=5, command=get_t, height=4, width=8)
            button[i][j].grid(row=m, column=n)
    game_board.mainloop()


# Initialize the game board to play with system
def withpc(game_board):
    game_board.destroy()
    game_board = Tk()
    game_board.title("Tic Tac Toe")
    l1 = Button(game_board, text="YOU : X", width=10)
    l1.grid(row=1, column=1)
    l2 = Button(game_board, text="JARVIS : O",
                width=10, state=DISABLED)

    l2.grid(row=2, column=1)
    gameboard_pc(game_board, l1, l2)


# main function
def play():
    menu = Tk()
    menu.geometry("250x250")
    menu.title("Tic Tac Toe")
    wpc = partial(withpc, menu)

    head = Button(menu, text="---Welcome to tic-tac-toe---",
                  activeforeground='red',
                  activebackground="black", bg="#ff1466",
                  fg="black", width=700, font='bubbles', bd=5)

    B1 = Button(menu, text="PLAY", command=wpc,
                activeforeground='red',
                activebackground="black", bg="#ff1466",
                fg="black", width=500, font='summer', bd=5)

    B3 = Button(menu, text="Exit", command=menu.quit, activeforeground='red',
                activebackground="black", bg="#ff1466", fg="black",
                width=700, font='summer', bd=5)
    head.pack(side='top')
    B1.pack(side='top')
    B3.pack(side='top')
    menu.mainloop()


# Call main function
if __name__ == '__main__':
    play()

