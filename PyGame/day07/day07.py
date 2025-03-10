import pygame
import sys
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Sheet Anim with Falling Balls")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BALL_RADIUS = 20

class Player:
    def __init__(self, x, y):
        self.sprite_sheet = pygame.image.load("day06/caveman.png").convert_alpha()
        self.sprite_sheet = pygame.transform.scale(self.sprite_sheet, (512, 128))
        self.frames = []
        self.frame_width = 128
        self.frame_height = 128
        self.total_frames = 4
        self.lives = 5  # Player starts with 5 lives
        self.speed = 5  # Player movement speed
        self.flipped = False  # Track player direction
        self.game_over = False  # Track game over state

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
        if abs(self.rect.x - self.target_x) > self.speed:
            if self.rect.x < self.target_x:
                self.rect.x += self.speed  # Move right
                if not self.flipped:
                    self.set_frames(flipped=True)
                    self.flipped = True
            elif self.rect.x > self.target_x:
                self.rect.x -= self.speed  # Move left
                if self.flipped:
                    self.set_frames(flipped=False)
                    self.flipped = False
        else:
            self.rect.x = self.target_x  # Snap exactly to target position to avoid shaking

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

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = random.randint(2, 5)  # Random speed for variation
        self.radius = BALL_RADIUS

    def update(self):
        self.y += self.speed

    def draw(self, surface):
        pygame.draw.circle(surface, RED, (self.x, self.y), self.radius)

    def check_collision(self, player):
        return player.rect.colliderect(pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2))

def main():
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150)
    balls = [Ball(random.randint(0, SCREEN_WIDTH), random.randint(-100, -20)) for _ in range(30)]
    
    running = True
    while running:
        dt = clock.tick(30) / 1000
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not player.game_over:
                player.target_x = event.pos[0]  # Update target position
        
        if not player.game_over:
            player.update(dt)
            balls_to_remove = []
            for ball in balls:
                ball.update()
                if ball.check_collision(player):
                    print("Hit")
                    player.lives -= 1  # Reduce life when hit
                    balls_to_remove.append(ball)  # Mark ball for removal
                    if player.lives <= 0:
                        print("Game Over")
                        player.game_over = True
        
            # Remove collided balls
            for ball in balls_to_remove:
                balls.remove(ball)
        
        screen.fill(WHITE)
        player.draw(screen)
        if not player.game_over:
            for ball in balls:
                ball.draw(screen)
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
