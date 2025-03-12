import pygame
from pygame.locals import *
import random
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("My PyGame")
running = True
r,g,b = 255,255,255
PI = 3.14
t = 0
circleList = []
colorList = []
sizeList = []
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == MOUSEBUTTONDOWN:
            position = event.pos
            circleList.append(position)
            colorList.append((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
            #??

    screen.fill((r,g,b))

    for pos,col in zip(circleList,colorList):
        pygame.draw.circle(screen,
                           col,
                           pos,
                           40)
    
    pygame.draw.circle(screen,(255,255,0),(300,200),85)
    if t%2 == 0:
        pygame.draw.polygon(screen,(255,255,255),points=[(300,200),(400,150),(400,250)])
    elif t%2 == 1:
        pygame.draw.polygon(screen,(255,255,255),points=[(300,200),(400,190),(400,210)])
    t=t+1
    #pygame.time.delay(500)
    pygame.display.update()
  
pygame.quit()