import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_settings, screen) :
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #carrega a imagem
        self.image = pygame.image.load('imagens/alien.png')
        self.rect = self.image.get_rect()

        #inicia um novo alien proximo a parte superior da tela
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #armazena a posiçao exata em sua posiçao alienigena 
        self.x = float(self.rect.x)

    def blitme(self):
        '''desenha o alien na sua posiçao atual'''
        self.screen.blit(self.image, self.rect)


    
    def check_edges(self):
        '''devolve true se o alien tocar a extremidade'''
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0 :
            return True
        
            
    
    def update(self):
        '''move o alieligena para a direita'''
        self.x += (self.ai_settings.alien_speed_factor *self.ai_settings.fleet_direction)
        self.rect.x = self.x