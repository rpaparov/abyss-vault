import socketserver
import json
import time

class GameServer(socketserver.ThreadingTCPServer):
	allow_reuse_address = True


class GameServerHandler(socketserver.BaseRequestHandler):
	def handle(self):
		# listen
		data = self.request.recv(64)
		query = data.decode('utf-8')
		# handle query (temporary output for debug)
		t = time.ctime()
		print('request at {}, query = {}'.format(t, query))
		# respond
		data = {'status' : 'ok', 'time' : t}
		s = bytes(json.dumps(data), 'UTF-8')
		self.request.sendall(s)
