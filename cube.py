from face import Face
class Cube:
	def __init__(self):
		self.faceList = [0] *6;
		self.faceListPrint = [0] *12;
		for i in range(0,6):
			self.faceList[i] = Face(i);
		
		self.faceListPrint[0] = Face(" ")
		self.faceListPrint[1] = self.faceList[0]
		self.faceListPrint[2] = Face(" ")
		self.faceListPrint[3] = Face(" ")
		self.faceListPrint[4] = self.faceList[1]
		self.faceListPrint[5] = self.faceList[2]
		self.faceListPrint[6] = self.faceList[3]
		self.faceListPrint[7] = self.faceList[4]
		self.faceListPrint[8] = Face(" ")
		self.faceListPrint[9] = self.faceList[5]
		self.faceListPrint[10] = Face(" ")
		self.faceListPrint[11] = Face(" ")

	def printCube(self):
		for row in range(0,3):
			self.printFourFaces(row)

	def printFourFaces(self,row):
		for k in range(0,36):
			i=(k/3)%4 
			j=k%3 + 3*(k/12) 
			if (j%3==0 ):
				print "",
			print self.faceListPrint[i+4*row].face[j],
			if ((i+1)%4 == 0 ) and ((j+1)%3 == 0 ):
				print ""
#    def add_trick(self, trick):
#        self.tricks.append(trick)

