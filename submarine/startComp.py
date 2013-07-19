import communication
import time
host = 'localhost'
port = 8888

socket = communication.Compsocket(host,port)

while 1:
	time.sleep(2)
	msg = str(time.time())
	print 'not socket' + msg
	socket.sendMessage(msg)
	