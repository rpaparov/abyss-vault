import socketserver
import json
import time
from random import choice

from common.networking import CompactJson
from common.variousTypes import RoomType

class GameServer(socketserver.ThreadingTCPServer):
	allow_reuse_address = True


class GameServerHandler(socketserver.BaseRequestHandler):
	def handle(self):
		# listen
		data = self.request.recv(64).decode('utf-8')
		print('data = ' + data)
		jsonDict = json.loads(data)
		# handle query (temporary output for debug)
		t = time.ctime()
		print('request at {}, query = {}'.format(t, data))
		
		if jsonDict.get('query') == 'update':
			idd = jsonDict.get('id')
			status = self.getStatus(idd)
		# respond
		answer = {'status' : 'ok', 'time' : t}
		answer.update(status)
		#print(answer)
		self.request.sendall(CompactJson(answer))


	def getStatus(self, idd):
		'''Get last status of shelter of given id'''
		if idd is None:
			print('unknown shelter id')
			return {}
		shelterSize = (choice(range(20, 30)), choice(range(5, 10)))
		roomTypes = {}
		for i in range(shelterSize[0]):
			for j in range(shelterSize[1]):
				key = '{},{}'.format(i, j)
				roomType = choice([RoomType.steam, RoomType.kitchen])
				roomTypes[key] = roomType
		status = {'shelterSize' : shelterSize,
		          'roomTypes' : roomTypes}
		return status
