import communication
import time
host = '192.168.234.234'
port = 8888

socket = communication.Compsocket(host,port)

while 1:
	print socket.getMessage()