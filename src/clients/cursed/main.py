import argparse
from game import Game

DEFAULT_ADDRESS = '127.0.0.1:20000'

def ReadOptions():
	'''
	Def : Parse command line arguments.
	Return : Parsed arguments.
	'''
	parser = argparse.ArgumentParser(description='Cursed client for Aqua Vault')
	parser.add_argument('-d', '--delay', type=int, help='refresh delay, in ms', default=1000)
	parser.add_argument('-a', '--address', type=str, metavar='ip:port', help='server address [default=%default]', default=DEFAULT_ADDRESS)
	return parser.parse_args()


def Main():
	'''
	Def : Main entry point. Read command line options and start the game.
	'''
	args = ReadOptions()
	idd = 1 # TODO just for debug
	game = Game(idd, args.address, args.delay)
	game.start()


if __name__ == '__main__':
	Main()
