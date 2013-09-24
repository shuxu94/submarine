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
	temp = sub1.sensor.getLatestTemp()
	print temp
	if controlReciever.message == None:
		continue
	elif controlReciever.message == oldmessage:
		continue
	else:
		message = controlReciever.message
		print message
		sub1.serial.sendMessage(message)
		oldmessage = message

#  sub1.setCourse(xcoord, ycoord)
#  sub1.startCourse()
#  if sub1.isCourseFinished == true
#  sub1.setCourse(xcoord2, ycoord2)

		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		