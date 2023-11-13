import pygame
import settings 
from pygame.sprite import Group, Sprite


class Bullet(Sprite):
    '''uma classe que administra os tiros'''

    def __init__(self, ai_settings, screen, ship):
        '''CRIA UM OBJETO PARA O TIRO NA POSIÇAO ATUAL DA ESPAÇONAVE'''
        super(Bullet, self).__init__()
        self.screen = screen

        #cria um retangulo (rect) para o tiro (0 , 0) e, em seguida define a posiçao
        self.rect = pygame.Rect(0 ,0 ,  ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #armazena a posiçao do projetil como um valor decimal
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor


    def update(self):
        '''move o tiro'''
        # atualiza a posição decimal do projetil
        self.y -= self.speed_factor
        # atualiza a posição de rect
        self.rect.y = self.y        
    
    def draw_bullet(self):
        '''desenha o projetil na tela'''
        pygame.draw.rect(self.screen, self.color, self.rect)