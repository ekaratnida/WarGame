import pygame
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("My PyGame")
Icon = pygame.image.load("day1\logo.png")
pygame.display.set_icon(Icon)

running = True
r,g,b = 0,0,0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((r,g,b))
    
    pygame.draw.circle(screen,(255,0,0),(300,200),85)
    pygame.draw.circle(screen,(255,255,255),(300,200),75)
    pygame.draw.rect(screen,(255,255,255),(10,10,100,100))
    pygame.draw.ellipse(screen,(255,255,255),(10,110,80,120))
    pygame.draw.polygon(screen,(255,255,255),points=[(10,300),(200,300),(150,500)])
    pygame.draw.arc(screen,(255,255,0),(500,10,200,100),0,1.0,2)
    pygame.draw.line(screen,(255,255,255),(500,200),(300,400),width=3)
    pygame.draw.circle(screen,(0,255,0),(300,400),75,width=0)
    
    
    pygame.display.update()
    '''
    pygame.display.flip()
    pygame.time.delay(100)
    r+=10
    g+=20
    b+=30
    if r > 255:
        r = 0
    if g > 255:
        g = 0
    if b > 255:
        b = 0
    '''
pygame.quit()
