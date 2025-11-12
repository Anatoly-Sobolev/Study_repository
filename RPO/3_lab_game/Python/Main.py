import pygame
import sys
import random

from Ball import Ball
from player import Player
from screen import Screen
from Mine import Mine

screen_width = 1280
screen_height = 720


pygame.init()


game_display = Screen(screen_width, screen_height, "Paddle Game! Laba_#_3")


ball_size = 30
initial_ball_speed_x = 8 * random.choice([-1, 1])  # Начальная скорость по X, рандомно влево или вправо
initial_ball_speed_y = 6 * random.choice([-1, 1])  # Начальная скорость по Y, рандомно вверх или вниз
ball_obj = Ball(screen_width / 2 - ball_size / 2, screen_height / 2 - ball_size / 2,
                ball_size, initial_ball_speed_x, initial_ball_speed_y, screen_width, screen_height)



paddle_width = 20
paddle_height = 100
# Player 1 (левая ракетка, управляется W/S)
player1_paddle = Player(0, screen_height / 2 - paddle_height / 2, paddle_width, paddle_height, screen_height)
# Player 2 (правая ракетка, управляется UP/DOWN)
player2_paddle = Player(screen_width - paddle_width, screen_height / 2 - paddle_height / 2, paddle_width, paddle_height,
                        screen_height)


player1_points = 0  # Очки левого игрока
player2_points = 0  # Очки правого игрока

lst_of_mines = []

clock = pygame.time.Clock()  # Для контроля частоты кадров

# --- Основной игровой цикл ---
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Обработка нажатий клавиш для управления ракетками
        if event.type == pygame.KEYDOWN:
            # Управление для Player 2 (правая ракетка)
            if event.key == pygame.K_UP:
                player2_paddle.set_speed(-15)
            if event.key == pygame.K_DOWN:
                player2_paddle.set_speed(15)
            # Управление для Player 1 (левая ракетка)
            if event.key == pygame.K_w:
                player1_paddle.set_speed(-15)
            if event.key == pygame.K_s:
                player1_paddle.set_speed(15)

        # Обработка отпускания клавиш для остановки ракетки
        if event.type == pygame.KEYUP:
            # Player 2
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player2_paddle.set_speed(0)
            # Player 1
            if event.key == pygame.K_w or event.key == pygame.K_s:
                player1_paddle.set_speed(0)


    ball_obj.move()  # Движение шара
    player1_paddle.move()  # Движение левой ракетки
    player2_paddle.move()  # Движение правой ракетки

    if  ball_obj.check_collision(player1_paddle, player2_paddle):

        new_mine = Mine(random.randint(30, 1200), random.randint(30, 700), 30, 30)
        lst_of_mines.append(new_mine)

    if ball_obj.check_collision_mine(lst_of_mines):
        player1_points += ball_obj.last_tuch == 'right'
        player2_points += ball_obj.last_tuch == 'left'
        ball_obj.last_tuch = None
        lst_of_mines = []
        ball_obj.reset()



    # Проверка на набор очков
    winner_side = ball_obj.check_point()  # Получаем, кто набрал очко ('player' или 'cpu' согласно Ball.py)
    if winner_side == 'player_1':  # Если шар вышел за правую границу (т.е. правый игрок пропустил), очко получает левый игрок
        player1_points += 1
        lst_of_mines = []

        ball_obj.reset()  # Сбрасываем шар
    elif winner_side == 'player_2':  # Если шар вышел за левую границу (т.е. левый игрок пропустил), очко получает правый игрок
        player2_points += 1
        lst_of_mines = []
        ball_obj.reset()  # Сбрасываем шар

    # --- Отрисовка всех элементов на экране ---
    game_display.draw_elements(ball_obj, player1_paddle, player2_paddle, player1_points, player2_points, lst_of_mines)

    clock.tick(60)  # Ограничиваем частоту кадров до 60 в секунду


