import pygame

class Ship():
    
    def __init__(self,  ai_settings,screen):
        self.screen = screen
        self.ai_settings = ai_settings

        # Carrega a imagem da espaçonave e obtém seu rect
        self.image = pygame.image.load('imagens/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
    
        # Inicia uma nova espaçonave na parte inferior central da tela
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)

        #flag de movimento
        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''atualiza a posiçao da espaçonave de acordo com a flag de movimento'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = int(self.center)


    def blitme(self):
        '''Desenha a espaçonave em sua posição atual'''
        self.screen.blit(self.image, self.rect)


    def center_ship(self):
        '''centraliza a espaçonave na tela'''
        self.center = self.screen_rect.centerx