import pygame
import random

class Mine:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)


    def draw(self, surface):

        pygame.draw.ellipse(surface, 'red', self.rect)







