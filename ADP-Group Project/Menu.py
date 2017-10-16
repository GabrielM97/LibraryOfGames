import pygame
import time
import runpy

pygame.init()
x = 800
y = 600
display = pygame.display.set_mode((x, y))
back = pygame.image.load('background.png')

black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
light_red = (155, 0, 0)
white = (255, 255, 255)
grey = (128,128,128)
boardemBlaster_memebers = ["Gabriel Menezes, ", "Kat Swannell, ", "Joe Muana, ", "Matthew Nicholas, ", "Camaron Turner"]
pygame.display.set_caption("Boredom Blasters Game Library")

Games = ["Connect 4", "Pong", "Snake", "Tron", "OXO", "Blackholes", "Mancala", "Adventure"]


def footer():
    adp_footer = "Agile Development Project, Boredom Blasters, Games by: "

    for name in boardemBlaster_memebers:
        adp_footer += name
    font = pygame.font.SysFont(None, 15)

    button_msg = font.render(adp_footer, True, white)
    display.blit(button_msg, [20, 580])


def close():
    menu_is_on = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu_is_on = False

    return menu_is_on


def text(i, x, y):
    font = pygame.font.SysFont(None, 30)

    button_msg = font.render(Games[i], True, black)
    display.blit(button_msg, [x+20, y+15])


def button(X, Y):
    global x
    global y
    display.blit(back, (0, 0))
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    for buttons in range(0, 8):

        if X + 150 > mouse[0] > X and Y + 50 > mouse[1] > Y:
            pygame.draw.rect(display, grey, [X, Y, 150, 50])
            text(buttons, X, Y)
            if click[0] == 1 and buttons == 0:
                runpy.run_path("Connect4.py")
            if click[0] == 1 and buttons == 1:
                runpy.run_path("Pong.py")
            if click[0] == 1 and buttons == 2:
                runpy.run_path("Snake.py")
            if click[0] == 1 and buttons == 3:
                runpy.run_path("Tron.py")
            if click[0] == 1 and buttons == 4:
                runpy.run_path("OXO.py")
            if click[0] == 1 and buttons == 5:
                runpy.run_path("Blackholes.py")
            if click[0] == 1 and buttons == 6:
                runpy.run_path("Mancala.py")
            if click[0] == 1 and buttons == 7:
                runpy.run_path("Adventure_game1.py")

        else:
            pygame.draw.rect(display, white, [X, Y, 150, 50])
            text(buttons, X, Y)

        Y += 70

        if Y >= 500:
            X += 170
            Y = 250

    footer()
    pygame.display.update()


def main():
    menu_on = True

    pygame.display.update()
    while menu_on:

        button(50, 250)
        menu_on = close()

    pygame.quit()
    quit()


main()