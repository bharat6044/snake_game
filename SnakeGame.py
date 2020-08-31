import pygame
import random
import math

fruitx = random.randint(10, 1180)
fruity = random.randint(10, 770)

snakex = 1080
snakey = 460

snakex_change = 0
snakey_change = 0
bodyx_change = 0
bodyy_change = 0

fruit_eaten = 0
delay_time = 50

snake_body = []
length = 1
body_list = []
snake_head_pos_list = []
bb = []

m = 0
qq = 0
qw = 0
key_pressed = 0

screen = pygame.display.set_mode((1200, 800))

running = True

while running:

    screen.fill((0, 0, 0))

    pygame.time.delay(delay_time)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and key_pressed != pygame.K_DOWN:
                snakey_change = -10
                snakex_change = 0
                key_pressed = pygame.K_UP

            if event.key == pygame.K_DOWN and key_pressed != pygame.K_UP:
                snakey_change = 10
                snakex_change = 0
                key_pressed = pygame.K_DOWN

            if event.key == pygame.K_LEFT and key_pressed != pygame.K_RIGHT:
                snakex_change = -10
                snakey_change = 0
                key_pressed = pygame.K_LEFT

            if event.key == pygame.K_RIGHT and key_pressed != pygame.K_LEFT:
                snakex_change = 10
                snakey_change = 0
                key_pressed = pygame.K_RIGHT

    snakex += snakex_change
    snakey += snakey_change

    if snakex > 1120:
        snakex = 0
        snakey = snakey

    if snakex < 0:
        snakex = 1120
        snakey = snakey

    if snakey > 800:
        snakey = 0
        snakex = snakex

    if snakey < 0:
        snakey = 800
        snakex = snakex

    bb.append(snakex)
    bb.append(snakey)
    snake_head_pos_list.append(bb)
    bb = []

    pygame.draw.rect(screen, (128, 58, 45), (fruitx, fruity, 16, 16))
    pygame.draw.rect(screen, (238, 44, 130), (snakex, snakey, 16, 16))

    for x in range(0,len(snake_body)+1):
        body_pos = snake_head_pos_list[(-1-x)]
        pygame.draw.rect(screen, (238, 44, 130), (body_pos[0], body_pos[1], 16, 16))


    if math.sqrt(abs((fruity - snakey) ** 2) + abs((fruitx - snakex) ** 2)) <= 10:
        length += 1
        fruit_eaten += 1

        body_list.append(snakex)
        body_list.append(snakey)

        snake_body.append(body_list)
        print(snake_body)

        body_list = []

        fruitx = random.randint(10, 1180)
        fruity = random.randint(10, 780)

        pygame.draw.rect(screen, (128, 58, 45), (fruitx, fruity, 16, 16))

        # if fruit_eaten == 1:
        #     delay_time -= 2
        #     fruit_eaten = 0

    pygame.display.update()


