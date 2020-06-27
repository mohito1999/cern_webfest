'''module/class import'''
import os
import pygame
from game_settings import Screen
from animsprite import AnimatedSprite

pygame.init()

screen_settings = Screen()
screen = pygame.display.set_mode((screen_settings.screen_width, screen_settings.screen_height))
FPS = 57

screen = pygame.display.set_mode()
clock = pygame.time.Clock()


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
        pygame.display.flip()

   
main()

    




