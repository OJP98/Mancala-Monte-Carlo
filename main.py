# %%
from funcs import *
import random
import copy

# 0 for player 1 / 1 for player 2
score = [0, 0]

playerTurn = nextPlayerTurn = 0
gameOver = False
lastStonePos = 0
actualBoard = [
    [4, 4, 4, 4, 4, 4, 0],
    [4, 4, 4, 4, 4, 4, 0]
]

# ! *********************************************


def getNextMove(board):
    posicionesDisponibles = []
    for i in range(0, 6):
        if(board[i] != 0):
            posicionesDisponibles.append(i)
    return posicionesDisponibles[int(random.uniform(0, len(posicionesDisponibles)))]


def isEnd(board):
    control1 = False
    control2 = False

    if(board[0][0] == board[0][1] == board[0][2] == board[0][3] == board[0][4] == board[0][5] == 0):
        control1 = True
    if(board[1][0] == board[1][1] == board[1][2] == board[1][3] == board[1][4] == board[1][5] == 0):
        control2 = True

    return control1 or control2


def getPoints(board):
    points1 = board[0][0] + board[0][1] + board[0][2] + \
        board[0][3] + board[0][4] + board[0][5] + board[0][6]

    points2 = board[1][0] + board[1][1] + board[1][2] + \
        board[1][3] + board[1][4] + board[1][5] + board[1][6]

    return points1, points2
    #print(f'Puntos jugador 0 {points1}\nPuntos jugador 1 {points2}')


def monteCarloMove(board):
    jugadorActual = 1
    control = False
    firstMove = None
    while(not isEnd(board)):
        # ? Jugador 0 Humano
        # ? Jugador 1 Monte Carlo

        if(jugadorActual == 1):
            # * Tira jugador 1
            nextMove = getNextMove(board[1])
            board, jugadorActual = Move(
                playerTurn=1, cell=nextMove, board=board)

            if (not control):
                firstMove = nextMove
                control = True

        else:
            # * Tira jugador 0
            board, jugadorActual = Move(
                playerTurn=0, cell=getNextMove(board[0]), board=board)

    points1, points2 = getPoints(board)

    if(points2 > points1):
        # Gano
        return firstMove, 1
    else:
        # perdio
        return firstMove, 0


def monteCarloBestMove(originalBoard, iterations):
    movesDict = {}
    for i in range(0, 6):
        movesDict[i] = [0, 0]  # Wins, Total

    for _ in range(iterations):
        iterationMove, winLose = monteCarloMove(copy.deepcopy(originalBoard))
        if(iterationMove != None):
            movesDict[iterationMove][1] += 1

            if(winLose):
                movesDict[iterationMove][0] += 1

    for i in range(0, 6):
        try:
            movesDict[i] = movesDict[i][0]/movesDict[i][1]
        except:
            movesDict[i] = 0

    movesDict = dict(
        sorted(movesDict.items(), key=lambda x: x[1], reverse=True))

    return list(movesDict.keys())[0]

    # ! *********************************************


print("Tablero Inicial")
PrintBoard(actualBoard)
print()
'''

board, nextPlayerTurn = Move(playerTurn=0, cell=5, board=board)
print("Tablero")
print(board)

print()
'''
print("Mejor Tiro")
# Posicion 0 del board siempre es mi tablero
# playerId 0 siempre para mi
print(monteCarloBestMove(copy.deepcopy(actualBoard), 10000))

print()
PrintBoard(actualBoard)
