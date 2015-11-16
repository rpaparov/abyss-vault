from game import Game

def test_loadingSaveGame():
	"""Loading saved game."""
	g = Game()
	assert g.loadFromFile('data/game1.json') == True
	assert 'id' in g.vault
