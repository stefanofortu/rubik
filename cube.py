from face import Face
from face import dict_allowed_input
from termcolor import colored,cprint
	
indexFaces={ 	'top'   : 0,
				'left'  : 1,
				'front' : 2,
				'right' : 3,
				'rear'  : 4,
				'bottom'  : 5}	

colorFace={		'b': ['blue'],
				'w': ['white'],
				'r': ['red'],
				'y': ['yellow'],
				'o': ['yellow', "on_red"],
				'g': ['green']}
class Cube:
	def __init__(self):
		self.faceList = {}
		self.faceListPrint = [0] *12;
		string="bwryog"
		for name in indexFaces: #range(0,6):
			self.faceList[name] = Face(string[indexFaces[name]]);

	######### PRINTING ##########################
	def prepareForPrint(self):		     
		self.faceListPrint[0] = Face(" ")
		self.faceListPrint[1] = self.faceList['top']
		self.faceListPrint[2] = Face(" ")
		self.faceListPrint[3] = Face(" ")
		self.faceListPrint[4] = self.faceList['left']
		self.faceListPrint[5] = self.faceList['front']
		self.faceListPrint[6] = self.faceList['right']
		self.faceListPrint[7] = self.faceList['rear']
		self.faceListPrint[8] = Face(" ")
		self.faceListPrint[9] = self.faceList['bottom']
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
				if len(colorFace[charToPrint.lower()])==1:
					print colored(charToPrint,colorFace[charToPrint.lower()][0], attrs=['bold']),
				else:
					print colored(charToPrint,colorFace[charToPrint.lower()][0],colorFace[charToPrint.lower()][1], attrs=['bold']),
			if ((i+1)%4 == 0 ) and ((j+1)%3 == 0 ):
				print ""
	def printCube(self):
		for row in range(0,3):
			self.printFourFaces(row)

	######### INPUT ##########################
	def verifyFaces(self):
		colorList=list(set([x.lower() for x in dict_allowed_input.keys()]))
		numRipetition = [0] *6;
		for nameFace in indexFaces:
			for j in range(0,9):
				numRipetition[ colorList.index(self.faceList[nameFace].face[j].lower()) ] +=1;
		numRipetition = filter(lambda x: x == 9,numRipetition)
		#print numRipetition
		if len(numRipetition) == 6:
			print "Cube faces are valid"
			return True
		else:
			print "FACES NOT VALID"
			return False

	def getCubeFromUser(self):
		for i in range(0,6):
			print("     top")
			print("left-front-right-rear")
			print("     bottom")
			for nameFace in indexFaces: 
				if indexFaces[nameFace] == i :
						self.faceList[nameFace].getFaceFromUser(nameFace);

	######### STRINGIFY ##########################
	def CharToNum(self):
		for nameFace in indexFaces:
			self.faceList[nameFace].CharToNum();

	def stringify(self):
		self.CharToNum()
		cubeStr=""
		for i in range(0,6):
			for nameFace in indexFaces: 
				if indexFaces[nameFace] == i :
					cubeStr+=self.faceList[nameFace].stringify();
		return cubeStr
