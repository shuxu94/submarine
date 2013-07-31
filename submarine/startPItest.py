import communication
import time
import submarine
import devicepath

host = ''
port = 8888
baud = 9600
timeout = 2
oldmessage = ''

socket = communication.PIsocket(host, port)
serial = communication.Serial(devicepath.Pi, baud, timeout)
sub1 = submarine.Submarine(serial)
controlReciever = communication.Reciever()

socket.start()
try:
	listen = communication.ListeningThread(socket)
	listen.daemon=True
	listen.start()
	listen.addReciever(controlReciever)

except (KeyboardInterrupt, SystemExit):
	print '\n! Received keyboard interrupt, quitting threads.\n'

while 1:
	data = sub1.sensor.getData()
	print data
	if controlReciever.message == None:
		continue
	if controlReciever.message == oldmessage:
		continue
	else:
		message = controlReciever.message
		print message
		sub1.serial.sendMessage(message)
		oldmessage = message