from random import randint

board = []

for x in range(0, 3):
  board.append(["[]"] * 3)

def print_board(board):
  for row in board:
    print(" ".join(row))

print_board(board)

print("You go first and play as X")

for round in range(5):
  print("Round", round + 1)
  name_row = int(input("Which Row Do You Want to Play: "))
  name_col = int(input("Which Column Do You Want to Play: "))
  while name_row not in range(1,4) or name_col not in range(1,4):
      print("Can't go there")
      name_row = int(input("Which Row: "))
      name_col = int(input("Which Col: "))
  while board[name_row-1][name_col-1] == "X" or board[name_row-1][name_col-1]=="O":
      print("Spot already taken, try another")
      name_row = int(input("Which Row: "))
      name_col = int(input("Which Col: "))
  board[name_row-1][name_col-1]="X"
  if ((board[0][0] == "X" and board[0][1] =="X" and board[0][2] == "X") or \
      (board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X") or \
      (board[2][0] =="X" and board[2][1] == "X" and board[2][2] == "X") or \
      (board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X") or \
      (board[0][1] == "X" and board[1][1] =="X" and board[2][1] == "X") or \
      (board[0][2] == "X" and board[1][2] =="X" and board[2][2] == "X") or \
      (board[0][0] == "X" and board[1][1] =="X" and board[2][2] == "X") or \
      (board[0][2] == "X" and board[1][1] =="X" and board[2][0] == "X")):
      print("You Win!")
      print_board(board)
      break
  if (round == 4):
      print("No winner lol")
      print_board(board)
      break  
  comp_row = randint(0, len(board) - 1)
  comp_col = randint(0, len(board) - 1)
  while board[comp_row][comp_col] == "X" or board[comp_row][comp_col]=="O":
      comp_row = randint(0, len(board) - 1)
      comp_col = randint(0, len(board) - 1)
  board[comp_row][comp_col] = "O"      
  print_board(board)
  if ((board[0][0] == "O" and board[0][1] =="O" and board[0][2] == "O") or \
      (board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O") or \
      (board[2][0] =="O" and board[2][1] == "O" and board[2][2] == "O") or \
      (board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O") or \
      (board[0][1] == "O" and board[1][1] =="O" and board[2][1] == "O") or \
      (board[0][2] == "O" and board[1][2] =="O" and board[2][2] == "O") or \
      (board[0][0] == "O" and board[1][1] =="O" and board[2][2] == "O") or \
      (board[0][2] == "O" and board[1][1] =="O" and board[2][0] == "O")):
      print("You lost :(")
      break  
                                                     
