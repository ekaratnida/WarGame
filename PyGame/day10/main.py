import pygame
import sys
import random
import pygame_gui

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Sheet Anim with Falling Balls")

manager = pygame_gui.UIManager((800,600))
start_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((400,300), #กำหนดตำแหน่งของ button
    (200,80)), #กำหนดขนาดของ button 
    text='Start',
    manager=manager
)

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0,0,0)
BALL_RADIUS = 20

class Player:
    def __init__(self, x, y):
        self.sprite_sheet = pygame.image.load("day07/caveman.png").convert_alpha()
        self.sprite_sheet = pygame.transform.scale(self.sprite_sheet, (512, 128))
        self.frames = []
        self.frame_width = 128
        self.frame_height = 128
        self.total_frames = 4
        self.lives = 5  # Player starts with 5 lives
        self.speedX = 3  # Player movement speed
        self.speedY = 5
        self.flipped = False  # Track player direction
        self.game_over = False  # Track game over state
        self.isJump = False
        self.isPlaying = False

        for i in range(self.total_frames):
            frame = self.get_frame(i)
            self.frames.append(frame)
        
        self.current_frame = 0
        self.original_frames = self.frames.copy()  # Store original frames for flipping
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.animation_speed = 0.1
        self.animation_timer = 0
        self.target_x = x  # New attribute to track target position

    def get_frame(self, frame_number):
        frame = pygame.Surface((self.frame_width, self.frame_height), pygame.SRCALPHA)
        frame.blit(
            self.sprite_sheet,
            (0, 0),
            (frame_number * self.frame_width, 0, self.frame_width, self.frame_height)
        )
        return frame

    def update(self, dt):
        if self.game_over:
            return

        self.animation_timer += dt
        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0
            self.current_frame = (self.current_frame + 1) % self.total_frames
            self.image = self.frames[self.current_frame]
        
        # Smooth movement towards target_x without shaking
        if abs(self.rect.x - self.target_x) > self.speedX:
            if self.rect.x < self.target_x:
                self.rect.x += self.speedX  # Move right
                if not self.flipped:
                    self.set_frames(flipped=True)
                    self.flipped = True
            elif self.rect.x > self.target_x:
                self.rect.x -= self.speedX  # Move left
                if self.flipped:
                    self.set_frames(flipped=False)
                    self.flipped = False
        else:
            self.rect.x = self.target_x  # Snap exactly to target position to avoid shaking

        if self.isJump:
            self.rect.y -= self.speedY
            self.speedY -= 8*dt
        if self.rect.y >= 450:
            self.isJump = False
            self.rect.y = 450

    def set_frames(self, flipped):
        if flipped:
            self.frames = [pygame.transform.flip(frame, True, False) for frame in self.original_frames]
        else:
            self.frames = self.original_frames.copy()
        self.image = self.frames[self.current_frame]

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        # Display lives
        font = pygame.font.SysFont(None, 36)
        lives_text = font.render(f"Lives: {self.lives}", True, (0, 0, 0))
        surface.blit(lives_text, (10, 10))
        
        if self.game_over:
            game_over_text = font.render("GAME OVER", True, (255, 0, 0))
            surface.blit(game_over_text, (SCREEN_WIDTH // 2 - 60, SCREEN_HEIGHT // 2))

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
        pygame.draw.rect(surface, BLACK, (self.x,self.y,self.width,self.height))

    def check_collision(self, player):
        return player.rect.colliderect(pygame.Rect(self.x, self.y, self.width, self.height))

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speedX = random.randint(2, 5)  # Random speed for variation
        self.radius = random.randint(10,30) #BALL_RADIUS

    def update(self):
        self.y += self.speedX

    def draw(self, surface):
        pygame.draw.circle(surface, RED, (self.x, self.y), self.radius)

    def check_collision(self, player):
        return player.rect.colliderect(pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2))

def main():
    
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150)
    balls = [Ball(random.randint(0, SCREEN_WIDTH), random.randint(-100, -20)) for _ in range(50)]
    enemy1s = [Enemy1(random.randint(-30, -20),random.randint(SCREEN_HEIGHT-150,SCREEN_HEIGHT),40,40) for _ in range(10)]
    running = True

    while running:
        dt = clock.tick(60) / 1000            
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if player.isJump == False:
                    player.isJump = True
                    player.speedY = 8
            elif event.type == pygame.MOUSEMOTION:
                player.target_x = event.pos[0]
            elif event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == start_button:
                    print("Start Game")
                    player.isPlaying = True
                    player.game_over = False
                    player.lives = 5
                    balls = [Ball(random.randint(0, SCREEN_WIDTH), random.randint(-100, -20)) for _ in range(50)]
                    player.rect.x = SCREEN_WIDTH // 2
                    player.rect.y = SCREEN_HEIGHT - 150
                    player.isJump = False
                    player.isPlaying = True
                    enemy1s = [Enemy1(random.randint(-30, -20),random.randint(SCREEN_HEIGHT-150,SCREEN_HEIGHT),40,40) for _ in range(10)]
  
            manager.process_events(event)
        
        if player.isPlaying:
            if not player.game_over:
                player.update(dt)
                balls_to_remove = []
                for enemy in enemy1s:
                    enemy.update()

                for ball in balls:
                    ball.update()
                    if ball.check_collision(player):   
                        if player.lives > 0:
                            print("Hit")
                            player.lives -= 1  # Reduce life when hit
                            balls_to_remove.append(ball)  # Mark ball for removal
                            if player.lives <= 0:
                                print("Game Over")
                                player.game_over = True
                                player.isPlaying = False
                                balls = []
                
                if len(balls) > 0:
                    for ball in balls_to_remove:
                        balls.remove(ball)
            
                screen.fill(WHITE)

                player.draw(screen)

                if not player.game_over:
                    for ball in balls:
                        ball.draw(screen)
                    for enemy in enemy1s:
                        enemy.draw(screen)
        
        manager.update(dt)

        if player.isPlaying == False:
            manager.draw_ui(screen)

        pygame.display.flip()

if __name__ == "__main__":
    main()