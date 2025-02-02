import random
import math
class Board:
    def __init__(self,row_scale: int,col_scale: int):
        if 3 <= row_scale <= 8:
            self._row_scale = row_scale
        else:
            raise ValueError("row_scale must be in range: 3, 4, 5, 6")

        if 3 <= col_scale <= 8:
            self._col_scale = col_scale
        else:
            raise ValueError("col_scale must be in range: 3, 4, 5, 6")
        self.board = {}

    def places(self):
        row = math.ceil(random.random()*self._row_scale)
        col = math.ceil(random.random()*self._col_scale)
        return str(row) ,col
    
    def set_places(self):
        while True:
            self.player = self.places()
            self.dungeon = self.places()
            self.dragon = self.places()
            self.map_location = self.places()  
            if self.player != self.dungeon and self.dungeon != self.dragon and self.dragon != self.player and self.map_location != self.player and self.map_location != self.dungeon and self.map_location != self.dragon:
                break       
        self.row_p,self.col_p =self.player 
        self.row_d,self.col_d =self.dragon 
        self.row_m,self.col_m =self.map_location 

    def board_creator(self):
        for row in range(1,self._row_scale+1):
            row = str(row)
            if row not in self.board:
                self.board[row] = {}
            for column in range(1,self._col_scale+1):  
                self.board[row][column] = "_" 
        self.board[self.row_m][self.col_m] = "M" 
                        
    def board_printer(self):
        self.board[self.row_p][self.col_p] = "X"
        self.row_dist = abs(int(self.row_d) - int(self.row_p))
        self.col_dist = abs(self.col_d - self.col_p)
        self.show_dragon = False
        if self.row_dist < 2 and self.col_dist < 2:
            self.show_dragon = True
        else:
            self.show_dragon = False
        self.board[self.dragon[0]][self.dragon[1]] = "D" if self.show_dragon else "_"
        

        map_dist = abs(int(self.row_m) - int(self.row_p)) + abs(self.col_m - self.col_p)
        if map_dist <= 2:
            self.board[self.row_m][self.col_m] = "M"
        else:
            self.board[self.row_m][self.col_m] = "_"
        
        print(" _"*self._col_scale)

        for row in self.board.items():
            for cell in row[1].items():
                print("|",end="")
                print(cell[1],end="")
            print("|",end="")   
            print()
        print()

    def check_for_map(self):
        if (self.row_p, self.col_p) == (self.row_m, self.col_m):
            input(f"You found a map! It says: What is that animal that have {self.dungeon[0]} legs and {self.dungeon[1]} eyes? : say anythong for continue!")
    def dragon_move(self):
            self.board[self.row_d][self.col_d] = "_"  
            if self.row_dist > self.col_dist:
                if int(self.row_d) > int(self.row_p) and self.row_d != "1":
                    self.row_d = str(int(self.row_d) - 1)
                elif int(self.row_d) < int(self.row_p) and self.row_d != str(self._row_scale):
                    self.row_d = str(int(self.row_d) + 1)
            else:
                if self.col_d > self.col_p and self.col_d != 1:
                    self.col_d -= 1
                elif self.col_d < self.col_p and self.col_d != self._col_scale:
                    self.col_d += 1
            self.board[self.row_d][self.col_d] = "D"
            self.dragon = (self.row_d, self.col_d)  

    def dragon_senses(self):
        distance = abs(int(self.row_d) - int(self.row_p)) + abs(self.col_d - self.col_p)
        if distance == 1:
            if random.random() < 0.9:
                self.dragon_move()
        elif distance <= 3:
            if random.random() < 0.3:
                self.dragon_move()

    def player_hears_dragon(self):
        distance = abs(int(self.row_d) - int(self.row_p)) + abs(self.col_d - self.col_p)
        if distance == 1:
            print("You see the dragon!")
        elif distance <= 3:
            print("You hear the dragon nearby!")

    def move(self,move):
        move = move.lower()
        moves = ["up","down","right","left"]
        if move in moves:
            self.board[self.row_p][self.col_p] = "_"
            if move == "up":
                if self.row_p == "1":
                    print("hitting wall")
                else:
                    self.row_p = str(int(self.row_p)-1)

            if move == "down":
                if self.row_p == self._row_scale:
                    print("hitting wall")
                else:
                    self.row_p = str(int(self.row_p)+1)

            if move == "left":
                if self.col_p == 1:
                    print("hitting wall")
                else:
                    self.col_p -=1
            if move == "right":
                if self.col_p == self._col_scale:
                    print("hitting wall")
                else:
                    self.col_p +=1
            
        
b = Board(8,8)
b.set_places()
b.board_creator()
b.board_printer()
moves = ["up","down","right","left"]
while True:
    move = input("move : ")
    if move not in moves:
        print(f"incorrect command : valid commands are {moves}")
        continue
    b.move(move)
    player = (b.row_p,b.col_p)
    dungeon = b.dungeon
    dragon = (b.row_d,b.col_d)
    b.player_hears_dragon()
    b.check_for_map()
    if b.show_dragon:
        b.board[b.row_d][b.col_d] = "_"
        if b.row_dist < 3 or b.col_dist < 3:
                b.dragon_senses()
    room = map(int,player)
    status = "win" if player == dungeon else "lose" if player == dragon else ""   
    if status:
        print(f"You {status}!")
        break
    b.board_printer()
    print(f"you are in room {tuple(room)}")
