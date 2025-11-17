import  pygame
from Game_consts import *

class Screen:
    def __init__(self, width, hight, caption):
        self.wigth = width
        self.hight = hight
        self.screen = pygame.display.set_mode((width, hight))
        self.font = pygame.font.Font(None, 100)
        pygame.display.set_caption(caption)


    def update(self, ball, blue_player, red_player):

        pygame.draw.aaline(self.screen, 'black', (self.wigth / 2, 0), (self.wigth / 2, self.hight))

        blue_player.move_player()
        blue_player.draw(self.screen)

        red_player.move_player()
        red_player.draw(self.screen)

        player1_score_surface = self.font.render(str(red_player.score), True, text_color)
        player2_score_surface = self.font.render(str(blue_player.score), True, text_color)


        for mine in ball.lst_of_mines:
            pygame.draw.ellipse(self.screen, mine.color, mine.rect)
            mine.bomb_rect.center = mine.rect.center
            if mine.color == 'red':
                self.screen.blit(red_bomb, mine.bomb_rect)
            else: self.screen.blit(blue_bomb, mine.bomb_rect)




        for mine in ball.lst_of_mines:
            if ball.rect.colliderect(mine) and mine.color != ball.last_tuch:
                if ball.last_tuch == 'red':
                    blue_player.score += 1

                else:
                    red_player.score += 1


                ball.lst_of_mines = []
                ball.start_position()

        ball.check_colisions(red_player, blue_player, ball)
        ball.move()
        ball.draw(self.screen)

        self.screen.blit(player1_score_surface, (self.wigth / 4, 20))
        self.screen.blit(player2_score_surface, (3 * self.wigth / 4, 20))
