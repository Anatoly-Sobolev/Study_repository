import pygame
import random

class Ball:
    def __init__(self, x, y, size, initial_speed_x, initial_speed_y, screen_width, screen_height):
        # Создаем прямоугольник для шара, который будет использоваться для отрисовки и обнаружения столкновений
        self.rect = pygame.Rect(x, y, size, size)
        # Текущие скорости шара по осям X и Y
        self.speed_x = initial_speed_x
        self.speed_y = initial_speed_y
        # Размеры экрана для расчета столкновений со стенами и набора очков
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.last_tuch = None


    def move(self):
        """
        Обновляет позицию шара на основе его текущей скорости.
        Обрабатывает столкновения с верхней и нижней границами экрана.
        """
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Отскок от верхней и нижней стен
        if self.rect.top <= 0 or self.rect.bottom >= self.screen_height:
            self.speed_y *= -1

    def check_collision(self, player1_paddle, player2_paddle):
        """
        Проверяет столкновения шара с ракетками игрока.
        При столкновении меняет направление движения шара по оси X.
        """
        # Проверяем столкновение с ракеткой первого игрока (слева)
        # Проверяем столкновение с ракеткой второго игрока (справа)
        if self.rect.colliderect(player1_paddle.rect): self.last_tuch = 'left'
        if self.rect.colliderect(player2_paddle.rect): self.last_tuch = 'right'

        if self.rect.colliderect(player1_paddle.rect) or self.rect.colliderect(player2_paddle.rect):
            self.speed_x *= -1
            return True
        else: return False

    def check_collision_mine(self, lst_of_mines):
        for mine in lst_of_mines:
            if self.rect.colliderect(mine.rect): return True



    def check_point(self):
        """
        Проверяет, вышел ли шар за левую или правую границу экрана,
        что означает набор очка.
        Возвращает 'player' или 'cpu' (согласно оригинальной логике, где 'cpu' - левый игрок, 'player' - правый),
        если очко набрано, иначе None.
        """
        if self.rect.left <= 0:
            return 'player_2' # Шар вышел за левую границу, значит очко набрал правый игрок
        if self.rect.right >= self.screen_width:
            return 'player_1' # Шар вышел за правую границу, значит очко набрал левый игрок
        return None

    def reset(self):
        """
        Сбрасывает позицию шара в центр экрана и рандомизирует его начальное направление
        после набора очка.
        """
        self.rect.center = (self.screen_width / 2, self.screen_height / 2)
        # Рандомизируем направление шара по X и Y
        self.speed_x *= random.choice([-1, 1])
        self.speed_y *= random.choice([-1, 1])

    def draw(self, surface):
        """
        Отрисовывает шар на заданной поверхности Pygame.
        """
        pygame.draw.ellipse(surface, 'white', self.rect)