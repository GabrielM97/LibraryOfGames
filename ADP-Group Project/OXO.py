#Joe Muana
#OXO
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
turn_count=[0]


def printBoard():
    print(" " + board[1] + " | " + board[2] + " | " + board[3] + " ")
    print("___|___|___")
    print(" " + board[4] + " | " + board[5] + " | " + board[6] + " ")
    print("___|___|___")
    print(" " + board[7] + " | " + board[8] + " | " + board[9] + " ")
    print("   |   |   ")

        
def CheckWin():
   
    win = False
    #Horizontal winning condition    
    if(board[1] == board[2] and board[2] == board[3] and board[1] != ' '):    
        win = True   
    elif(board[4] == board[5] and board[5] == board[6] and board[4] != ' '):    
        won = True    
    elif(board[7] == board[8] and board[8] == board[9] and board[7] != ' '):    
        win = True    
    #Vertical Winning Condition    
    elif(board[1] == board[4] and board[4] == board[7] and board[1] != ' '):    
        win = True    
    elif(board[2] == board[5] and board[5] == board[8] and board[2] != ' '):    
        win = True    
    elif(board[3] == board[6] and board[6] == board[9] and board[3] != ' '):    
        win = True    
    #Diagonal Winning Condition    
    elif(board[1] == board[5] and board[5] == board[9] and board[5] != ' '):    
        win = True    
    elif(board[3] == board[5] and board[5] == board[7] and board[5] != ' '):    
        win = True    
    #Match Draw Condition    
##    elif(board[1]!=' ' and board[2]!=' ' and board[3]!=' ' and board[4]!=' ' and board[5]!=' ' and board[6]!=' ' and board[7]!=' ' and board[8]!=' ' and board[9]!=' '):    
##        win = True

    return win

#Start Game


def main ():
    turn = True
    game = True
    printBoard()
    while(game):
        if(turn):
            move = int(input("Player One, please enter the position between [1-9] where you want to mark "))

            while(move>9 or move<1) or board[move]!=' ':
                move = int(input("That is an invalid move. Please enter a new move "))
            
            board[move] = 'X'
            printBoard()
            turn = False
            winner = CheckWin()
            turn_count.append(1)

            if(winner):
                print("X Wins!")
                
                game = False
            elif sum(turn_count) == 9:
                print('Game Drawn')
                game = False

        elif not(turn):
            move = int(input("Player two, please enter the position between [1-9] where you want to mark "))


            while(move>9 or move<1) or board[move]!=' ':
                move = int(input("That is an invalid move. Please enter a new move "))

                
            board[move] = 'O'
            printBoard()
            turn = True
            winner = CheckWin()
            turn_count.append(1)
            if(winner):
                print("O Wins!")
                game = False
            elif sum(turn_count) == 9:
                print('Game Drawn')
                game = False
        if not game:
            for x in range (0, len(board)-1):
                board[x] = ' '


main()