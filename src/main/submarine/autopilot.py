import threading
import navigation

MAX = 180
MID = 90
MIN = 0

class Autopilot(threading.Thread):
	def __init__(self):
		pass
	
	def run(self):
		pass
		
	
	def addSub(self, submarine):
		self.submarine = submarine
	
	def goHere(self, x, y, speed):
		self.desx = x
		self.desy = y
		course = navigation.Course(self.desx, self.desy)
		
	
	
	
	def maintainSpeed(self, speed):
		self.targetSpeed = speed
		self.currentSpeed = sensor.getCurrentSpeed
		
		if self.currentSpeed == self.targetSpeed:
			pass
		elif self.currentSpeed > self.targetSpeed:
			difference = math.fabs(self.currentSpeed - self.targetSpeed)
			motorsetting = getMotorsetting - difference
			if motorsetting < MID:
				motorsetting = MID
				setMotor(motorsetting)
			else:
				setMotor(motorsetting)
			
		elif self.currentSpeed < self.targetSpeed:
			difference = math.fabs(self.currentSpeed - self.targetSpeed)
			motorsetting = getMotorsetting + difference
			if motorsetting > MAX:
				motorsetting = MAX
				setMotor(motorsetting)
			else:
				setMotor(motorsetting)