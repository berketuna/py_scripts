from random import randint

board = []

for x in range(5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print " ".join(row)
print ""
print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

for turn in range(10):
  print ""
  guess_row = int(raw_input("Guess Row: "))-1
  guess_col = int(raw_input("Guess Col: "))-1

  if guess_row == ship_row and guess_col ==   ship_col:
    print ""
    print "Congratulations! You sunk my battleship!"
    break

  elif guess_row == 8 and guess_col == 8:
    print ""
    print "Ship Row:%s,Ship Column:%s" %(ship_row+1,ship_col+1)

  else:

    if (guess_row < 0 or guess_row > 4) or   (guess_col < 0 or guess_col > 4):
      print ""
      print "Oops, that's not even in the ocean."

    elif(board[guess_row][guess_col] ==     "X"):
      print ""
      print "You guessed that one already."

    else:
      print ""
      print "You missed my battleship!"
      board[guess_row][guess_col] = "X"

    print ""
    print "Remaining turn: %s" %(3-turn)
    print ""
    print_board(board)

    if turn == 3:
      print ""
      print "Game Over"
      break
