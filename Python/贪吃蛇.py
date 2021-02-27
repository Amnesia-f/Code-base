import pygame
import sys
import time
import random
from pygame.locals import *

#
pygame.init()
size = width, height = 350, 350
screen = pygame.display.set_mode((size))
t = pygame.time.Clock()
snake_head = [110, 50]
snake_body = [[110, 50], [100, 50], [90, 50], [80, 50], [70, 50]]

foodx = random.randint(5, 30) * 10
foody = random.randint(5, 30) * 10


# fx = "RIGHT"
# while True:
#     t.tick(5)
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()
def Fx2():
    if event.type == KEYDOWN and event.key == K_LEFT:
        # snak_head[0] -=10
        global fx
        if fx != "RIGHT":
            fx = "LEFT"
    if event.type == KEYDOWN and event.key == K_RIGHT:
        # snak_head[0] -=10
        if fx != "LEFT":
            fx = "RIGHT"
    if event.type == KEYDOWN and event.key == K_DOWN:
        # snak_head[0] -=10
        if fx != "UP":
            fx = "DOWN"
    if event.type == KEYDOWN and event.key == K_UP:
        # snak_head[0] -=10
        if fx != "DOWN":
            fx = "UP"


def Move2():
    if fx == "RIGHT":
        snake_head[0] += 10
    if fx == "LEFT":
        snake_head[0] -= 10
    if fx == "DOWN":
        snake_head[1] += 10
    if fx == "UP":
        snake_head[1] -= 10


#
#     screen.fill((255, 255, 255))
#     # snak_head[0] += 10
#     print(snak_head)
#     snak_body.insert(0,list(snak_head))
#     snak_body.pop()
#     print(snak_body)
#     for i in snak_body:
#         pygame.draw.rect(screen,(0,0,0),(i[0],i[1],10,10))
#
#     pygame.display.update()


fx = "K_d"


def Fx():
    if event.type == KEYDOWN and event.key == K_w:
        # snake_head[1]-=10
        global fx
        if fx != "K_s":
            fx = "K_w"

    if event.type == KEYDOWN and event.key == K_a:
        # snake_head[0] -= 10
        if fx != "K_d":
            fx = "K_a"
    if event.type == KEYDOWN and event.key == K_s:
        # snake_head[1]+=10
        if fx != "K_w":
            fx = "K_s"
    if event.type == KEYDOWN and event.key == K_d:
        # snake_head[0]+=10
        if fx != "K_a":
            fx = "K_d"


def Rest():
    global fx, foody, foodx, snake_head, snake_body, score, kaiguan
    while True:
        event = pygame.event.poll()
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN and event.key == K_RETURN:
            fx = "K_d"
            snake_head = [110, 50]
            snake_body = [[110, 50], [100, 50], [90, 50], [80, 50], [70, 50]]

            foodx = random.randint(5, 30) * 10
            foody = random.randint(5, 30) * 10
            score = 0
            kaiguan = 0
            break


def Move():
    # global fx
    if fx == "K_a":
        snake_head[0] -= 10
    if fx == "K_d":
        snake_head[0] += 10
    if fx == "K_s":
        snake_head[1] += 10
    if fx == "K_w":
        snake_head[1] -= 10


def Fontf(mx, ziti, x, y):
    afont = pygame.font.Font(None, 40)
    bfont = afont.render(ziti, True, (255, 0, 0))
    screen.blit(bfont, (x, y))
    pygame.display.update()


def color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color1 = (r, g, b)
    return color1


list3 = []
for i in range(5):
    colors = color()
    list3.append(colors)
print(list3)

n = 0
score = 0
kaiguan = 0
while 1:
    n += 1
    t.tick(5)
    screen.fill((0, 0, 0))
    # colors = color()
    # list.append(colors)

    # print(colors)
    pygame.draw.rect(screen, (255, 0, 0), (foodx, foody, 10, 10))
    if snake_head == [foodx, foody]:
        foodx = random.randint(5, 30) * 10
        foody = random.randint(5, 30) * 10
        snake_body.append([-10, -10])
        score += 1

    Fontf(40, "score:" + str(score), 200, 0)
    if snake_head[0] <= -10 or snake_head[0] >= 400 or snake_head[1] <= -10 or snake_head[1] >= 400:
        kaiguan = 1
    if snake_head in snake_body[1:]:
        kaiguan = 1
    if kaiguan:
        Fontf(40, "you lose", 100, 150)
        # break
        Rest()
        # while True:
        #     event = pygame.event.poll()
        #     if event.type == QUIT:
        #         pygame.quit()
        #     if event.type == KEYDOWN and event.key == K_RETURN:
        #         fx = "K_d"
        #         snake_head = [110, 50]
        #         snake_body = [[110, 50], [100, 50], [90, 50], [80, 50], [70, 50]]
        #
        #         foodx = random.randint(5, 30) * 10
        #         foody = random.randint(5, 30) * 10
        #         score = 0
        #         kaiguan =0
        #         break

    for i in snake_body:
        pygame.draw.rect(screen, list3[n % 5], (i[0], i[1], 10, 10))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        Fx()

        # if event.type==KEYDOWN and event.key==K_w:
        #     # snake_head[1]-=10
        #     if fx !="K_s":
        #         fx = "K_w"
        #
        # if event.type == KEYDOWN and event.key == K_a:
        #     # snake_head[0] -= 10
        #     if fx !="K_d":
        #         fx = "K_a"
        # if event.type==KEYDOWN and event.key==K_s:
        #     # snake_head[1]+=10
        #     if fx !="K_w":
        #         fx = "K_s"
        # if event.type==KEYDOWN and event.key==K_d:
        #     # snake_head[0]+=10
        #     if fx !="K_a":
        #         fx = "K_d"

    # if fx == "K_a":
    #     snake_head[0]-=10
    # if fx == "K_d":
    #     snake_head[0]+=10
    # if fx == "K_s":
    #     snake_head[1]+=10
    # if fx == "K_w":
    #     snake_head[1]-=10
    # snake_head[0] += 10
    Move()

    snake_body.insert(0, list(snake_head))
    snake_body.pop()

    pygame.display.update()