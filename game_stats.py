class GameStats():
	"""Track statistics for lien Invasion. """
	def __init__(self, ai_settings):
		"""Initialise statistics"""
		self.ai_settings = ai_settings
		self.reset_stats()
		#Start alien invasion in an active state.
		self.game_active = False

		#High score should never be reset.
		self.high_score = 0
		self.level = 1
		

	def reset_stats(self):
		"""Initialise statistics that can change during the game."""
		self.ship_left = self.ai_settings.ship_limit
		self.score = 0
