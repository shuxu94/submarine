import communication
import time

host = ''
port = 8888

socket = communication.PIsocket(host, port)
socket.start()
try:
	listen = communication.ListeningThread(socket)
	listen.daemon=True
	listen.start()

except (KeyboardInterrupt, SystemExit):
	print '\n! Received keyboard interrupt, quitting threads.\n'
while 1:
#	time.sleep(2)
	msg = raw_input('Enter message: ')
	print 'sending: ' + msg
	socket.sendMessage(msg)