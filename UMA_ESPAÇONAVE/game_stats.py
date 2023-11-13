class GameStats():
    '''armazena dados estatisticos  do jogo'''
    def __init__(self, ai_settings):
        '''inicia os dados estatisticos'''
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = True
    
        

    def reset_stats(self):
        '''inicializa os dados estatisticos que
        podem mudar durante o jogo'''
        self.ship_left = self.ai_settings.ship_limit

