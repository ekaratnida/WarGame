import pygame
import sys
import random
import pygame_gui
from Ball import Ball
from Player import Player
from Enemy import Enemy1
from GameUI import GameUI
from GameLogic import GameLogic

pygame.init()

def main():

    GameUI.init()
    
    clock = pygame.time.Clock()
    player = Player(GameUI.SCREEN_WIDTH // 2, GameUI.SCREEN_HEIGHT - 150)
    balls = [Ball(random.randint(0, GameUI.SCREEN_WIDTH), random.randint(-100, -20)) for _ in range(20)]
    enemy1s = [Enemy1(random.randint(-30, -20),random.randint(GameUI.SCREEN_HEIGHT-150,GameUI.SCREEN_HEIGHT),40,40) for _ in range(5)]
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
                if event.ui_element == GameUI.start_button:
                    print("Start Game")
                    GameLogic.isPlaying = True
                    GameLogic.game_over = False
                    player.lives = 5
                    balls = [Ball(random.randint(0, GameUI.SCREEN_WIDTH), random.randint(-100, -20)) for _ in range(20)]
                    player.rect.x = GameUI.SCREEN_WIDTH // 2
                    player.rect.y = GameUI.SCREEN_HEIGHT - 150
                    player.isJump = False
                    GameLogic.isPlaying = True
                    enemy1s = [Enemy1(random.randint(-30, -20),random.randint(GameUI.SCREEN_HEIGHT-150,GameUI.SCREEN_HEIGHT),40,40) for _ in range(10)]
  
            GameUI.manager.process_events(event)

        if GameLogic.isPlaying:

            GameUI.screen.fill(GameUI.WHITE)

            if not GameLogic.game_over:
            
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
                            GameUI.draw(surface=GameUI.screen,lives=player.lives)
                            balls_to_remove.append(ball)  # Mark ball for removal
                            if player.lives <= 0:
                                print("Game Over")
                                GameLogic.game_over = True
                                GameLogic.isPlaying= False
                                balls = []
                
                if len(balls) > 0:
                    for ball in balls_to_remove:
                        balls.remove(ball)

                player.draw(GameUI.screen)

                if not GameLogic.game_over:
                    for ball in balls:
                        ball.draw(GameUI.screen)
                    for enemy in enemy1s:
                        enemy.draw(GameUI.screen)

        else:
            GameUI.screen.fill("#af7edd")
        
        GameUI.manager.update(dt)

        if GameLogic.isPlaying == False:
            GameUI.manager.draw_ui(GameUI.screen)

        pygame.display.flip()

if __name__ == "__main__":
    main()