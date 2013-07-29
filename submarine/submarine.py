import communication
import sensor
import autopilot

#  the command is sent in the following format
#  motor, elevator, rudder


baudrate = 9600
timeout = 2
class Submarine(object):
	'''main object initiate this to start'''
	def __init__(self, serial):
		self.serial = serial #  communication.serial object
		self.sensor = sensor.Sensors(self.serial) #  sensor.sensor object
		self.autopilot = autopilot.Autopilot(self)
				
	def sendCommand(self):
		'''Sends the commands to arduino'''
		self.controlmessage = "%d,%d,%d\n" % (
												self.motorsetting,
												self.elevatorsetting,
												self.ruddersetting)
												
		self.serial.sendMessage(self.controlmessage)
		
	def setAllControls(self, motorsetting, elevatorsetting, ruddersetting):
		'''Sets the all the controls'''
		self.motorsetting = motorsetting	
		self.elevatorsetting = elevatorsetting
		self.ruddersetting = ruddersetting
		
		self.sendCommand()
		
	def setMotor(self, motorSetting):
 		self.motorsetting = motorsetting
 		
		self.sendCommand()
		
		
	def setElevator(self, elevatorSetting):
		self.elevatorsetting = elevatorsetting
		
		self.sendCommand()
	
	def setRudder(self, rudderSetting):
		self.rudderSetting = rudderSetting
		
		self.sendCommand()

def main():
	pass


if __name__ == "__main__":
	main()