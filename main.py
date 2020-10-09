# %%
from funcs import *

# 0 for player 1 / 1 for player 2
score = [0,0]

playerTurn = nextPlayerTurn = 0
gameOver = False
lastStonePos = 0
board = [
	[4,4,4,4,4,4,0],
	[4,4,4,4,4,4,0]
]

board, nextPlayerTurn = Move(playerTurn, 1, board)
PrintBoard(board)