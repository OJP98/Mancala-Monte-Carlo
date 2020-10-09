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