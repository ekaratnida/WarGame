'''
import subprocess
import sys
subprocess.check_call([sys.executable, '-m', 'pip', 
'install', 'pygame_gui', '-U'])
'''

import pygame
import pygame_gui
pygame.init()

pygame.display.set_caption('My GUI Test')
window_surface = pygame.display.set_mode((800, 600))

background = pygame.Surface((800, 600))
background.fill(pygame.Color('#FFFFFF'))

manager = pygame_gui.UIManager((800,600), theme_path="day09/quick_start.json")

hello_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((400,300), #กำหนดตำแหน่งของ button
    (200,80)), #กำหนดขนาดของ button 
    text='Click Me',
    manager=manager
)

hello_button2 = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((400,100), #กำหนดตำแหน่งของ button
    (200,80)), #กำหนดขนาดของ button 
    text='Click Me2',
    manager=manager
)

drop_down_menu = pygame_gui.elements.UIDropDownMenu(
    options_list=["Easy","Medium","Hard"],
    starting_option="Medium",
    relative_rect=pygame.Rect((10,275),(300,40)),
    manager=manager
)

text_box = pygame_gui.elements.UITextBox(
     html_text="This is an <effect id=test>EARTHQUAKE</effect>",
     relative_rect=pygame.Rect(100, 100, 200, 50),
     manager=manager)

clock = pygame.time.Clock()

is_running = True

while is_running:
    time_delta = clock.tick(60)/1000.0 #ระยะเวลาของการ update ในแต่ละรอบ มีค่าเท่ากับ 1000 (ms)/60 (fps)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == hello_button:
                print("Hello World!",time_delta)
                message_window = pygame_gui.elements.UIWindow(
                    rect=(400,400,200,100),
                    manager=manager,
                    window_display_title="Message alert"
                )
                # Add a UILabel inside the window
                label = pygame_gui.elements.UILabel(
                    relative_rect=pygame.Rect(0, 0, 200, 30),
                    text=f"Hello World! = {time_delta}",
                    manager=manager,
                    container=message_window  # This ensures the label is inside the window
                )
              
                label2 = pygame_gui.elements.UILabel(
                    relative_rect=pygame.Rect(0, 30, 200, 30),
                    text=f"Test label2",
                    manager=manager,
                    container=message_window  # This ensures the label is inside the window
                )



        if event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
            if event.ui_element == drop_down_menu:
                print("drop down select = ",event.text)
                text_box.set_active_effect(pygame_gui.TEXT_EFFECT_BOUNCE, effect_tag='test')

        manager.process_events(event)

    manager.update(time_delta)
    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()
