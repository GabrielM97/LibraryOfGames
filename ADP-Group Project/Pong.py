import pygame
import  time
import runpy
pygame.init()

pong_display = pygame.display.set_mode((800, 600))
objects = [0, 0, 0]
control = [0, 0, False, 20, 20]
ball_pos = [400, 150]
score = [0, 0]
# colours
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
clock = pygame.time.Clock()


def SFX ():
    effect = pygame.mixer.Sound('Pong Sound Effect #3.ogg')
    effect.play()


def point():
    effect = pygame.mixer.Sound('Pong Sound Effect #2.ogg')
    effect.play()


def print_scores():
    score_font = pygame.font.SysFont(None, 60)

    score_p1 = score_font.render(str(score[0]), True, white)
    pong_display.blit(score_p1, [325, 30])

    score_p2 = score_font.render(str(score[1]), True, white)
    pong_display.blit(score_p2, [450, 30])

    pygame.display.update()


def graphics(right_p, left_p, ball_x, ball_y):
    pong_display.fill(black)
    left_paddle = pygame.draw.rect(pong_display, white, [20, left_p, 20, 150])  # left paddle
    right_paddle = pygame.draw.rect(pong_display, white, [760, right_p, 20, 150])  # right paddle
    pygame.draw.line(pong_display, white, (400, 0), (400, 600), 4)

    ball = pygame.draw.circle(pong_display, white, (ball_x, ball_y), 10, 10)

    objects[0] = left_paddle
    objects[1] = right_paddle
    objects[2] = ball
    pygame.display.update()


def win():
    msg = pygame.font.SysFont(None, 60)
    if score[0] == 11:
        pong_display.fill(black)
        win_msg = msg.render("Player 1 Wins!", True, white)
        pong_display.blit(win_msg, [280, 80])
        pygame.display.update()
        time.sleep(3)
        control[2] = False
        score[0] = 0
        score[1] = 0
    elif score[1] == 11:
        pong_display.fill(black)
        win_msg = msg.render("Player 2 Wins!", True, white)
        pong_display.blit(win_msg, [280, 80])
        pygame.display.update()
        time.sleep(3)
        control[2] = False
        score[0] = 0
        score[1] = 0


def controls():

    game_is_on = True
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                right_paddle_y = -20
                control[0] = right_paddle_y
            elif event.key == pygame.K_DOWN:
                right_paddle_y = 20
                control[0] = right_paddle_y
            elif event.key == pygame.K_w:
                left_paddle_y = -20
                control[1] = left_paddle_y
            elif event.key == pygame.K_s:
                left_paddle_y = 20
                control[1] = left_paddle_y

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                control[0] = 0
            elif event.key == pygame.K_DOWN:

                control[0] = 0
            elif event.key == pygame.K_w:

                control[1] = 0
            elif event.key == pygame.K_s:

                control[1] = 0

        if event.type == pygame.QUIT:
            game_is_on = False

        control[2] = game_is_on


def start_game():
    msg = pygame.font.SysFont(None, 60)
    msg2 = pygame.font.SysFont(None, 120)
    pong_display.fill(black)
    pygame.draw.rect(pong_display, white, [20, 250, 20, 150])
    pygame.draw.rect(pong_display, white, [760, 250, 20, 150])
    msg_start2 = msg2.render("PONG", True, red)
    pong_display.blit(msg_start2,[255, 80] )
    msg_start = msg.render("Press space to start", True, red)
    pong_display.blit(msg_start, [200, 200])
    pygame.display.update()

    while not control[2]:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    control[2]= True
            if event.type == pygame.QUIT:
                pygame.quit()

                quit()


def collision(right_p, left_p, ball_y_move, ball_x_move):

    ball = objects[2]
    l_paddle = objects[0]
    r_paddle = objects[1]

    if right_p < 0 or right_p >= 450:
        control[0] *= -1

    if left_p < 0 or left_p >= 450:
        control[1] *= -1

    if ball_y_move < 5 or ball_y_move >= 590:

        control[3] *= -1
    if ball_x_move < -10:

        ball_pos[0] = 400
        ball_pos[1] = 150
        score[1] += 1
        graphics(right_p, left_p, ball_pos[0], ball_pos[1])
        print_scores()
        time.sleep(1)

    elif ball_x_move >= 810:

        ball_pos[0] = 400
        ball_pos[1] = 150
        score[0] += 1
        graphics(right_p, left_p, ball_pos[0], ball_pos[1])
        print_scores()
        time.sleep(1)

    if ball.colliderect(r_paddle) or ball.colliderect(l_paddle):
        SFX()
        control[4] *= -1


def main():

    FPS = 25
    right_p = 240
    left_p = 240
    start_game()
    game_on = control[2]
    while game_on:

        controls()
        right_p += control[0]
        left_p += control[1]
        graphics(right_p, left_p, ball_pos[0], ball_pos[1])
        collision(right_p, left_p, ball_pos[1], ball_pos[0])
        print_scores()
        ball_pos[1] += control[3]
        ball_pos[0] += control[4]
        win()
        game_on = control[2]
        clock.tick(FPS)
    runpy.run_path("Menu.py")

    pygame.quit()

    quit()

main()