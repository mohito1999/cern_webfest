import pygame
import sys 
from game_settings import Screen

pygame.init()
pygame.mixer.quit()
clock = pygame.time.Clock()

settings = Screen()
screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(settings.bg_color)

    pygame.display.flip()

