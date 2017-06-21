import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
	#Initialise pygame, settings and screen object.
	pygame.init()
	ai_settings=Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	#Make the play Button
	play_button = Button(ai_settings, screen, "Play")

	#Create an instance to store game statistics.
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings, screen,stats)

	#Make a ship, a group of bullets, and a fleet of aliens.
	ship=Ship(ai_settings, screen)
	bullets = Group()
	aliens = Group()

	#create athe fleet of aliens.
	gf.create_fleet(ai_settings, screen, ship, aliens)

	#Start the main loop for the game.
	while True:
		gf.check_events(ai_settings, screen,stats, sb, play_button, ship, aliens, bullets)
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
			gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, aliens)
		gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
		

		
		

run_game()

