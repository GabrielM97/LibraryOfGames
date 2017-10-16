gameon = True
def drawboard(contents):
    height = 2
    width = 8
    pipe = "|"
    dashes = "---"
    spc = "   "
    for row in range(0, height):
        line = pipe
        content = pipe
        for col in range(0, width):
                line = line + dashes + pipe
                content = content + contents[row * width + col] + pipe
        print(line)
        print(content)
    print(line)

#setting the board
board = ["   "] * 16

for i in range(0, 1):
    board[i] = " 0 "

for i in range(1, 7):
    board[i] = " 4 "

for i in range(7, 9):
    board[i] = "///"

for i in range(9, 15):
    board[i] = " 4 "

for i in range(15, 16):
    board[i] = " 0 "

player = 0
pla_0_ft = False
pla_1_ft = False
print("Welcome to Mancala. The aim of the game is to have more stones")
print("in the end pots by the end of the game. These spots are the top left, and bottom right.")
print("Player 1 controls the top row, Player 2 controls the bottom.")
print("The rules of Mancala are simple, score more than your opponent.")
print("Do this by moving stones around from pots. When you select a pot, it will empty and all the stones will move around, counter clockwise.")
print("Use this, and the combination of free turns to win. Good luck to the both of you.")
while gameon == True:
    print("      1   2   3   4   5   6")
    drawboard(board)
    player = (player + 1) % 2

    if pla_0_ft == True:
        player = 0
        pla_0_ft = False

    elif pla_1_ft == True:
        player = 1
        pla_1_ft = False
        
    print("Active player is: " + str(player + 1))
    move = int(input("Please input a space to move the stones: "))
    
    if player == 1:
        currentPos = move + 8
    else:
        currentPos = move
    
    counter = 0
    numbeads = int(board[currentPos])
    str(board[currentPos])
    print(board[currentPos])
    if currentPos == 1:
        board[currentPos] = " 0 "
        
    elif currentPos == 2:
        board[currentPos] = " 0 "
        
    elif currentPos == 3:
        board[currentPos] = " 0 "

    elif currentPos == 4:
        board[currentPos] = " 0 "

    elif currentPos == 5:
        board[currentPos] = " 0 "

    elif currentPos == 6:
        board[currentPos] = " 0 "

    elif currentPos == 9:
        board[currentPos] = " 0 "

    elif currentPos == 10:
        board[currentPos] = " 0 "

    elif currentPos == 11:
        board[currentPos] = " 0 "

    elif currentPos == 12:
        board[currentPos] = " 0 "

    elif currentPos == 13:
        board[currentPos] = " 0 "

    elif currentPos == 14:
        board[currentPos] = " 0 "

    
    if currentPos < 7:
        additive = -1
        
    elif currentPos > 8:
        additive = 1

   

    while counter < numbeads:
        counter = counter + 1
        currentPos = currentPos + additive

        if currentPos < 0:
            currentPos = 9
            additive = 1

        elif currentPos > 15:
            currentPos = 6
            additive = -1
        
        
        x = int(board[currentPos])
        x = x + 1
        if len(str(x)) < 2:
            board[currentPos] = " "+ str(x) +" "

        else:
            board[currentPos] = str(x) +" "

        if counter == numbeads:
            if currentPos == 0 or currentPos == 15:
                if player == 0:
                    pla_0_ft = True

                elif player == 1:
                    pla_1_ft = True

    
    if (int(board[0]) + int(board[15]) == 48):
        gameon = False
    

if board[0] > board[15]:
    print("Congratulations Player 1, you won this game of Mancala.")

elif board[0] == board[15]:
    print("You both tied, congratulations.")

elif board[0] < board[15]:
    print("Player 2 has taken this game. Well done.")
