import communication


class Sensors(object):
	def __init__(self, submarine): #  class submarine as an argument
		self.submarine = submarine
		self.data = self.submarine.ardSerial.getMessage().split

		self.currentLocation = GPScoord(float(self.data[0]), 
										float(self.data[1]))
		self.currentHeading  = float(self.data[2])
		self.currentTemp     = float(self.data[3])
		
	def getLatestLocation(self):
		return self.currentLocation
	
	def getLatestHeading(self):
		return self.currentHeading
	
	def getLatestTemp(self):
		return self.currentTemp
	
class GPScoord(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
class Compass(object):
	def __init__(self, x,y):
		self.x = x
		self.y = y

def main():
	pass


if __name__ = "__main__":
	main()