import pygame
import random
from time import time
#import pkg_resources.py2_warn

if __name__ == '__main__':

    pygame.init()
    win = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("first game")
    FPS = 60
    clock = pygame.time.Clock()

    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 30)

    x = 0
    y = 0
    w = 50
    h = 50
    v = 10

    x1 = random.randrange(500 - w)
    y1 = random.randrange(500 - h)

    punti = 0

    start_time = time()
    run = True
    while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and x > 0:
            x -= v
        if keys[pygame.K_RIGHT] and x < 500 - 50:
            x += v
        if keys[pygame.K_UP] and y > 0:
            y -= v
        if keys[pygame.K_DOWN] and y < 500 - 50:
            y += v

        end_time = time()
        if end_time - start_time >= 8:
            x1 = random.randrange(500 - w)
            y1 = random.randrange(500 - h)
            start_time = time()

        pygame.display.set_caption("punteggio: {}".format(punti))
        if x1 in range(x - v, x + v) and y1 in range(y - v, y + v):
            punti += 1
            x1 = random.randrange(500 - w)
            y1 = random.randrange(500 - h)

        win.fill((0, 0, 0))
        pygame.draw.rect(win, (255, 0, 0), (x, y, w, h))
        pygame.draw.rect(win, (0, 255, 0), (x1, y1, w, h))
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()