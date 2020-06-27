'''module/class import'''
import os
import pygame
from game_settings import Screen
from animsprite import AnimatedSprite
from buttons import Buttons
import math
from sec_round import main1

pygame.init()

screen_settings = Screen()
screen = pygame.display.set_mode((screen_settings.screen_width, screen_settings.screen_height))
FPS = 57

screen = pygame.display.set_mode()
play = pygame.image.load("/Users/mohitmotwani/Documents/GitHub/cern_webfest/assets/Buttons/Play-Button.png").convert_alpha()
play_button = pygame.Rect(325, 500, 150, 50)
#play = Buttons((325, 250))
#play.load_image("/Users/mohitmotwani/Documents/GitHub/cern_webfest/assets/Buttons/Play-Button.png")
clock = pygame.time.Clock()
'''
ball = pygame.Rect(304,640,20 ,20)
line = pygame.Rect(280,650,50, 3)
gravity = 9.8
'''
'''
#Graphics
launcher = pygame.image.load('/Users/mohitmotwani/Documents/GitHub/cern_webfest/assets/Projectile Launcher.png')
#launcher.set_colorkey((0,0,0))
background = pygame.image.load('/Users/mohitmotwani/Documents/GitHub/cern_webfest/assets/Challenge Room1.jpg')
#launcher.set_alpha(100)

bg_color = pygame.Color('grey12')
light_grey = (200,200,200)

font = pygame.font.SysFont("comicsans", 30, True)
'''

def load_images(path):
    images = []
    imagelist = sorted(os.listdir(path))
    imagelist = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg',  '6.jpg', '7.jpg', '8.jpg', '9.jpg', '10.jpg', '11.jpg', '12.jpg', '13.jpg', '14.jpg', '15.jpg', '16.jpg', '17.jpg', '18.jpg', '19.jpg', 
     '20.jpg', '21.jpg', '22.jpg', '23.jpg', '24.jpg', '25.jpg', '26.jpg', '27.jpg', '28.jpg', '29.jpg',  
    '30.jpg', '31.jpg', '32.jpg', '33.jpg', '34.jpg', '35.jpg', '36.jpg', '37.jpg', '38.jpg', '39.jpg', '40.jpg', 
    '41.jpg', '42.jpg', '43.jpg', '44.jpg', '45.jpg', '46.jpg', '47.jpg', '48.jpg', '49.jpg', '50.jpg', '51.jpg', 
    '52.jpg', '53.jpg', '54.jpg', '55.jpg', '56.jpg', '57.jpg']
    for file_name in imagelist:
        image = pygame.image.load(path + os.sep + file_name).convert()
        images.append(image)
    return images


def main():
    images = load_images(path="/Users/mohitmotwani/Documents/GitHub/cern_webfest/assets/Foundation (d2) - copy")  # Make sure to provide the relative or full path to the images directory.
    player = AnimatedSprite(position=(0, 0), images=images)
    all_sprites = pygame.sprite.Group(player)  # Creates a sprite group and adds 'player' to it.

    running = True
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                pygame.quit()
        
        while running:

            dt = 1   # Amount of seconds between each loop.

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    

            all_sprites.update(dt)  # Calls the 'update' method on all sprites in the list (currently just the player).

            
            
            screen.fill(screen_settings.bg_color)
            all_sprites.draw(screen)
            pygame.display.update()
            clock.tick(100)
            if player.index == 56:
                running = False
                break
        
        screen.blit(screen_settings.home_image, (0, 0))
        screen.blit(play, [115, 300])
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    ## if mouse is pressed get position of cursor ##
                    pos = pygame.mouse.get_pos()
                    ## check if cursor is on button ##
                    if play_button.collidepoint(pos):
                        #Group all of Ryan's code as a function and call it when mouse is pressed
                        main1(screen, screen_settings.bg_color)
        
        

   
main()

'''
def test():
    pygame.init()
    screen = pygame.display.set_mode((770,430))
    pygame.mouse.set_visible(1)
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250,250,250))
    screen.blit(background, (0,0))
    pygame.display.flip()

    ## set-up screen in these lines above ##

    button = pygame.image.load('Pictures/cards/stand.png').convert_alpha()
    b = screen.blit(button, (300, 200))
    pygame.display.flip()

    ## does button need to be 'pygame.sprite.Sprite for this? ##
    ## I use 'get_rect() ##
    

    ## loop to check for mouse action and its position ##
   ''' 


