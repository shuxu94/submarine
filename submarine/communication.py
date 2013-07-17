import serial
import socket
import thread
import time
import devicepath

#  Sensor data coming in in the following form:
#  x-coordinate, y-coordinate, compassx, compassy, temperature

class PIsocket(socket.socket):
	pass
	
class Compsocket(socket.socket):
	pass

	
class Serial(object):
	def __init__(self, devicepath, brate, tout):
		self.Serial = serial.Serial(devicepath, baudrate = brate, timeout = tout)

	def getMessage(self, tout = None):
		if tout == None: #  if no tout is selected
			stop = time.time()+3 #  used as a timer
			while time.time() < stop:
				data = self.Serial.realline()
				if len(data) == 5: #  makes sure that all the data
								   #  is received.
					return data
		elif tout != None: #  if tout is selected
			stop = time.time()+tout
			while time.time() < stop:
				data = self.Serial.realline()
				if len(data) == 5:
					return data
				
	def sendMessage(self, message):
		self.Serial.write(message)

	def readline(self):
		return self.Serial.readline() #chang it to a serial subclass

def main(): #  test client
	pass #  this test client will only run when connected
# 	testserial == Serial(devicepath.Shusmac1, 9600, 2)
# 	#  reading test
# 	#  runs for 7 seconds
# 	stop = time.time() + 7
# 	while time.time() < stop
# 		print testserial.getMessage(5)
# 		print testserial.getMessage
		
	

if __name__ == "__main__":
	main()