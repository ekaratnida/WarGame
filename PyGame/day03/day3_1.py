import pygame
pygame.init()

WIDTH, HEIGH = 800, 600

screen = pygame.display.set_mode((WIDTH, HEIGH))
pygame.display.set_caption("MY game")

running = True
while running: #Game loop using “while” to control the activity of running the game.
    for event in pygame.event.get(): #Check events while running the game.
        if event.type == pygame.QUIT: #If a game screen close event occurs.
            running = False #Stop the loop
    screen.fill((255, 255, 0))  # White background
    pygame.display.flip() #updates the entire screen by swapping the display buffer.

pygame.quit() #End the game.
