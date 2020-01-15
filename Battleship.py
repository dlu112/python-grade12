from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print (" ".join(row))

print ("Let's play Battleship!")
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

for turn in range(4):
    print ("Turn ",(turn+1))
    turn = turn+1
    guess_row = int(input("Guess Row:"))
    guess_col = int(input("Guess Col:"))
    if guess_row-1 == ship_row and guess_col-1 == ship_col:
        print ("Congratulations! You sunk my battleship!")
        break
    else:
        if (guess_row-1 < 0 or guess_row-1 > 4) or (guess_col-1 < 0 or guess_col-11 > 4):
            print ("Oops, that's not even in the ocean.")
            if turn == 4:
                print("Game over")
                print("The battleship was at row", ship_row+1,", column", ship_col+1)
        elif(board[guess_row-1][guess_col-1] == "X"):
            print ("You guessed that one already.")
            if turn == 4:
                print("Game over")
                print("The battleship was at row", ship_row+1,", column", ship_col+1)
        else:
            print ("You missed my battleship!")
            board[guess_row-1][guess_col-1] = "X"
            if turn == 4:
                print("Game over")
                print("The battleship was at row", ship_row+1,", column", ship_col+1)
    print_board(board)