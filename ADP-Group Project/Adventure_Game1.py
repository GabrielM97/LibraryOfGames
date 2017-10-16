# Kat Swannell s6298435
# Adventurer Wanted - The Boardom Blasters

import time
import random

game_on = True
ticket_number = 0
count = 0

# Printing the opening script with pauses in between each statement document.
def opening_script():
    opening = " "
    with open("opening.txt",mode="r") as file:
        for line in file:
            opening = opening + line
    print(opening)
    time.sleep(1)
    print(" ")
    enter = input("Press return key to continue...")
    opening_1 = " "
    with open("opening_1.txt",mode="r") as file:
        for line in file:
            opening_1 = opening_1 + line
    print(opening_1)
    time.sleep(1)
    print(" ")
    enter = input("Press return key to continue...")
    print(" ")

# Asks the player if they want to play. If the player agrees the game then
# randomly selects a number from 1-100 which becomes the players ticket number
# If the player declines, the player will be asked one more time and if answer
# remains as 'no', the game is over.
def player_draw():
    global ticket_number
    global game_on
    decision = input("Do you draw a ticket? Please type 'yes' or 'no':").lower()
    if decision == "yes":
        ticket_number = random.randint(1,100)
        print("Your fingers fumble as you unfold the ticket. The street")
        print("caller roughly takes the paper from you and declares to the ")
        print("gathered crowd that your number is ", ticket_number)
    elif decision == "no":
        print("Street Caller:   Ya sure about that? It's an opportunity", \
              "not to be missed!")
        print("                 I can't hang around here all day... Are", \
              " you taking a ")
        print("                 ticket or not?")
        print(" ")
        decision = input("Please type 'yes' or 'no': ")
        if decision == "yes":
            print("Your fingers fumble as you unfold the ticket. The ", \
                  "street caller roughly takes the paper from you and", \
                  "declares to the gathered crowd that your number is ", \
                  ticket_number)    
            print("The caller exclaims that the number you drew was ", \
                   ticket_number)
        else:
            print("Street Caller:   Aah... too bad. I thought you ", \
                  "could've been a winner.")
            print("                 Well, have a good day.")
            print(" ")
            print("You walk away, wondering what could have been.")
            print("Game Over")
            game_on = False
    else:
        print("Street Caller:   Come on now, I don't have time to mess ")
        print("about. Do you want to draw a number or not?")
        decision = input("Please type 'yes' or 'no': ")
        if decision == "yes":
            ticket_number = random.randint(1,100)
            print("Hesitantly reaching into the bucket, you pull out a ticket.")
            print("Your fingers fumble as you unfold the ticket. The street")
            print("caller roughly takes the paper from you and declares to")
            print("the gathered crowd that your number is ", ticket_number)
        elif decision == "no":
            print("Street Caller:   Ya sure about that? It's an opportunity", \
                  "not to be missed!")
            print("                 I can't hang around here all day... Are", \
                  " you taking a ")
            print("                 ticket or not?")
            print(" ")
            decision = input("Please type 'yes' or 'no': ")
            if decision == "yes":
                print("Your fingers fumble as you unfold the ticket.", \
                      "The street caller roughly takes the paper from ", \
                      "you and declares to the gathered crowd that ", \
                      "your number is ", ticket_number)
                print("The caller exclaims that the number you drew was ", \
                      ticket_number)
            else:
                print("Street Caller:   Aah... too bad. Thought you could've")
                print("                 been a winner.")
                print(" ")
                print("The street caller turned and carried on his business.")
                print(" ")
                print("You walk away, wondering what could have been.")
                print("Game Over")
                game_on = False
        else:
                print("Street Caller:   Aah... I don't have time to waste. ", \
                      "Too bad...  Thought you could've been a winner.")
                print(" ")
                print("The street caller turned and carried on his business.")
                print(" ")
                print("You walk away, wondering what could have been.")
                print("Game Over")
                game_on = False
    return ticket_number

# Reads scripts with some time delays allowing the player to read each 
# statement before the game prints another one.
def declaring_winner():
    waiting_in_crowd = " "
    with open("waiting_in_crowd.txt",mode="r") as file:
        for line in file:
            waiting_in_crowd = waiting_in_crowd + line
    print(waiting_in_crowd)
    time.sleep(1)
    print(" ")
    enter = input("Press return key to continue...")
    waiting_in_crowd_1 = " "
    with open("waiting_in_crowd_1.txt",mode="r") as file:
        for line in file:
            waiting_in_crowd_1 = waiting_in_crowd_1 + line
    print(waiting_in_crowd_1)
    time.sleep(1)
    print(" ")
    enter = input("Press return key to continue...")
    waiting_in_crowd_2 = " "
    with open("waiting_in_crowd_2.txt",mode="r") as file:
        for line in file:
            waiting_in_crowd_2 = waiting_in_crowd_2 + line
    print(waiting_in_crowd_2)
    time.sleep(1)
    print(" ")

    enter = input("Press return key to continue...")
    declare_winner = " "
    with open("declare_winner.txt",mode="r") as file:
        for line in file:
            declare_winner = declare_winner + line
    print(declare_winner)
    time.sleep(1)
    print(" ")
    enter = input("Press return key to continue...")
    print(" ")
    declare_winner_1 = " "
    with open("declare_winner_1.txt",mode="r") as file:
        for line in file:
            declare_winner_1 = declare_winner_1 + line
    print(declare_winner_1)
    time.sleep(1)
    print(" ")
    enter = input("Press return key to continue...")
    declare_winner_2 = " "
    with open("declare_winner_2.txt",mode="r") as file:
        for line in file:
            declare_winner_2 = declare_winner_2 + line
    print(declare_winner_2)
    time.sleep(1)
    print(" ")
    enter = input("Press return key to continue...")
    declare_winner_3 = " "
    with open("declare_winner_3.txt",mode="r") as file:
        for line in file:
            declare_winner_3 = declare_winner_3 + line
    print(declare_winner_3)
    time.sleep(1)
    print(" ")
    enter = input("Press return key to continue...")
    print(" ")
    
    print("Suited Man:   This is the moment we have all been waiting for...")
    print("              The holder of ticket number, ", ticket_number, "is")
    print("              our adventurer.")
    print(" ")

# Another script setting scene for the journey to the edge of the forest.
    winner_declared = " "
    with open("winner_declared.txt",mode="r") as file:
        for line in file:
            winner_declared = winner_declared + line
    print(winner_declared)
    time.sleep(1)
    print(" ")
    enter = input("Press return key to continue...")
    print(" ")
    print("                4 hours later. . .  ")
    print(" ")
    print(" ")

def entering_forest():
    forest_image = " "
    with open("ascii_forest.txt",mode="r") as file:
        for line in file:
            forest_image = forest_image + line
    print(forest_image)
    time.sleep(1)
    print(" ")
    enter = input("Press return key to continue...")
    entering_forest = " "
    with open("entering_forest.txt",mode="r") as file:
        for line in file:
            entering_forest = entering_forest + line
    print(entering_forest)
    time.sleep(1)
    print(" ")
    enter = input("Press return key to continue...")
    entering_forest_1 = " "
    with open("entering_forest_1.txt",mode="r") as file:
        for line in file:
            entering_forest_1 = entering_forest_1 + line
    print(entering_forest_1)
    time.sleep(1)
    print(" ")
    enter = input("Press return key to continue...")
    entering_forest_2 = " "
    with open("entering_forest_2.txt",mode="r") as file:
        for line in file:
            entering_forest_2 = entering_forest_2 + line
    print(entering_forest_2)
    time.sleep(1)
    print(" ")
    enter = input("Press return key to continue...")
    entering_forest_3 = " "
    with open("entering_forest_3.txt",mode="r") as file:
        for line in file:
            entering_forest_3 = entering_forest_3 + line
    print(entering_forest_3)
    time.sleep(1)
    print(" ")
    enter = input("Press return key to continue...")
    entering_forest_4 = " "
    with open("entering_forest_4.txt",mode="r") as file:
        for line in file:
            entering_forest_4 = entering_forest_4 + line
    print(entering_forest_4)
    time.sleep(1)
    print(" ")
    enter = input("Press return key to continue...")
    cave_entrance = " "
    with open("ascii_cave_entrance.txt",mode="r") as file:
        for line in file:
            cave_entrance = cave_entrance + line
    print(cave_entrance)
    time.sleep(1)
    print(" ")
    enter = input("Press return key to continue...")

def entering_cave():
    entering_cave = " "
    with open("entering_cave.txt",mode="r") as file:
        for line in file:
            entering_cave = entering_cave + line
    print(entering_cave)
    time.sleep(1)
    print(" ")
    enter = input("Press return key to continue...")
         
def first_puzzle():
    presented_riddle = random.randint(0,2)
    print("Your first puzzle is a riddle. Can you answer the following?")
    global game_on
            
    if presented_riddle == 0:
        count = 0
        riddle_0_answer = input("What has a mouth but no tongue? ").lower()

        print(riddle_0_answer)
        if riddle_0_answer == "cave":
            print("The barrier disintegrates before your eyes")
        while riddle_0_answer != "cave":
            print("YOU WERE WRONG! You can only try 3 times.. heh heh heh!")
            if count == 2:
                game_on = False
                print("Game Over")
                break
            riddle_0_answer = input("What has a mouth but no tongue? ").lower()
            
            if riddle_0_answer == "cave":
                print("The barrier disintegrates before your eyes")
            else:
                count += 1

    elif presented_riddle == 1:
        count = 0
        riddle_1_answer = input("What comes down but never goes up? ").lower()

        print(riddle_1_answer)
        if riddle_1_answer == "rain":
            print("The barrier disintegrates before your eyes")
        while riddle_1_answer != "rain" :
            print("YOU WERE WRONG! You can only try 3 times.. heh heh heh!")
            if count == 2:
                game_on = False
                print("Game Over")
                break
            riddle_1_answer = input("What comes down but never goes up? ").lower()
            if riddle_1_answer == "rain":
                print("The barrier disintegrates before your eyes")

            else:
                count += 1
                
    else:
        count = 0
        riddle_2_answer = input("What's so delicate that saying its name breaks it? ").lower()
        print(riddle_2_answer)
        if riddle_2_answer == "silence":
            print("The barrier disintegrates before your eyes")
        while riddle_2_answer != "silence" :
            print("YOU WERE WRONG! You can only try 3 times.. heh heh heh!")
            if count == 2:
                game_on = False
                print("Game Over")
                break
            riddle_2_answer = input("What is so delicate that saying its ", \
                                    "name breaks it? ").lower()
            if riddle_2_answer == "silence":
                print("The barrier disintegrates before your eyes")
            else:
                count += 1

def second_puzzle():
    guess_ascii_image = random.randint(0,2)
    print("The next challenge is to name the character. Can you guess", \
          "correctly?")
    
    global game_on
    if guess_ascii_image == 0:
        count = 0
        ascii_mona_lisa = " "
        with open("ascii_mona_lisa.txt",mode="r") as file:
            for line in file:
                ascii_mona_lisa = ascii_mona_lisa + line
        print(ascii_mona_lisa)
        time.sleep(1)
        print(" ")
    
        guess_ascii_image_0 = input("Guess who... please input ---- ----: ").lower()
        print(guess_ascii_image_0)
        if guess_ascii_image_0 == "mona lisa":
            print("The second barrier disintegrates before your eyes")
        while guess_ascii_image_0 != "mona lisa" :
            print("YOU WERE WRONG! You can only try 3 times.. heh heh heh!")
            if count == 2:
                game_on = False
                print("Game Over")
                break
            guess_ascii_image_0 = input("Guess who... please input ---- ----: ").lower()
            
            if guess_ascii_image_0 == "cave":
                print("The second barrier disintegrates before your eyes")
            else:
                count += 1
             
    if guess_ascii_image == 1:
        count = 0
        ascii_mickey_mouse = " "
        with open("ascii_mickey_mouse.txt",mode="r") as file:
            for line in file:
                ascii_mickey_mouse = ascii_mickey_mouse + line
        print(ascii_mickey_mouse)
        time.sleep(1)
        print(" ")
    
        guess_ascii_image_1 = input("Guess who... please input ----- -----: ").lower()
        print(guess_ascii_image_1)
        if guess_ascii_image_1 == "mickey mouse":
            print("The second barrier disintegrates before your eyes")
        while guess_ascii_image_1 != "mickey mouse" :
            print("YOU WERE WRONG! You can only try 3 times.. heh heh heh!")
            if count == 2:
                game_on = False
                print("Game Over")
                break
            guess_ascii_image_1 = input("Guess who... please input -----: ").lower()
            
            if guess_ascii_image_1 == "mickey mouse":
                print("The second barrier disintegrates before your eyes")
            else:
                count += 1

    else:
        count = 0
        ascii_homer = " "
        with open("ascii_homer.txt",mode="r") as file:
            for line in file:
                ascii_homer = ascii_homer + line
        print(ascii_homer)
        time.sleep(1)
        print(" ")
    
        guess_ascii_image_2 = input("Guess who... please input -----: ").lower()
        print(guess_ascii_image_2)
        if guess_ascii_image_2 == "homer":
            print("The second barrier disintegrates before your eyes")
        while guess_ascii_image_2 != "homer" :
            print("YOU WERE WRONG! You can only try 3 times.. heh heh heh!")
            if count == 2:
                game_on = False
                print("Game Over")
                break
            guess_ascii_image_2 = input("Guess who... please input -----: ").lower()
            
            if guess_ascii_image_2 == "homer":
                print("The second barrier disintegrates before your eyes")
            else:
                count += 1

def third_puzzle():
    number_base_challenge = random.randint(0,2)
    print("The final puzzle is relating to number bases.. Let's test your", \
          "knowledge!")
    global game_on
            
    if number_base_challenge == 0:
        count = 0
        challenge_0_answer = input("In binary, what does '1101' represent? ").lower()

        print(challenge_0_answer)
        if challenge_0_answer == "13":
            print("The final barrier disintegrates before your eyes")
        while challenge_0_answer != "13":
            print("YOU WERE WRONG! You can only try 3 times.. heh heh heh!")
            if count == 2:
                game_on = False
                print("Game Over")
                break
            challenge_0_answer = input("In binary, what does '1101' represent? ").lower()
            
            if challenge_0_answer == "13":
                print("The final barrier disintegrates before your eyes")
            else:
                count += 1

    elif number_base_challenge == 1:
        count = 0
        challenge_1_answer = input("In denary, how is number twenty represented? ").lower()

        print(challenge_1_answer)
        if challenge_1_answer == "20":
            print("The final barrier disintegrates before your eyes")
        while challenge_1_answer != "rain" :
            print("YOU WERE WRONG! You can only try 3 times.. heh heh heh!")
            if count == 2:
                game_on = False
                print("Game Over")
                break
            challenge_1_answer = input("In denary, how is number twenty represented? ").lower()
            if challenge_1_answer == "20":
                print("The final barrier disintegrates before your eyes")

            else:
                count += 1
                
    else:
        count = 0
        challenge_1_answer = input("In hexadecimal, how is number 15 represented? ").lower()

        print(challenge_1_answer)
        if challenge_1_answer == "e":
            print("The final barrier disintegrates before your eyes")
        while challenge_1_answer != "e" :
            print("YOU WERE WRONG! You can only try 3 times.. heh heh heh!")
            if count == 2:
                game_on = False
                print("Game Over")
                break
            challenge_1_answer = input("In hexadecimal, how is number 15 represented? ").lower()
            if challenge_1_answer == "e":
                print("The final barrier disintegrates before your eyes")

            else:
                count += 1

def end_game():
    print("You win and find gems, gold and riches!")
    print("Congratulations!")
    game_on = False


## Main Game Loop
while game_on:
    opening_script()
    player_draw()
    declaring_winner()
    entering_forest()
    entering_cave()
    first_puzzle()
    second_puzzle()
    third_puzzle()
    end_game()



