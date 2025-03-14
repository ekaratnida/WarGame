import random
import pygame
class Enemy1:
    def __init__(self, x, y,width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speedX = random.randint(2, 5)  # Random speed for variation

    def update(self):
        self.x += self.speedX

    def draw(self, surface):
        pygame.draw.rect(surface, (0,255,0), (self.x,self.y,self.width,self.height))

    def check_collision(self, player):
        return player.rect.colliderect(pygame.Rect(self.x, self.y, self.width, self.height))
