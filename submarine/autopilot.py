from sensor import GPScoord

class Autopilot(object):
	def __init__(self, submarine):
		self.submarine = submarine

	def goHere(self, location):
		self.desx = location.x
		self.dexy = location.y
		self.des = location
		self.currentlocation = self.submarine.sensor.getLatestLocation()
			 #  location is a gps object
	
	def goHere(self, x, y):
		self.desx = x
		self.desy = y
		self.des = GPScoord(x, y)
		self.currentlocation = self.submarine.sensor.getLatestLocation()
		
	
	def maintainSpeed(self, speed):
		self.desiredSpeed = speed
		self.currentSpeed = self.submarine.sensor.getLastestSpeed()
		
	def maintainHeading(self, heading):
		self.desiredHeading = heading
		self.currentHeading = self.sumbarine.sensor.getLatestHeading()
	
	def setBase(self, coord):
		self.basex = coord.x
		self.basey = coord.y
	
	def setBase(self, x, y):
		self.basex = x
		self.basey = y
	def distanceToDes

def main():
	pass


if __name__ == "__main__":
	main()