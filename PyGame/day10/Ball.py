import random
import pygame 
class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speedX = random.randint(1, 4)  # Random speed for variation
        self.radius = random.randint(10,30) #BALL_RADIUS

    def update(self):
        self.y += self.speedX

    def draw(self, surface):
        pygame.draw.circle(surface, (255,0,0), (self.x, self.y), self.radius)

    def check_collision(self, player):
        return player.rect.colliderect(pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2))
