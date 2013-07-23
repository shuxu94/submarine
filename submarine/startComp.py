import communication
import time
#host = '192.168.234.234'
host = 'localhost'
port = 8888

socket = communication.Compsocket(host,port)
socket.start()

try:
	listen = communication.ListeningThread(socket)
	listen.daemon=True
	listen.start()

except (KeyboardInterrupt, SystemExit):
	print '\n! Received keyboard interrupt, quitting threads.\n'
while 1:
	msg = raw_input('Enter message: ')
	print 'sending: ' + msg
	socket.sendMessage(msg)