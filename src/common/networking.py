import socket
import errno
#from socket import error as socket_error
import json

def QueryServer(tcpAdd, tcpPort, request):
	# format query
	r = bytes(json.dumps(request), 'UTF-8')
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
	soc.sendall(r)
	# read answer
	data = soc.recv(1024)
	soc.close()
	# decode answer and return
	answer = data.decode('utf-8')
	return json.loads(answer)
