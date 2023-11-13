import sys
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats

def run_game():
    # Inicializa as configurações
    ai_settings = Settings()

    # Inicia o jogo
    pygame.init()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Cria uma instância para armazenar os dados estatísticos do jogo
    stats = GameStats(ai_settings)

    # Inicializa a nave, os aliens e o grupo de projéteis
    ship = Ship(ai_settings, screen)
    aliens = Group()
    bullets = Group()

    # Cria a frota de aliens
    gf.create_fleet(ai_settings,ship,screen, aliens)

    # Inicia o laço principal do jogo
    while True:
        # Verifica os eventos de teclado e mouse
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()
