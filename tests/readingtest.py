import communication
import sensor
import commands
import serial
import time


testserial = serial.Serial(communication.ShusMacdevicePath1, 9600, timeout = 2)

	stop = time.time()+3
	while time.time() < stop:
		data = testserial.readline().split()
		if len(data) == 5:
			print "gpsxy = %f %f" % (float(data[0]), float(data[1]))
			print "compassxy = %f %f" % (float(data[2]), float(data[3]))
			print "tempurature = %f" % float(data[4])