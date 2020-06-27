import pygame

class Buttons():
    def __init__(self, position): #position will be a tuple, define when making instance
        self.position = position

    def load_image(self, path):
        pygame.image.load(path).convert_alpha()
