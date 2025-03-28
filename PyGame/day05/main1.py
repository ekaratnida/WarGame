
# Import pygame
import pygame

# Initialise pygame
pygame.init()

# Set window size
size = width,height = 600, 600
screen = pygame.display.set_mode(size)

# Clock
clock = pygame.time.Clock()

# Load image
image = pygame.image.load('day5/img1.png')

# Set the size for the image
DEFAULT_IMAGE_SIZE = (200, 200)

# Scale the image to your needed size
image = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)

# Set a default position
DEFAULT_IMAGE_POSITION = (200,200)

# Prepare loop condition
running = False

# Event loop
while not running:

	# Close window event
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = True

	# Background Color
	screen.fill((0, 0, 0))

	# Show the image
	screen.blit(image, DEFAULT_IMAGE_POSITION)

	# Part of event loop
	pygame.display.flip()
	clock.tick(30)
