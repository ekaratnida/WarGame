import pygame

pygame.init()



screen = pygame.display.set_mode((800, 600))

rect_x, rect_y = 400, 300

running = True



while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:

                rect_x -= 20

            elif event.key == pygame.K_RIGHT:

                rect_x += 20

   

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (255, 0, 0), (rect_x, rect_y, 50, 50))

    pygame.display.flip()



pygame.quit()