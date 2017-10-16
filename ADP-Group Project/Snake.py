import pygame
import random
import time

import runpy
pygame.mixer.pre_init(44100, -16, 2, 2048)
# Frameworks for pygame
pygame.init()
# colour must be set using their RGB values
#         R    G    B
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 100, 0)
light_green = (0, 155, 0)
orange = (255, 159, 82)
high_score = [0]
display_width = 800
display_height = 600
walls = []
gameDisplay = pygame.display.set_mode((display_width, display_height))
# sets a surface display
# parameters must be either a list or tuple.
# gameDisplay is surface
# pygame.display.flip()
# flip updates everything
# pygame.update()
# updates the display for a parameter.
pygame.display.set_caption("Snake_test")
clock = pygame.time.Clock()  # allows for and FPS rate to be set

block_size = 10
font = pygame.font.SysFont(None, 30)


def play_music():
    pygame.mixer.music.load('Snake - Main Theme.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(.3)


def read_file():
    with open("HighScores Snake.txt", mode="r") as my_file:
        for line in my_file:
            high_score.append(int(line))


def append_file(file_name, score):
    with open(file_name, mode="a") as my_file:
        my_file.write(str(score) + '\n')


def snake(snake_list):

    for XnY in snake_list:

        snakes = pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], block_size, block_size])

    return snakes


def print_hs():
    new_font = pygame.font.SysFont(None, 60)
    score_font = pygame.font.SysFont(None, 40)
    read_file()
    x = 230
    y = 150
    highScore = new_font.render("HIGH SCORES", True, black)
    gameDisplay.blit(highScore, [220, 80])

    high_score.sort(reverse=True)
    print(high_score)

    for count in range(0, 8):
        scores = score_font.render(str(high_score[count]), True, black)
        gameDisplay.blit(scores, [x, y])

        y += 30


def msg_to_display(msg, colour, x, y):
    screen_text = font.render(msg, True, colour)
    gameDisplay.blit(screen_text, [x, y])


def message_to_screen(msg, colour):
    screen_text = font.render(msg, True, colour)
    gameDisplay.blit(screen_text, [200, 450])


def scoring(msg, colour):

    screen_text = font.render(msg, True, colour)
    gameDisplay.blit(screen_text, [700, 35])


def pop_screen():
    # left walls
    lw1 = pygame.draw.rect(gameDisplay, orange, [0, 0, 20, 220])
    walls.append(lw1)
    lw2 = pygame.draw.rect(gameDisplay, orange, [0, 375, 20, 245])
    walls.append(lw2)
    # right walls
    rw1 = pygame.draw.rect(gameDisplay, orange, [780, 0, 20, 220])
    walls.append(rw1)
    rw2 = pygame.draw.rect(gameDisplay, orange, [780, 375, 20, 245])
    walls.append(rw2)

    # up walls
    uw1 = pygame.draw.rect(gameDisplay, orange, [0, 0, 300, 20])
    walls.append(uw1)
    uw2 = pygame.draw.rect(gameDisplay, orange, [500, 0, 300, 20])
    walls.append(uw2)

    # down walls
    dw1 = pygame.draw.rect(gameDisplay, orange, [0, 580, 300, 20])
    walls.append(dw1)
    dw2 = pygame.draw.rect(gameDisplay, orange, [500, 580, 300, 20])
    walls.append(dw2)

    # pillars

    p1 = pygame.draw.rect(gameDisplay, orange, [140, 250, 30, 100])
    walls.append(p1)
    p2 = pygame.draw.rect(gameDisplay, orange, [640, 250, 30, 100])
    walls.append(p2)
    p3 = pygame.draw.rect(gameDisplay, orange, [350, 90, 100, 30])
    walls.append(p3)
    p4 = pygame.draw.rect(gameDisplay, orange, [350, 480, 100, 30])
    walls.append(p4)


def get_fruit():
    effect = pygame.mixer.Sound('Coin Sound Effect.ogg')
    effect.play()
    effect.set_volume(.05)


def game_loop():
    FPS = 10
    lead_x_change = 0
    lead_y_change = 0
    game_start = True
    lead_x = display_width / 2
    lead_y = display_height / 2

    snake_list = []
    snake_length = 3
    game_is_on = True
    game_over = False

    rand_apple_x = round(random.randrange(30, (display_width-100) - block_size*2)/10.0)*10.0
    rand_apple_y = round(random.randrange(30, (display_height-100) - block_size*2)/10.0)*10.0
    which_apple = random.randrange(0, 6)
    print(which_apple)

    score = 0
    apple = pygame.draw.rect(gameDisplay, red, [900, 300, block_size, block_size])
    big_apple = pygame.draw.rect(gameDisplay, red, [900, 700, 20, 20])
    del high_score[:]
    play_music()
    while game_is_on:
        # Events

        while game_start:

            gameDisplay.fill(light_green)
            pop_screen()
            msg_to_display("Press Space To Start", black, 300, 300)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        lead_y_change = 10
                        game_start = False
                if event.type == pygame.QUIT:  # event handling for quiting the game
                    game_is_on = False
                    game_start = False

        if game_over:
            append_file("HighScores Snake.txt", score)
            gameDisplay.fill(light_green)
            print_hs()
            message_to_screen("Game Over, press C to continue or Q to quit", black)
            pygame.display.update()

        while game_over:

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_is_on = False
                        game_over = False
                    if event.key == pygame.K_c:
                        game_loop()
                if event.type == pygame.QUIT:  # event handling for quiting the game
                    game_is_on = False
                    game_over = False

        for event in pygame.event.get():  # pygame.event.get uses build in event handling
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and lead_x_change == 0:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT and lead_x_change == 0:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP and lead_y_change == 0:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN and lead_y_change == 0:
                    lead_y_change = block_size
                    lead_x_change = 0

            if event.type == pygame.QUIT:  # event handling for quiting the game
                game_is_on = False

                #  logic

        if lead_x >= 800:
            lead_x = 0
        elif lead_x < 0:
            lead_x = 800
        elif lead_y > 600:
            lead_y = 0
        elif lead_y < 0:
            lead_y = 600

        lead_x += lead_x_change
        lead_y += lead_y_change

        # graphics
        gameDisplay.fill(light_green)
        pop_screen()

        if which_apple <= 4:
            apple = pygame.draw.rect(gameDisplay, red, [rand_apple_x, rand_apple_y, block_size, block_size])
            # gameDisplay.draw.rect(surface, colour, [x, y, width, height])
        elif which_apple > 4:
            big_apple = pygame.draw.rect(gameDisplay, red, [rand_apple_x, rand_apple_y, block_size*2, block_size*2])

        snake_head = [lead_x, lead_y]

        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        snaky = snake(snake_list)

        if lead_x == rand_apple_x and lead_y == rand_apple_y:
            rand_apple_x = round(random.randrange(30, (display_width-100) - block_size) / 10.0) * 10.0
            rand_apple_y = round(random.randrange(30, (display_height-100) - block_size) / 10.0) * 10.0
            which_apple = random.randrange(0, 6)
            get_fruit()
            snake_length += 1
            score += 5
        elif snaky.colliderect(big_apple):
            # if big_block == block_size*2:
            rand_apple_x = round(random.randrange(30, (display_width-100) - block_size*2) / 10.0) * 10.0
            rand_apple_y = round(random.randrange(30, (display_height-100) - block_size*2) / 10.0) * 10.0
            which_apple = random.randrange(0, 6)
            get_fruit()
            score += 10
            snake_length += 5

        for wall in walls:

            if apple.colliderect(wall):
                rand_apple_x = round(random.randrange(30, (display_width - 100) - block_size) / 10.0) * 10.0
                rand_apple_y = round(random.randrange(30, (display_height - 100) - block_size) / 10.0) * 10.0
                which_apple = random.randrange(0, 6)

            elif big_apple.colliderect(wall):
                rand_apple_x = round(random.randrange(30, (display_width - 100) - block_size * 2) / 10.0) * 10.0
                rand_apple_y = round(random.randrange(30, (display_height - 100) - block_size * 2) / 10.0) * 10.0
                which_apple = random.randrange(0, 6)

            if snaky.colliderect(wall):

                game_over = True

        for count in range(1, len(snake_list)):
            if snake_list[0][0] == snake_list[count][0] and snake_list[0][1] == snake_list[count][1]:

                game_over = True

        scoring(str(score), black)

        pygame.display.update()

        clock.tick(FPS)
    pygame.mixer.music.stop()
    gameDisplay.fill(black)
    pygame.display.update()


    pygame.quit()

    quit()

game_loop()
