class Settings():
    #todas as configs do jogo.

    def __init__(self):
        '''inicia as configurações do jogo '''

        #configuçao da tela
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color =(0, 0, 0)
        #config da velocida da nave
        self.ship_speed_factor = 1.5
        #config do bullet
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 50, 60)
        #numero de balas
        self.bullet_allowed = 3
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet direction = 1 (direita ) ou -1 (esquerda)
        self.fleet_direction = 1
        self.ship_limit = 3
