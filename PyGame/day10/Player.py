import pygame
class Player:
    def __init__(self, x, y):
        self.sprite_sheet = pygame.image.load("day10/caveman.png").convert_alpha()
        self.sprite_sheet = pygame.transform.scale(self.sprite_sheet, (512, 128))
        self.frames = []
        self.frame_width = 128
        self.frame_height = 128
        self.total_frames = 4
        self.lives = 5  # Player starts with 5 lives
        self.speedX = 3  # Player movement speed
        self.speedY = 5
        self.flipped = False  # Track player direction
        self.isJump = False

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