import communication
import time
#host = '192.168.234.234'
host = 'localhost'
port = 8888

socket = communication.Compsocket(host,port)

while 1:
	socket.start()
	print socket.getMessage()