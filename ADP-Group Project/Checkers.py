import pygame
pygame.init()

display = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Checkers")

# Initial Variables
black = [0, 0, 0]
white = [255, 255, 255]
blue = [0, 0, 120]
red = [120, 0, 0]
green = [0, 120, 0]
blue_light = [0, 0, 255]
red_light = [255, 0, 0]
green_light = [0, 555, 0]
teal = [97, 216, 245]
control_blue = [122, 200, 255]
game_in_progress = False
menu_back = pygame.image.load("checkers.png")
menu = ["start"]


def mouse():

    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()

    return mouse_pos, mouse_click


def buttons(num_of_buttons, x, y, height, width, colour, colour2, options, types):

    mouse_pos, click = mouse()
    count = num_of_buttons
    for button_on_screen in range(0, num_of_buttons):

        if x + height > mouse_pos[0] > x and y + width > mouse_pos[1] > y:
            pygame.draw.rect(display, colour, [x, y, height, width])

            for button_click in range(0, num_of_buttons):
                if click[0] == 1 and button_on_screen == (num_of_buttons - count):

                    print(options[button_on_screen])
                    return options[button_on_screen]

        elif type == 1:
            pygame.draw.rect(display, colour2, [x, y, height, width])

        y += 70
        count -= 1


def start_page():
    display.blit(menu_back, (0,0))


def main():
    while True:
        start_page()
        choice = buttons(1, 300, 300, 400, 60, red_light, black, menu, 0)
        pygame.display.update()


main()