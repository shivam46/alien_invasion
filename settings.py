class Settings():
	""" A class to store all Settings for Alien Invasion game"""
	def __init__(self):
		"""Initialise the game static settings"""
		# Screen's settings
		self.screen_width = 1366
		self.screen_height = 700
		self.bg_color = (230,230,230) 

		# Ship settings
		self.ship_speed_factor = 1.5
		self.ship_limit = 3

		#Bullet's settings
		self.bullet_width = 27
		self.bullet_height = 15
		self.bullet_speed_factor = 2
		self.bullet_color = 60,60,60
		self.bullets_allowed = 3

		#Alien settings
		self.alien_speed_factor=1
		self.fleet_drop_speed = 8
		#fleet direction of 1 represent right; -1 represent right
		self.fleet_direction = 1

		#How quickly game speed up
		self.speed_up_scale = 1.2

		#How quickly alien's points increase
		self.score_scale = 1.1

		self.initialise_dynamic_settings()

	def initialise_dynamic_settings(self):
		"""Initialise settings that change throughput the game."""
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 3
		self.alien_speed_factor = 1

		#fleet direction 1 represent right, -1 represent left.
		self.fleet_direction = 1

		#Scoring.
		self.alien_points = 50

	def increase_speed(self):
		"""Increase speed settings and alien point score."""
		self.ship_speed_factor *= self.speed_up_scale
		self.bullet_speed_factor *= self.speed_up_scale
		self.alien_speed_factor *= self.speed_up_scale
		self.alien_points = int(self.alien_points * self.score_scale)



		