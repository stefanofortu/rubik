from face import Face
from face import dict_allowed_input
from termcolor import colored,cprint

indexFaces={ 	0 : 'top',
				1 :	'left',
				2 :	'front',
				3 :	'right',
				4 :	'back',
				5 :	'bottom'}

colorFace={		'b': 'blue',
				'w': 'white',
				'r': 'red',
				'y': 'yellow',
				'o': 'magenta',
				'g': 'green'}
class Cube:
	def __init__(self,debug=False):
		self.faceList = [0] *6;
		self.faceListPrint = [0] *12;
		if debug:
			for i in range(0,6):
				self.faceList[i] = Face(i);
		else:
			string="bwryog"
			for i in range(0,6):
				self.faceList[i] = Face(string[i]);
		self.verifyFaces()

	######### PRINTING ##########################
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
			charToPrint=self.faceListPrint[i+4*row].face[j]
			if charToPrint==" ":
				print charToPrint,
			else:
				print colored(charToPrint,colorFace[charToPrint.lower()]),
			if ((i+1)%4 == 0 ) and ((j+1)%3 == 0 ):
				print ""
	def printCube(self):
		for row in range(0,3):
			self.printFourFaces(row)

	######### INPUT ##########################
	def verifyFaces(self):
		colorList=list(set([x.lower() for x in dict_allowed_input.keys()]))
		numRipetition = [0] *6;
		for i in range(0,6):
			for j in range(0,9):
				numRipetition[ colorList.index(self.faceList[i].face[j].lower()) ] +=1;
		numRipetition = filter(lambda x: x == 9,numRipetition)
		print numRipetition
		if len(numRipetition) == 6:
			print "Face inserted were valid"
			return True
		else:
			print "FACES NOT VALID"
			return False

	def getCubeFromUser(self):
		for i in range(0,6):
			self.faceList[i] = Face(" ")
			print("============> Insert %s face " %(indexFaces[i]))
			self.faceList[i].getFaceFromUser(i);
		
		self.printCube()

	######### STRINGIFY ##########################
	def CharToNum(self):
		for i in range(0,6):
			self.faceList[i].CharToNum();

	def stringify(self):
		self.CharToNum()
		cubeStr=""
		for f in self.faceList:
			cubeStr+=f.stringify();
		return cubeStr