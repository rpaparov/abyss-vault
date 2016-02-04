import socket
import errno
#from socket import error as socket_error
import json

def CompactJson(d):
	return bytes(json.dumps(d, separators=(',', ':')), 'UTF-8')

def QueryServer(tcpAdd, tcpPort, request):
	# try to connect
	try:
		soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		soc.connect((tcpAdd, int(tcpPort)))
	except socket.error as serr:
		if serr.errno != errno.ECONNREFUSED:
			raise serr
		answer = {'status' : 'error', 'message' : 'connection refused'}
		return answer
	# send query
	soc.sendall(CompactJson(request))
	# read answer
	data = soc.recv(4096)
	soc.close()
	# decode answer and return
	answer = data.decode('utf-8')
	return json.loads(answer)
