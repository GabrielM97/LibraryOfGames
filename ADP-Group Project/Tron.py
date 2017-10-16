import pygame
import random
import time
import runpy
pygame.init()

clock = pygame.time.Clock()
tron_display = pygame.display.set_mode((800, 600))

black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255, 255, 255)

pygame.display.set_caption("TRON")
p1_lb = pygame.image.load('P1Bike.png')
p2_lb = pygame.image.load('P2Bike.png')
power_ups = pygame.image.load('powerup.png')

walls = []
direction = "down"
direction2 = "down"
bikes = []
bikes1 = []
gamestate = [True]
power = []
move = [10]


def maps():
    tron_display.fill(black)

    top = pygame.draw.rect(tron_display, blue,[0, 0, 800, 20])
    walls.append(top)
    bot = pygame.draw.rect(tron_display, blue, [0, 580, 800, 20])
    walls.append(bot)
    left = pygame.draw.rect(tron_display, blue, [0, 0, 20, 800])
    walls.append(left)
    right = pygame.draw.rect(tron_display, blue, [780, 0, 20, 800])
    walls.append(right)


def directions():
    if direction == "right":
        head = pygame.transform.rotate(p1_lb, 270)
    if direction == "left":
        head = pygame.transform.rotate(p1_lb, 90)
    if direction == "up":
        head = pygame.transform.rotate(p1_lb, 360)
    if direction == "down":
        head = pygame.transform.rotate(p1_lb, 180)

    if direction2 == "right":
        head2 = pygame.transform.rotate(p2_lb, 270)
    if direction2 == "left":
        head2 = pygame.transform.rotate(p2_lb, 90)
    if direction2 == "up":
        head2 = pygame.transform.rotate(p2_lb, 360)
    if direction2 == "down":
        head2 = pygame.transform.rotate(p2_lb, 180)

    return head, head2


def light_bike_1(bike_1, bike_2):
        game = True
        p1_bike = pygame.draw.rect(tron_display, blue, [1800, 10, 10, 10])
        p2_bike = pygame.draw.rect(tron_display, red, [1800, 10, 10, 10])

        body1, body2 = directions()

        tron_display.blit(body1, ((bike_1[-1][0])-5, (bike_1[-1][1])))
        tron_display.blit(body2, ((bike_2[-1][0])-5, (bike_2[-1][1])))

        for XnY in bike_1[:-1]:

            p1_bike = pygame.draw.rect(tron_display, blue, [XnY[0], XnY[1], 10, 10])
            bikes.append(p1_bike)

        for XY in bike_2[:-1]:

            p2_bike = pygame.draw.rect(tron_display, red, [XY[0], XY[1], 10, 10])
            bikes1.append(p2_bike)

        for count in range(0, len(bikes)-2):

            if p1_bike.colliderect(bikes[count]):
                msg_to_display("Red Wins", red,100)
                game = False
            if p2_bike.colliderect(bikes[count]):
                msg_to_display("Blue Wins", blue,100)

                game = False

        for count in range(0, len(bikes1)-2):

            if p2_bike.colliderect(bikes1[count]):
                msg_to_display("Blue Wins", blue,100)
                game = False
            if p1_bike.colliderect(bikes1[count]):
                msg_to_display("Red Wins", red,100)

                game = False

        for wall in walls:

            if p2_bike.colliderect(wall) and p1_bike.colliderect(wall):
                msg_to_display("draw", red, 100)
                game = False
            elif p1_bike.colliderect(wall):
                msg_to_display("Red Wins", red, 100)
                game = False
                print("blue")
            elif p2_bike.colliderect(wall):
                print("red")
                msg_to_display("Blue Wins", blue, 100)
                game = False

        gamestate[0] = game


def msg_to_display(msg, colour, size):
    tron_display.fill(black)
    font = pygame.font.SysFont(None, size)
    screen_text = font.render(msg, True, colour)
    tron_display.blit(screen_text, [250, 250])
    pygame.display.update()
    pygame.time.delay(50)


def start_game():
    game_start = False
    print ("hello")
    msg = pygame.font.SysFont(None, 60)
    msg2 = pygame.font.SysFont(None, 120)
    tron_display.fill(black)

    msg_start2 = msg2.render("Tron", True, red)
    tron_display.blit(msg_start2,[300, 80])
    msg_start = msg.render("Press space to start", True, red)
    tron_display.blit(msg_start, [200, 200])
    pygame.display.update()

    while not game_start:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_start= True
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


def main():

    game_on = True
    p1_lead_x_change = 0
    p1_lead_y_change = 10
    p1_lead_x = 400
    p1_lead_y = 100
    p2_lead_x_change = 0
    p2_lead_y_change = 10
    p2_lead_x = 350
    p2_lead_y = 100
    bike_movement = 10
    global direction
    global direction2
    bike_1 = []
    bike_2 = []
    start_game()
    while game_on:

        for event in pygame.event.get():  # pygame.event.get uses build in event handling
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and p1_lead_x_change == 0:
                    p1_lead_x_change = -bike_movement
                    p1_lead_y_change = 0
                    direction = "left"
                elif event.key == pygame.K_RIGHT and p1_lead_x_change == 0:
                    p1_lead_x_change = bike_movement
                    p1_lead_y_change = 0
                    direction = "right"
                elif event.key == pygame.K_UP and p1_lead_y_change == 0:
                    p1_lead_y_change = -bike_movement
                    p1_lead_x_change = 0
                    direction = "up"
                elif event.key == pygame.K_DOWN and p1_lead_y_change == 0:
                    p1_lead_y_change = bike_movement
                    p1_lead_x_change = 0
                    direction = "down"

                if event.key == pygame.K_d and p2_lead_x_change == 0:
                    p2_lead_x_change = bike_movement
                    p2_lead_y_change = 0
                    direction2 = "left"
                elif event.key == pygame.K_a and p2_lead_x_change == 0:
                    p2_lead_x_change = -bike_movement
                    p2_lead_y_change = 0
                    direction2 = "right"
                elif event.key == pygame.K_w and p2_lead_y_change == 0:
                    p2_lead_y_change = -bike_movement
                    p2_lead_x_change = 0
                    direction2 = "up"
                elif event.key == pygame.K_s and p2_lead_y_change == 0:
                    p2_lead_y_change = bike_movement
                    p2_lead_x_change = 0
                    direction2 = "down"

            if event.type == pygame.QUIT:  # event handling for quiting the game
                gamestate[0] = False

        game_on = gamestate[0]
        if not game_on:
            break
        maps()

        p1_lead_x += p1_lead_x_change
        p1_lead_y += p1_lead_y_change
        p2_lead_x += p2_lead_x_change
        p2_lead_y += p2_lead_y_change

        main_bike = [p1_lead_x, p1_lead_y]
        main_bike_2 = [p2_lead_x, p2_lead_y]
        bike_2.append(main_bike_2)
        bike_1.append(main_bike)

        light_bike_1(bike_1, bike_2)

        pygame.display.update()
        clock.tick(15)

    tron_display.fill(black)
    pygame.display.update()
    runpy.run_path("Menu.py")
    pygame.quit()

    quit()


main()

