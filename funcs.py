
import random
import copy
import os
import time
# ! *********************************************


def getNextMove(board):
    posicionesDisponibles = []
    for i in range(0, 6):
        if(board[i] != 0):
            posicionesDisponibles.append(i)
    return posicionesDisponibles[int(random.uniform(0, len(posicionesDisponibles)))]


def getPosiblesTurnos(board):
    posicionesDisponibles = []
    for i in range(0, 6):
        if(board[i] != 0):
            posicionesDisponibles.append(i)
    return posicionesDisponibles


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


def getNumIteration(BORRAR):
    while True:
        print("Select the difficulty level")
        print("1. Noob")
        print("2. Advanced")
        print("3. Pro")
        selection = input("> ")

        try:
            if(1 <= int(selection) <= 3):
                if(int(selection) == 1):
                    return 0
                if(int(selection) == 2):
                    return 500
                else:
                    return 10000
            else:
                print("Enter a valid option!")
                time.sleep(2)
                os.system(BORRAR)

        except:
            print("Enter a valid option!")
            time.sleep(2)
            os.system(BORRAR)


def validateUserTurn(board):
    userTurn = input("> ")
    posibleTurns = getPosiblesTurnos(board)
    try:
        if(int(userTurn) in posibleTurns):
            return int(userTurn)
        else:
            print("Enter a valid option!")
            time.sleep(1)
            return None
    except:
        print("Enter a valid option!")
        time.sleep(1)
        return None

# ! *********************************************


def Move(playerTurn, cell, board):
    lastPos = 0
    currRow = playerTurn

    # Assume the next player moving will be the opponent
    nextPlayerTurn = (playerTurn + 1) % 2
    # Get the amount of stones that the selected cell has
    stones = board[playerTurn][cell]
    board[playerTurn][cell] = 0

    #                           MAIN MOVEMENT
    #################################################################
    while stones > 0:
        # Change to the next cell
        cell += 1
        # Keep the last position a stone was played
        lastPos = cell

        # We need to check if we're on the pit of the current player
        if cell == 6 and currRow == playerTurn:
            # Add 1 to the pit of stones of the current player
            board[currRow][cell] = board[currRow][cell] + 1

            # Change the row we're in and reset the counter
            cell = -1
            stones -= 1
            currRow = (currRow + 1) % 2

        # Check if we're on the opponent's pit
        elif cell == 6:
            # Change the row we're in and reset the counter
            cell = -1
            currRow = (currRow + 1) % 2

            # NOTE: we're not adding a new stone to the pit
            # nor substracting another stone from out total.
            continue

        else:
            # We just add 1 stone to the current cell
            board[currRow][cell] = board[currRow][cell] + 1
            stones -= 1

    #                     CHECK IF LAST POS == 1
    # If that's the case, we take the stones in the front row.
    #################################################################
    if board[currRow][lastPos] == 1 and currRow == playerTurn and lastPos != 6:

        frontPos = (currRow + 1) % 2
        opponentPit = board[frontPos][-1]
        frontRow = board[frontPos][:6][::-1]
        frontStones = frontRow[lastPos]

        board[frontPos][5-lastPos] = 0

        # If the other player has stones in its cell, collect them
        if frontStones > 0:
            board[currRow][-1] = board[currRow][-1] + frontStones

    #                  CHECK IF LAST POS == PIT
    #################################################################
    elif lastPos == 6:
        # If that's true, then the player gets another turn
        nextPlayerTurn = playerTurn

    return board, nextPlayerTurn


def PrintBoard(board):
    row0 = board[0]
    row1 = board[1][::-1]
    print(row1)
    print('  ', row0)
