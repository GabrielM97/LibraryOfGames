#Matthew Nicholas S6089196
import time 
import random
print("""
  ____  _            _    _           _                  
 |  _ \| |          | |  | |         | |                 
 | |_) | | __ _  ___| | _| |__   ___ | | ___  ___        
 |  _ <| |/ _` |/ __| |/ / '_ \ / _ \| |/ _ \/ __|       
 | |_) | | (_| | (__|   <| | | | (_) | |  __/\__ \       
 |____/|_|\__,_|\___|_|\_\_| |_|\___/|_|\___||___/       
                              | |                        
                __ _ _ __   __| |                        
               / _` | '_ \ / _` |                        
 __          _| (_| | | | | (_| |_           _           
 \ \        / /\__,_|_| |_|\__,_| |         | |          
  \ \  /\  / /__  _ __ _ __ ___ | |__   ___ | | ___  ___ 
   \ \/  \/ / _ \| '__| '_ ` _ \| '_ \ / _ \| |/ _ \/ __|
    \  /\  / (_) | |  | | | | | | | | | (_) | |  __/\__ \\    
     \/  \/ \___/|_|  |_| |_| |_|_| |_|\___/|_|\___||___/
     
""")

print("""
+-----+   Player 1 will always be on the left of the box
|  1  |   Player 2 will always be on the left of the box
| 1 2 |   If there is a dot in the middle of the box it means you have come to a blackhole or wormhole
+-----+   and will be moved back or forward accordingly
""")
p1counter = "1"
p2counter = "2"
p1counter = input("Please enter your counter icon Player 1 ")
p1counter = str(p1counter)+ " "
p1counter = p1counter[0]
p2counter = input("Please enter your counter icon Player 2 ")
p2counter = str(p2counter)+ " "
p2counter = p2counter[0]

roll = 0
boardheight = 10 
boardwidth = 10
boardtotal = boardheight * boardwidth
halfbh = 5
board = []
currplayerpos = 0
W = "⊙"
B = "●"
def dice(roll):
    
    roll = random.randrange(1,7) 

    if roll == 1:
        print("""
    +-------+
    |       |
    |   0   |
    |       |
    +-------+
    """)
    elif roll == 2:
        print("""
    +-------+
    | 0     |
    |       |
    |     0 |
    +-------+
    """)
    elif roll == 3:
        print("""
    +-------+
    | 0     |
    |   0   |
    |     0 |
    +-------+
    """)
    elif roll == 4:
        print("""
    +-------+
    | 0   0 |
    |       |
    | 0   0 |
    +-------+
    """)
    elif roll == 5:
        print("""
    +-------+
    | 0   0 |
    |   0   |
    | 0   0 |
    +-------+
    """)
    elif roll == 6:
        print("""
    +-------+
    | 0   0 |
    | 0   0 |
    | 0   0 |
    +-------+
    """)
    print("You rolled a " , roll)
    return roll
    time.sleep(2)

p1arr = []
p2arr = []
gameplay = []

for count in range(0,boardtotal): # making the array for the board        
        board.extend(["   "])
        p1arr.extend([" "])
        p2arr.extend([" "])
        gameplay.extend([" "])
for count  in range(7):
    bhcount = random.randrange(18,98) #80
    gameplay[bhcount] = B
for count  in range(7):
    whcount = random.randrange(5,85) #80
    
    gameplay[whcount] = W


def drawboard(board): # defining the drawboard 

    cellid = 100
    for count in range(0,halfbh):
        
        print("") # get new line closer than what \n would have gotten
        for count in range(0,boardwidth):
            
            print("+-----+",end = "") #print the first line witch is the top of the cells 
                
        print("")   
        for count in range(0,boardwidth):

            cellid = cellid - 1
            if cellid < 10:
                board[cellid] = " "+ str(cellid+1) + " "
            elif cellid <99:
                board[cellid] = str(cellid+1) + " "
            else:
                board[cellid] = str(cellid+1)
            print("| ",end="")     
            print(board[cellid],end="")
            print(" |",end="")
        cellid = cellid + 10
        print("")
        for count in range(0,boardwidth):
            cellid = cellid - 1
            print("| ",end="")
            print(p1arr[cellid],end="")
            print(gameplay[cellid],end="")
            print(p2arr[cellid],end="")
            print(" |",end = "")

        
        print("")        
        for count in range(0,boardwidth):
            print("+-----+",end="")


        
        print("") # get new line closer than what \n would have gotten
        for count in range(0,boardwidth):
            
            print("+-----+",end = "") #print the first line witch is the top of the cells 
                
        print("")
        cellid = cellid - 11

        for count in range(0,boardwidth):


            cellid = cellid + 1
            if cellid < 9:
                board[cellid] = " "+ str(cellid+1) + " "
            elif cellid <99:
                board[cellid] = str(cellid+1) + " "
            else:
                board[cellid] = str(cellid+1)
            print("| ",end="")     
            print(board[cellid],end="")
            print(" |",end="")
        cellid = cellid - 10
        print("")
        for count in range(0,boardwidth):
            cellid = cellid + 1
            print("| ",end="")
            print(p1arr[cellid],end="")
            print(gameplay[cellid],end="")
            print(p2arr[cellid],end="")
            print(" |",end = "")
                
        print("")        
        for count in range(0,boardwidth):
            print("+-----+",end="")
        

        cellid = cellid - 9
p1pos = 0
p2pos = 0
p1arr[p1pos] = p1counter
p2arr[p2pos] = p2counter

Game = "On"
if Game != "Over":
    drawboard(board)

while Game != "Over":
    if Game !="Over":
        print("\n⊙ is wormhole and ● is blackhole")
        print("\n",p1pos+1)
        print("\n PLAYER 1")
        ready = "meme"
        while (ready.lower() !="y") or (ready==""):
            ready = input("Are you ready? Y/N ")
        p1arr[p1pos] = " "
        p1prevpos = p1pos
        p1pos = p1pos + dice(roll)
        if p1pos > 99:
            p1pos = p1prevpos
            print("Cannot move, skipping turn")
        p1arr[p1pos] = p1counter
        drawboard(board)
        if gameplay[p1pos] == W:
            p1arr[p1pos] = " "
            forward = random.randrange(5,15)
            print("\nYou landed on a wormhole so prepare to go from space ", p1pos+1)
            p1pos = p1pos + forward 
            print("WHOOOSH! You went forward " , forward, " spaces.")
            p1arr[p1pos] = p1counter
            drawboard(board)
        elif gameplay[p1pos] == B:
            p1arr[p1pos] = " "
            backward = random.randrange(5,15)
            print("\nYou landed on a blackhole so prepare to escape from space ", p1pos+1)
            p1pos = p1pos - backward 
            print("Darkness surrounds you as you successfully escape the blackhole but loose " , backward, " spaces.")
            p1arr[p1pos] = p1counter
            drawboard(board)
        if p1pos == 99:
            end = "Welldone! Player 1 you have won!"
            Game = "Over"
        
    if Game !="Over":
        print("\n⊙ is wormhole and ● is blackhole")
        print("\n",p2pos+1)
        print("\n PLAYER 2")
        ready = "meme"
        while (ready.lower() !="y") or (ready==""):
            ready = input("Are you ready? Y/N ")
        p2arr[p2pos] = " "
        p2prevpos = p2pos
        p2pos = p2pos + dice(roll)
        if p2pos > 99:
            p2pos = p2prevpos
            print("Cannot move, skipping turn")
        p2arr[p2pos] = p2counter
        drawboard(board)
        if gameplay[p2pos] == W:
            p2arr[p2pos] = " "
            forward = random.randrange(5,15)
            print("\nYou landed on a wormhole so prepare to go from space ", p2pos+1)
            p2pos = p2pos + forward 
            print("WHOOOSH! You went forward " , forward, " spaces.")
            p2arr[p2pos] = p2counter
            drawboard(board)
        elif gameplay[p2pos] == B:
            p2arr[p2pos] = " "
            backward = random.randrange(5,15)
            print("\nYou landed on a blackhole so prepare to escape from space ", p2pos+1)
            p2pos = p2pos - backward 
            print("Darkness surrounds you as you successfully escape the blackhole but loose " , backward, " spaces.")
            p2arr[p2pos] = p2counter
            drawboard(board)
        if p2pos == 99:
            end = "Welldone! Player 2 you have won!"
            Game = "Over"
            
print("\n" ,end)
        
        
    
