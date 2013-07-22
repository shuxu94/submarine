import communication
import time

host = ''
port = 8888

socket = communication.PIsocket(host, port)

while 1:
	time.sleep(2)
	msg = str(time.time())
	print 'sending: ' + msg
	socket.sendMessage(msg)