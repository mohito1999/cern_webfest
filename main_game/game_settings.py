import pygame

class Screen():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)
        self.home_image = pygame.image.load("/Users/mohitmotwani/Documents/GitHub/cern_webfest/assets/Foundation (d2) - Copy/57.jpg")