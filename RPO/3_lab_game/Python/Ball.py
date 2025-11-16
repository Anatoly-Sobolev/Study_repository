import pygame
import random
from Mine import Mine
from Game_consts import *

class Ball:
    def __init__(self, width , hight, color, screen_w, screen_h):
        self.rect = pygame.Rect(screen_w/2, screen_h/2, width, hight)
        self.width = width
        self.hight = hight
        self.color = color
        self.last_tuch = None
        self.speed_x = random.choice([-1, 1]) * speed_x
        self.speed_y = random.choice([-1, 1]) * speed_y
        self.screen_w = screen_w
        self.screen_h = screen_h
        self.lst_of_mines = []

    def start_position(self):
        self.rect.x = 640
        self.rect.y = 360
        self.speed_x = random.choice([-1, 1]) * speed_x
        self.speed_y = random.choice([-1, 1]) * speed_y

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y


    def check_colisions(self, red_player, blue_player, ball):
        if self.rect.x + self.width> self.screen_w:
            red_player.score += 1
            self.start_position()
            self.lst_of_mines = []


        if self.rect.x < 0:
            blue_player.score += 1
            self.start_position()
            self.lst_of_mines = []

        if self.rect.y < 0:
            self.speed_y *= -1
        if self.rect.y + self.hight > self.screen_h:
            self.speed_y *= -1

        if self.rect.colliderect(red_player.rect):
            self.speed_x *= -1
            self.last_tuch = red_player.color
            new_mine = Mine(self.last_tuch)
            self.lst_of_mines.append(new_mine)

        if self.rect.colliderect(blue_player.rect):
            self.speed_x *= -1
            self.last_tuch = blue_player.color
            new_mine = Mine(self.last_tuch)
            self.lst_of_mines.append(new_mine)


    def check_colis_mine(self, red_player, blue_player):
        for mine in self.lst_of_mines:
            if self.rect.colliderect(mine) and mine.color != self.last_tuch:
                if self.last_tuch == 'red':
                    blue_player.score += 1

                else:
                    red_player.score += 1

                self.lst_of_mines = []





    def draw(self, surface):
        pygame.draw.ellipse(surface, self.color, self.rect)

