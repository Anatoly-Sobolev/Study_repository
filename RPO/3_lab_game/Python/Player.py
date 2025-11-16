import pygame
from Game_consts import  *

class Player:
    def __init__(self, x, y, width, hight, screen_h, color, key_up, key_down, speed_y = 0):
        self.width = width
        self.hight = hight
        self.screen_h = screen_h
        self.color = color
        self.score = 0
        self.rect = pygame.Rect(x, y, width, hight)
        self.speed_y = speed_y
        self.key_up = key_up
        self.key_down = key_down




    def move_player(self):
        self.rect.y += self.speed_y
        if self.rect.y < 0: self.rect.y = 0
        if self.rect.y + self.hight > self.screen_h: self.rect.y = self.screen_h - self.hight


    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)


    def check_push(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == self.key_up:
                self.speed_y = -15
            if event.key == self.key_down:
                self.speed_y = 15

        if event.type == pygame.KEYUP:
            if event.key == self.key_up or event.key == self.key_down:
                self.speed_y = 0




