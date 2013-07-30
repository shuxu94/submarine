class Course(object):
	def __init__(self, desx, desy):
		self.desx = desx
		self.desy = desy
	
	def setStart(self, startx, starty):
		self.startx = startx
		self.starty = starty
	
	def distanceOffCourse(self, currentx, currenty):
		#  using the projection forumla to find the distance
		#  away from the intended course
		self.desx = desx - self.startx
		self.desy = desy - self.startx
		self.currentx = currentx - self.startx
		self.currenty = currenty - self.starty
		adotb = (self.desx*self.currentx) + (self.desxy*self.currenty)
		magb = math.sqrt((self.desx*self.desx) + (self.desy*self.desy))
		magbsqr = magb*magb
		projectx = (adotb/magbsqr) * self.desx
		projecty = (adotb/magbsqr) * self.desy
		disx = self.currentx - projectx
		disy = self.currenty - projecty
		distance = math.sqrt((disx*disx) + (disy*disy))
		return distance