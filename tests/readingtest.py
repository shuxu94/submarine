import communication
import sensor
import commands
import serial
import time
import devicepath


test serial = communication.Serial(Shusmac1, 9600, 2):
	print getMessage