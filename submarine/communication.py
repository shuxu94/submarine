import serial
import threading
import socket
import thread
import sensor
import time
import devicepath
import sys

#  Sensor data coming in in the following form:
#  x-coordinate, y-coordinate, compassx, compassy, temperature
class ListeningThread(threading.Thread):#  This is used to listen for messages
	def __init__(self, Commsocket):
		threading.Thread.__init__(self)
		self.socket = Commsocket
		self.reciever = []
	def run(self):
		while 1:
			self.msg = self.socket.getMessage()
 			self.send(self.msg)
 			
 	def addReciever(self, reciever):
 		self.reciever.append(reciever)

 	def send(self, message):
 		for i in self.reciever:
 			i.message = message
		
class Reciever(object):#  this is used to read from ListeningThread
	def __init__(self):#  use either this object or an inheritance of it
		self.message = None
	

class PIsocket(socket.socket):#  PIsocket is the server side 
							  #  User datagram 
	'''Socket to be used on PI, UDP server'''
	def __init__(self, ip, port):
		super(PIsocket, self).__init__(socket.AF_INET, socket.SOCK_DGRAM)
		self.ip = ip
		self.port = port
		try:
			self.bind((self.ip, self.port))
		except socket.error, msg:
			print 'socket error'
			sys.exit()
	def start(self):#   this has to start before compsocket
		while 1:
			self.garbage, self.addr = self.recvfrom(1024)
			print 'recieved inside() ' + self.garbage
			if len(self.garbage) > 0:
				self.garbage = None
 				self.sendMessage('msg by pi')
 				print 'confirmed break'
 				break

	def sendMessage(self, message):
		self.sendto(message, self.addr)
	def getMessage(self):
		self.data, self.addr = self.recvfrom(1024)
		return self.data
	def getAddress(self):
		return self.addr
		
		
class Compsocket(socket.socket):
	'''Socket to be used on the Computer; UDP client'''
	def __init__(self, ip, port):
		super(Compsocket, self).__init__(socket.AF_INET, socket.SOCK_DGRAM)
		self.ip = ip
		self.port = port
		
	def start(self):
		while 1:
			self.sendto('msg by comp',(self.ip, self.port))
			self.garbage, self.addr = self.recvfrom(1024)
			print 'recieved inside start() ' + self.garbage
			if len(self.garbage) > 0:
				self.garbage = None
				print 'confirmed break'
				break

	def sendMessage(self, message):
		self.sendto(message, (self.ip, self.port))

	def getMessage(self):
		self.data, self.addr = self.recvfrom(1024)
		return self.data
	def getAddress(self):
		return self.addr
		
class Serial(object):
	'''Serial object connecting pi to arduino'''
	def __init__(self, devicepath, brate, tout):
		self.Serial = serial.Serial(devicepath, baudrate = brate, timeout = tout)

	def getMessage(self, tout = None):
		if tout == None: #  if no tout is selected
			stop = time.time()+3 #  used as a timer
			while time.time() < stop:
				data = self.Serial.realline()
				data = data.split
				if len(data) == 5: #  makes sure that all the data
								   #  is received.
					return data
		elif tout != None: #  if tout is selected
			stop = time.time()+tout
			while time.time() < stop:
				data = self.Serial.realline()
				data = data.split()
				if len(data) == 5:
					return data
				
	def sendMessage(self, message):
		self.Serial.write(message)

# 	def getMessage(self):
# 		return self.Serial.readline() #chang it to a serial subclass

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
