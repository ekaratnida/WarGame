from GameLogic import GameLogic
import pygame
import pygame_gui
class GameUI:

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    
    def __init__(self):
        print("Init GameUI.")

    @staticmethod
    def init():
        GameUI.screen = pygame.display.set_mode((GameUI.SCREEN_WIDTH, GameUI.SCREEN_HEIGHT))
        pygame.display.set_caption("Adventure of CaveMan")
        GameUI.manager = pygame_gui.UIManager((GameUI.SCREEN_WIDTH, GameUI.SCREEN_HEIGHT))
        GameUI.start_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((300,250),(200,80)), #ตำแหน่งและขนาดของ button 
            text='Start Game',
            manager=GameUI.manager
        )

        GameUI.WHITE = (255, 255, 255)
        GameUI.RED = (255, 0, 0)
        GameUI.BLACK = (0,0,0)

    @staticmethod
    def draw(surface,lives):
        # Display lives
        font = pygame.font.SysFont(None, 36)
        lives_text = font.render(f"Lives: {lives}", True, (0, 0, 0))
        surface.blit(lives_text, (10, 10))

        if GameLogic.game_over:
            game_over_text = font.render("GAME OVER", True, (255, 0, 0))
            surface.blit(game_over_text, (GameLogic.SCREEN_WIDTH // 2 - 60, GameLogic.SCREEN_HEIGHT // 2))