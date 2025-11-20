import pygame
pygame.init()

screen_w = 1280
screen_h = 720
background = pygame.image.load('images/background.png')
caption = "FOOTBALL GAME!"
ball_size = 50
ball_image = pygame.image.load('images/ball.png')
speed_x = 12
speed_y = 10
paddle_w = 20
paddle_h = 200
paddle_speed = 25
blue_player_image = pygame.image.load('images/blue_player.png')
red_player_image = pygame.image.load('images/red_player.png')
size_player = 200
game_over_score = 3

blue_player_data = (0, screen_h//2, paddle_w, paddle_h)
red_player_data = (screen_w -paddle_w, screen_h//2, paddle_w, paddle_h)

game_over_sound = pygame.mixer.Sound('sounds/game_over.wav')
game_over_sound.set_volume(0.7)
goal_sound = pygame.mixer.Sound('sounds/whistle.wav')
game_over_aplod = pygame.mixer.Sound('sounds/game_over_aplod.wav')

back_music = pygame.mixer.Sound('sounds/back_music.wav')
back_sounds = pygame.mixer.Sound('sounds/back_sounds.wav')
kick_sound = pygame.mixer.Sound('sounds/kick.wav')