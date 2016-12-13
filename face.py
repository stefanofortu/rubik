class Face:
	def __init__(self):
		self.face=[ " " for i in range(0,9)]
	
	def __init__(self,num):
		self.face=[ num for i in range(0,9)]

	def printFace(self):
		for i in range(0,9):
			if ((i)%3 == 0):
				print "",
			print self.face[i],
			if ((i+1)%3 == 0):
				print ""
