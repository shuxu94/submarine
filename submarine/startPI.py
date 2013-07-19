import communication

host = ''
port = 8888

socket = communication.PIsocket(host, port)

while 1:
	print socket.getMessage()