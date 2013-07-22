import communication
import devicepath
import time

testserial = communication.Serial(devicepath.Shusmac1, 9600, 2)
while 1:
	time.sleep(2)
	msg = '1600,1600,1600'
	print 'sending msg ' + msg
	testserial.sendMessage(msg)