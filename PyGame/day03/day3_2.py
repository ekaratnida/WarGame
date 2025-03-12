import pygame
pygame.font.init()

WIDTH, HEIGH = 800, 600

screen = pygame.display.set_mode((WIDTH, HEIGH))
pygame.display.set_caption("MY Text")

font1 = pygame.font.SysFont("Arial", 800)

text1 = font1.render("KJ", True, (0, 255, 0))

textRect1 = text1.get_rect()
textRect1.center = (400, 300)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    screen.fill((255, 255, 255))
    screen.blit(text1, textRect1)

    pygame.display.update()

pygame.quit()



