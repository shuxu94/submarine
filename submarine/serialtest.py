import communication
import devicepath

testserial = communication.Serial(devicepath.Pi, 9600, 2)
while 1:
	testserial.sendMessage('1600,1600,1600')