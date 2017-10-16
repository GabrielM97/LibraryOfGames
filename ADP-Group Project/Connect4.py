#Gabriel Menezes
#06/03/2017

BOARD = ["" for x in range(0, 72)]
WIDTH = 7
player_one = "X"
player_two = "O"


def draw_BOARD():
    # Builds and displays board
    print("")
    print("")
    for count in range(1, 8):
        BOARD[count] = count
    for x in range(1, 64):
        if x % WIDTH == 0:
            print((" ["), str(BOARD[x]).rjust(2, " "), " ]")
            print("-" * 56)
        else:
            print("[", str(BOARD[x]).rjust(2, " "), (" ]"), end=" ")


def play_move(player):
    # Allows the player to select in what row they will drop their marker
    print("player: ", player + 1)
    while True:
        try:  # try catch used to stop game from breaking should the player input be inconsistant with expectations..         
            print("Select a row to drop your marker into \nuse the numbers above the board between 1 and 7")
            which_row = int(input())
            if 1 < which_row > 7 or which_row == 0:  # basic error check for the correct range.
                print("Invalid input\nplease select from the numbers above the board between 1 and 7")
                which_row = int(input())
            if which_row >= 1 and which_row <= 7:  # condition to check for the correct input and break of out the try and loop..
                break
        except ValueError:  # catches any input that isnt a number and throws an exception rather then crash
            print("Error Invalid Input!")
            print("")
    return which_row


def valid_move(player, which_row):  # check the move is validand the marker can be places.
    col = 8
    if player == 0:
        while col != 0:
            board_pos = which_row + (col * WIDTH)
            if BOARD[which_row + WIDTH] != "":
                print("Invalid, row is full try another")
                which_row = int(input())
                col = 8
            elif BOARD[board_pos] == player_one or BOARD[board_pos] == player_two:
                col -= 1
            elif BOARD[board_pos] == "":
                BOARD[board_pos] = player_one

                col = 0

    if player == 1:
        while col != 0:
            board_pos = which_row + (col * WIDTH)
            if BOARD[which_row + WIDTH] != "":
                print("Invalid, row is full try another")
                which_row = int(input())
                col = 8
            elif BOARD[board_pos] == player_one or BOARD[board_pos] == player_two:
                col -= 1
            elif BOARD[board_pos] == "":
                BOARD[board_pos] = player_two
                col = 0
                
    return board_pos


def check_down(board_pos,player):
    marker_P1 = 1
    marker_P2 = 1
    markers = 0
    width = WIDTH
    
    if board_pos > 43:
        return markers
    
    print ("player",player)
    
    for count in range(0, 4):
        
        if player == 0:
            if BOARD[board_pos + width] == player_one:
                marker_P1 += 1
                width += 7
                markers = marker_P1
                print ("p1 ++")
        if player == 1:
            if BOARD[board_pos + width] == player_two:
                marker_P2 += 1
                width += 7
                markers = marker_P2
                print ("p2 ++")

    return markers


def check_left_right(board_pos, player):

    marker_P1 = 1
    marker_P2 = 1
    markers = 0
    row = (board_pos- 1)// WIDTH
    left_bound = row * WIDTH + 1
    right_bound = left_bound + WIDTH - 1
    
    print(row,left_bound,right_bound)

    for count in range(1, 4):
        if board_pos - count < left_bound and (BOARD[board_pos - count] == player_one) :
            print("checkin LB")
            break
        if board_pos - count < left_bound and (BOARD[board_pos - count] == player_two):
            print("checkin LB")
            break

        if board_pos + count > right_bound and (BOARD[board_pos + count] == player_one):
            print("check RB")
            break

        if board_pos + count > right_bound and (BOARD[board_pos + count] == player_two):
            print("check RB")
            break
        

        if player == 0:
            

            if BOARD[board_pos - count] == player_one:
                print("left check")
                marker_P1 += 1
                markers = marker_P1

            if BOARD[board_pos + count] == player_one and BOARD[board_pos + (count-1)] == player_one:
                print("right check")
                marker_P1 += 1
                markers = marker_P1
                
            if BOARD[board_pos - count] != player_one:
               
                break

        if player == 1:

            if BOARD[board_pos - count] == player_two:
                
                print("Doing left")
                marker_P2 += 1
                markers = marker_P2

            if BOARD[board_pos + count] == player_two and BOARD[board_pos + (count-1)] == player_two:

                print("Doing right")
                marker_P2 += 1
                markers = marker_P2
                
    return markers


def Diagonal_left(board_pos,player):
    
    marker_P1 = 1
    marker_P2 = 1
    markers = 0

    rows = (board_pos- 1)// WIDTH
    left_bound = rows * WIDTH + 1
    right_bound = left_bound + WIDTH - 1
    
    row = 1
    width = WIDTH
    

    print(rows,left_bound,right_bound)
    

    for count in range (1,4):


        if (board_pos + width) - row >63:
            break
        if board_pos== left_bound:
            break
        
       
        if (board_pos + width) - row == left_bound + (WIDTH * count) and BOARD[(board_pos + width) - row] == player_one:
            print("checkin LB")
            markers += 1
            break
        elif (board_pos + width) - row == left_bound + (WIDTH * count):
            break
 
        if player == 0:

            if BOARD[(board_pos + width) - row] == player_one:
                
                print("p1 left diag",(board_pos + width) - row)
                marker_P1 += 1
                markers = marker_P1
                row += 1
                width += 7
                
        if player == 1:
            
             if BOARD[(board_pos + width) - row] == player_two:
                
                print("p2 left diag",(board_pos + width) - row)
                marker_P2 += 1
                markers = marker_P2
                row += 1
                width += 7
                
    return markers


def Right_diagonal(board_pos,player):
     
    marker_P1 = 1
    marker_P2 = 1
    markers = 0

    rows = (board_pos- 1)// WIDTH
    left_bound = rows * WIDTH + 1
    right_bound = left_bound + WIDTH - 1
    
    row = 1
    width = WIDTH
    

    print(rows,left_bound,right_bound)
    

    for count in range (1,4):


        if (board_pos + width) - row > 63:
            break
        if board_pos == right_bound:
            break
        
    
 
        if (board_pos + width) + row == right_bound + (WIDTH * count) and BOARD[(board_pos + width) + row] == player_one:
            print("checkin LB")
            markers += 1
            break
        elif (board_pos + width) + row == right_bound + (WIDTH * count):
            break
 
        if player == 0:

            if BOARD[(board_pos + width) + row] == player_one:
                
                print("p1 right diag",(board_pos + width) + row)
                marker_P1 += 1
                markers = marker_P1
                row += 1
                width += 7
                
        if player == 1:
            
             if BOARD[(board_pos + width) + row] == player_two:
                
                print("p2 right diag",(board_pos + width) + row)
                marker_P2 += 1
                markers = marker_P2
                row += 1
                width += 7
                
    return markers



def Check_win(board_pos, player):  # check the if the player has 4 in a row and ends accordingly.

    markers_in_row = 0
    is_full = 0

    game_is_on = True
    

    markers_in_row = check_down(board_pos,player)

    if markers_in_row <4:
        markers_in_row = check_left_right(board_pos, player)
        
    if markers_in_row < 4:
        markers_in_row = Diagonal_left(board_pos,player)
        
    if markers_in_row < 4:
        markers_in_row = Right_diagonal(board_pos,player)
    for count in range (8,15):
        if (BOARD[count] == player_one):
            is_full += 1
        elif BOARD[count] == player_two:
            is_full += 1
        

    

    # when win condition is met show which player has won and end game

    if markers_in_row >= 4:
        game_is_on = False
        draw_BOARD()
        print("Game Over")
        print("Player", player + 1, "Wins!")
        
        for count in range(0, 72):
            BOARD[count] = ""
        
    elif is_full == 7:
        print ("Game is a draw!")
        game_is_on = False
        draw_BOARD()
        
  
        

    return game_is_on


def play_again():  # allows the player to play again if they wish too.
    print("Do you wish to play again ? Y/N")
    continues = input().lower()

    while continues != "y" and continues != "n":  # stops player from entering anything but a number
        print("Invalid input, please try again ")
        continues = input().lower()

    if continues == "y":
        for count in range(0, 72):
            BOARD[count] = ""

        Connect_4_Main()
    elif continues == "n":
        print("Game has Ended...")


def Connect_4_Main():
    player = 1
    game_on = True
    while game_on:
        player = (player + 1) % 2
        draw_BOARD()
        row = play_move(player)
        marker_pos = valid_move(player, row)
        game_on = Check_win(marker_pos, player)

    play_again()


Connect_4_Main()
