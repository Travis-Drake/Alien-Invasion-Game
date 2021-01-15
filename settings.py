class Settings:
	"""a class to store all of the game settings"""
	def __init__(self):
		"""initialize game settings"""
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (0,168,243)
		# Bullet Settings
		self.bullet_width = 5
		self.bullet_height = 15
		self.bullet_color = (255,0,0)
		self.bullets_allowed = 3
		# Alien settings
		self.fleet_drop_speed =10
		self.mothra_limit = 3
		# How quickly the game speeds up
		self.speedup_scale = 1.1
		#How quickly alien point values increase
		self.score_scale = 1.5
		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		"""Initialize settings that change over time"""
		self.mothra_speed = 1.5
		self.bullet_speed = 5
		self.alien_speed = 1.0
		# Fleet direction of 1 represents right, -1 represents left
		self.fleet_direction = 1
		#Scoring
		self.alien_points = 50

	def increase_speed(self):
		"""increase speed settings and alien point values"""
		self.mothra_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.alien_speed *= self.speedup_scale
		self.alien_points =int(self.score_scale * self.alien_points)

