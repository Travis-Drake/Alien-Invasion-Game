class GameStats:
	"""Track statistics for alien invasion"""
	def __init__(self, ai_game):
		"""initialize statistics"""
		self.settings = ai_game.settings
		self.reset_stats()
		# Start game in active state
		self.game_active = False
		#High score should never be reset
		self.high_score = 0

	def reset_stats(self):
		"""initialize statistics that can change during the game"""
		self.mothras_left = self.settings.mothra_limit
		self.score = 0
		self.level = 1