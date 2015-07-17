import argparse
from gameServer import GameServer, GameServerHandler # remove this!

DEFAULT_ADDRESS = '127.0.0.1:20000'

def ReadOptions():
	'''
	Def : Parse command line arguments.
	Return : Parsed arguments.
	'''
	parser = argparse.ArgumentParser(description='Cursed client for Aqua Vault')
	parser.add_argument('-d', '--delay', type=int, help='refresh delay, in ms', default=500)
	parser.add_argument('-a', '--address', type=str, metavar='ip:port', help='server address [default=%default]', default=DEFAULT_ADDRESS)
	return parser.parse_args()


def Main():
	'''
	Def : Main entry point. Read command line options and start the server.
	'''
	args = ReadOptions()
	(host, port) = args.address.split(':')
	
	server = GameServer((host, int(port)), GameServerHandler)
	try:
		server.serve_forever()
	except KeyboardInterrupt:
		pass


if __name__ == '__main__':
	Main()
