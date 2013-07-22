import communications
import devicepath

testserial = communications.Serial(Pi, 9600, 2)
while 1:
	testserial.sendMessage('1600,1600,1600')