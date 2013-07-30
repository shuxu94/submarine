import thread.Treading


MAX = 180
MID = 90
MIN = 0

class Autopilot(thread.Threading):
	def __init__(self):
		pass
	
	def run(self):
		
	
	def addSub(self, submarine):
		self.submarine = submarine
	
	def goHere(self, x, y, speed):
		
	
	
	
	def maintainSpeed(self, speed):
		self.targetSpeed = speed
		self.currentSpeed = sensor.getCurrentSpeed
		
		if self.currentSpeed = self.targetSpeed:
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