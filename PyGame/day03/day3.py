import pygame
from pygame.locals import *
import random
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My PyGame")
running = True
r, g, b = 255, 255, 255
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
            colorList.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            sizeList.append(random.randint(20, 100))

    screen.fill((r, g, b))

    # Draw circles
    for pos, col, radius in zip(circleList, colorList, sizeList):
        pygame.draw.circle(screen, col, pos, radius)

    # Draw the large circle and polygon
    pygame.draw.circle(screen, (255, 255, 0), (300, 200), 85)
    if t % 2 == 0:
        pygame.draw.polygon(screen, (255, 255, 255), points=[(300, 200), (400, 150), (400, 250)])
    elif t % 2 == 1:
        pygame.draw.polygon(screen, (255, 255, 255), points=[(300, 200), (400, 190), (400, 210)])

    t += 1
    
    pygame.display.update()

    # Optional: Add a small delay for better visibility of changes
    pygame.time.delay(100)  # 100 ms delay (adjust as needed)

pygame.quit()
