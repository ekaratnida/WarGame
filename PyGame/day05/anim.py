import pygame
 
SIZE = WIDTH, HEIGHT = 600, 400 
BACKGROUND_COLOR = pygame.Color('white') 
FPS = 10

class MySprite(pygame.sprite.Sprite):
    def __init__(self):
            super(MySprite, self).__init__()
            self.images = []
            self.images.append(pygame.image.load('day5/Sprites/images/walk1.png'))
            self.images.append(pygame.image.load('day5/Sprites/images/walk2.png'))
            self.images.append(pygame.image.load('day5/Sprites/images/walk3.png'))
            self.images.append(pygame.image.load('day5/Sprites/images/walk4.png'))
            self.images.append(pygame.image.load('day5/Sprites/images/walk5.png'))
            self.images.append(pygame.image.load('day5/Sprites/images/walk6.png'))
            self.images.append(pygame.image.load('day5/Sprites/images/walk7.png'))
            self.images.append(pygame.image.load('day5/Sprites/images/walk8.png'))
            self.images.append(pygame.image.load('day5/Sprites/images/walk9.png'))
            self.images.append(pygame.image.load('day5/Sprites/images/walk10.png'))

            for i in range(len(self.images)):
                self.images[i] = pygame.transform.scale(self.images[i], (100,120))

            self.index = 0
            self.image = self.images[self.index]
            self.rect = pygame.Rect(5,5,150,198)
    
    def moveRight(self, pixels):
        self.rect.x += pixels
 
    def moveLeft(self, pixels):
        self.rect.x -= pixels
    
    def moveForward(self, speed):
        self.rect.y += speed * speed/10
 
    def moveBack(self, speed):
        self.rect.y -= speed * speed/10
 
    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
       
def main():
     pygame.init()
     screen = pygame.display.set_mode(SIZE)
     my_sprite = MySprite()
     my_group = pygame.sprite.Group(my_sprite)
     clock = pygame.time.Clock()
     run = True
     while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            my_sprite.moveLeft(10)
        if keys[pygame.K_RIGHT]:
            my_sprite.moveRight(10)
        if keys[pygame.K_DOWN]:
            my_sprite.moveForward(10)
        if keys[pygame.K_UP]:
            my_sprite.moveBack(10)
        
        my_group.update()
        screen.fill(BACKGROUND_COLOR)
        my_group.draw(screen)
        pygame.display.update()
        clock.tick(10)

if __name__ == '__main__':
    main()
