from face import Face
class Cube:
	def __init__(self,string="bwryog"):
		self.faceList = [0] *6;
		self.faceListPrint = [0] *12;
		if string == "":
			for i in range(0,6):
				self.faceList[i] = Face(i);
		else:
			for i in range(0,6):
				self.faceList[i] = Face(string[i]);


	def printCube(self):
		for row in range(0,3):
			self.printFourFaces(row)

	def prepareForPrint(self):
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

	def printFourFaces(self,row):
		self.prepareForPrint();
		for k in range(0,36):
			i=(k/3)%4 
			j=k%3 + 3*(k/12) 
			if (j%3==0 ):
				print "",
			print self.faceListPrint[i+4*row].face[j],
			if ((i+1)%4 == 0 ) and ((j+1)%3 == 0 ):
				print ""

	def getCubeFromUser(self):
		for i in range(0,6):
			self.faceList[i] = Face(" ")
			self.faceList[i].getFaceFromUser(i);

	def CharToNum(self):
		for i in range(0,6):
			self.faceList[i].CharToNum();

	def verifyFaces(self):
		numRipetition = [0] *6;
		for i in range(0,6):
			for j in range(0,9):
				numRipetition[ self.faceList[i].face[j] ] +=1;
		numRipetition = filter(lambda x: x == 9,numRipetition)
		print numRipetition
		if len(numRipetition) == 6:
			print "Inser face were valid"
			return True
		else:
			print "FACES NOT VALID"
			return False

	def stringify(self):
		cubeStr=""
		for f in self.faceList:
			cubeStr+=f.stringify();
		return cubeStr