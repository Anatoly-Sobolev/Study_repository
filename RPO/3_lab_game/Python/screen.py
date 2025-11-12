import pygame

class Screen:
    """
    Класс Screen управляет отображением всех игровых элементов на экране Pygame.
    Отвечает за инициализацию экрана, отрисовку фона, счета, разделительной линии,
    а также шара и ракеток.
    """
    def __init__(self, width, height, caption):
        # Инициализируем Pygame (на случай, если не инициализировано в main.py)
        # Хотя лучше инициализировать один раз в main.py
        # pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(caption)
        # Шрифт для отображения счета
        self.font = pygame.font.Font(None, 100)
        self.screen_width = width
        self.screen_height = height

    def draw_elements(self, ball_obj, player1_paddle, player2_paddle, player1_points, player2_points, lst_of_mines):
        """
        Отрисовывает все игровые элементы на экране.
        :param ball_obj: Объект Ball для отрисовки.
        :param player1_paddle: Объект Player для левой ракетки.
        :param player2_paddle: Объект Player для правой ракетки.
        :param player1_points: Счет левого игрока.
        :param player2_points: Счет правого игрока.
        """
        self.screen.fill('black') # Заливаем фон черным цветом

        # Отрисовка счета
        # player1_points (левая сторона)
        # player2_points (правая сторона)
        player1_score_surface = self.font.render(str(player1_points), True, "white")
        player2_score_surface = self.font.render(str(player2_points), True, "white")
        self.screen.blit(player1_score_surface, (self.screen_width / 4, 20))
        self.screen.blit(player2_score_surface, (3 * self.screen_width / 4, 20))

        # Отрисовка центральной разделительной линии
        pygame.draw.aaline(self.screen, 'white', (self.screen_width / 2, 0), (self.screen_width / 2, self.screen_height))

        # Отрисовка шара и ракеток
        ball_obj.draw(self.screen)
        player1_paddle.draw(self.screen)
        player2_paddle.draw(self.screen)
        [mine.draw(self.screen) for mine in lst_of_mines]



        # Обновляем весь экран для отображения изменений
        pygame.display.update()