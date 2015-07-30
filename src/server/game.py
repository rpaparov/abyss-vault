import json

class Game():
	
	def __init__(self):
		self.shelter = {}
	
	def loadFromFile(self, filename):
		"""Load a game from a json file."""
		with open(filename, 'rt') as fp:
			try:
				self.vault = json.load(fp)
			except ValueError:
				self.logErr('could not load game file {}'.format(filename))
				return False
		return True
	
	def logErr(self, message):
		"""Log error to file. TODO implement this!"""
		print(message)
