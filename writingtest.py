import serial
import communication
testserial = serial.Serial(communication.ShusMacdevicePath1, 9600, timeout = 2)


while 1:
	testserial.write('2000, 2000')