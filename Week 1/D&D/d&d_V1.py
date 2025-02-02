import math
import random
def dragon():
    row = math.ceil(random.random()*4)
    col = math.ceil(random.random()*4)
    return str(row) ,col
def dungeon():
    row = math.ceil(random.random()*4)
    col = math.ceil(random.random()*4)
    return str(row) ,col
def player():
    row = math.ceil(random.random()*4)
    col = math.ceil(random.random()*4)
    return str(row) ,col
while dungeon() != dragon() and player != dragon() and player != dungeon() :
    dun_row ,dun_col = dungeon()
    drag_row ,drag_col = dragon()
    player_row,player_col = player()
board = {}
for i in range(1,17):
    row = str(math.ceil(i/4))
    if row not in board:
        board[row] = {}
    column = 4 if i%4 == 0 else i%4  
    board[row][column] = "_" 
status = "play"
result = ["win" , "lose"]
moves = ["up","down","right","left"]
print(f"dragon : {drag_col,drag_row}")
print(f"dungeon : {dun_col,dun_row}")
while status not in result:
    board[player_row][player_col] = "X"
    print(" _ _ _ _")
    for row in board.items():
        for cell in row[1].items():
            print("|",end="")
            print(cell[1],end="")
        print("|",end="")   
        print()
    print()
    move = input("move : ")
    move = move.lower()
    old_row ,old_col = player_row,player_col
    if move == "up":
        if player_row =="1":
            print("im hitting wall")
        else:    
            player_row = str(int(player_row)-1)
    elif move == "down":
        if player_row =="4":
            print("im hitting wall")
        else:    
            player_row = str(int(player_row)+1)     
    elif move == "right":
        if player_col ==4:
            print("im hitting wall")
        else:    
            player_col += 1     
    elif move == "left":
        if player_col ==1:
            print("im hitting wall")
        else:    
            player_col -= 1     
    else:
        print("incorrect command")
    board[old_row][old_col] = "_"
    if (player_row , player_col) == (dun_row,dun_col) :
        status = "win"
    elif (player_row , player_col) == (drag_row,drag_col) :
        status = "lose"
print(f"You {status}!")
