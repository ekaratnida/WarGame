import pygame
import sys
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Sheet Anim")

WHITE = (255,255,255)

class Player:
    def __init__(self,x,y):
        self.sprite_sheet = pygame.image.load("day06/caveman.png").convert_alpha()
        self.sprite_sheet = pygame.transform.scale(self.sprite_sheet,(512,128))
        self.frames = []
        self.frame_width = 128
        self.frame_height = 128
        self.total_frames = 4

        for i in range(self.total_frames):
            frame = self.get_frame(i)
            self.frames.append(frame)
        
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.animation_speed = 0.1 #เวลาระหว่าง frame
        self.animation_timer = 0

    def get_frame(self, frame_number):
        frame = pygame.Surface((self.frame_width, self.frame_height),pygame.SRCALPHA)
        frame.blit(
            self.sprite_sheet,
            (0,0),
            (frame_number*self.frame_width,0,self.frame_width,self.frame_height)
        )
        return frame

    def update(self, dt):
        self.animation_timer += dt
        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0
            self.current_frame = (self.current_frame + 1) % self.total_frames
            self.image = self.frames[self.current_frame]
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)

def main():
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    running = True
    while running:
        dt = clock.tick(30)/1000 #แปลง millisecs to sec
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        player.update(dt)

        screen.fill(WHITE)
        player.draw(screen)
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()