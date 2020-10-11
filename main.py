from funcs import *
import random
import copy
import platform
import os
import time

playerTurn = nextPlayerTurn = 0
gameOver = False
lastStonePos = 0
actualBoard = [
    [4, 4, 4, 4, 4, 4, 0],
    [4, 4, 4, 4, 4, 4, 0]
]

if(platform.system() == 'Windows'):
    BORRAR = 'cls'
else:
    BORRAR = 'clear'


os.system(BORRAR)
NUM_ITERATIONS = getNumIteration(BORRAR)


while not isEnd(actualBoard):
    PrintBoard(actualBoard)

    if playerTurn == 0:
        print("Your turn...")
        while 1:
            userTurn = validateUserTurn(copy.deepcopy(actualBoard[0]))
            if userTurn == None:
                PrintBoard(actualBoard)
                continue
            else:
                actualBoard, playerTurn = Move(
                    playerTurn=0, cell=userTurn - 1, board=copy.deepcopy(actualBoard))
                break

    else:
        print("PC turn...")
        pcTurn = monteCarloBestMove(copy.deepcopy(actualBoard), NUM_ITERATIONS)
        actualBoard, playerTurn = Move(
            playerTurn=1, cell=pcTurn, board=copy.deepcopy(actualBoard))
        time.sleep(1)

os.system(BORRAR)
PrintBoard(actualBoard)
points1, points2 = getPoints(actualBoard)
print()

if(points1 > points2):
    print("The winner is Player 1")
else:
    print("The winner is Player 2")

'''
print("Tablero Inicial")
PrintBoard(actualBoard)
print()

actualBoard, nextPlayerTurn = Move(
	playerTurn=1, cell=5, board=copy.deepcopy(actualBoard))


print()
PrintBoard(actualBoard)
'''
