# Function to print Tic Tac Toe board
def display(values):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[1], values[2], values[3]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[4], values[5], values[6]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
 
    print("\t  {}  |  {}  |  {}".format(values[7], values[8], values[9]))
    print("\t     |     |")
    print("\n")


row = [0,'-','-','-','-','-','-','-','-','-',0]

# display(row)

# random choice 
from random import randint

tossing = randint(0,1)
if tossing == 1:
  player1_symbol = "X"
  player2_symbol = "0"
else:
  player2_symbol = "X"
  player1_symbol = "0"

print(f"player 1's symbol is '{player1_symbol}' ")
print(f"player 2's symbol is '{player2_symbol}' ")
  
# print(player2)


# checking for the inputs are valid or not

def valid_input(n):
  if n not in range(1,10):
    return False
  if row[n] != "-":
    return False
  return True

# taking input from players
def take_input():
  data=int(input("Enter your choice from 1 to 9: "))
  if valid_input(data):
    
    return data
  else:
    print("invalid input")
    return take_input()
  

# check are there any space or not
def is_space(row):
  if "-" not in row:
    return False
  return True


# checking for winner

def winner(row):
  if row[1] == row [2] == row[3]:
    return row[1]
  elif  row[4] == row [5] == row[6]:
    return row[4]
  elif row[7] == row [8] == row[9]:
    return row[7]
  elif row[1] == row [4] == row[7]:
    return row[1]
  elif row[2] == row [5] == row[8]:
    return row[2]
  elif row[3] == row [6] == row[9]:
    return row[3]
  elif row[3] == row [6] == row[9] :
    return row[3]
  elif row[1] == row [5] == row[9]:
    return row[1]
  elif row[1] == row [5] == row[9]:
    return row[1]
  elif row[3] == row [5] == row[7]:
    return row[3]
  else:
    return "Z"

  



player_list={
  player1_symbol : "Player 1",
  player2_symbol : "Player 2"
}
# print(player_list)
# print(player_list[player1_symbol])
for round in range(1,10):
  if not is_space(row):
    print("Match is tied")
    break
  result = winner(row)
  if result != "Z" and result != '-':
    print(f"{player_list[result]} is the winner")
    break
  print("player1's turn")
  player1 = take_input()
  
  row[player1] = player1_symbol
  display(row)
  if not is_space(row):
    print("Match is tied")
    break
  result = winner(row)
  if result != "Z" and result != '-':
    print(f"{player_list[result]} is the winner")
    break
  print("Player2's turn ")
  player2 = take_input()
  
  row[player2] = player2_symbol
  display(row)




  

