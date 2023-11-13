import sys
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group, Sprite
from game_stats import GameStats



def run_game():

    #inicia as configs
    ai_settings = Settings()

        
    # inicia o game.
    pygame.init()
    screen = pygame.display.set_mode((ai_settings.screen_width,  ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # cria uma instancia para armazenar dados estatisticos do jogo
    stats = GameStats(ai_settings)



    # inicia a nave
    ship = Ship(ai_settings , screen)
    #cria um grupo do qual serao armazenados projeteis
    bullets = Group()
    aliens =  Group()

    # frotas de aliens
    gf.create_fleet(ai_settings, screen,ship, aliens)



        
    # inicia o laço principal   
    while True:
        #eventos do teclado e mouse
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, ship, aliens ,bullets)

        gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
  
        # Deixa a tela mais recente visivel 
        pygame.display.flip()

run_game()

