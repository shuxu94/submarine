


MAX = 180
MID = 90
MIN = 0

class Autopilot(object)
	def __init__(self)
	
	
	
	def maintainSpeed(self, speed)
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