from submarine.communication import *
from submarine.sumbmarine import *
import time


testserial = communication.Serial(Shusmac1, 9600, 2)
stop = time.time() + 10
while time.time() < stop:
		print serial.getMessage