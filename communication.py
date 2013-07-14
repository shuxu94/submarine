import serial
import socket
import thread
import time

#  Sensor data coming in in the following form:
#  x-coordinate, y-coordinate, compassx, compassy, temperature



class PIsocket(socket.socket):
	pass
	
class Compsocket(socket.socket):
	pass

	
class Serial(object):
	def __init__(self, devicepath, brate, tout):
		self.Serial = serial.Serial(devicepath, baudrate = brate, timeout = tout)

	def getMessage(self):
		stop = time.time()+3
		while time.time() < stop:
			data = self.Serial.realline()
			if len(data) == 5:
				return data
				
	def sendMessage(self, message):
		self.Serial.write(message)

	def readline(self):
		return self.Serial.readline() #chang it to a serial subclass

