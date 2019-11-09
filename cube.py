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
			print "Face inserted were valid"
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

	def stringify(self):
		cubeStr=""
		for i in range(0,6):
			for nameFace in indexFaces: 
				if indexFaces[nameFace] == i :
					cubeStr+=self.faceList[nameFace].stringify();
		return cubeStr

	def rotateClockWise(self, triplet1, triplet2, triplet3, triplet4):
		savedTriplet = [' ', ' ',  ' ']
		#. save triplet4 
		savedTriplet = triplet4
		#. move triplet3 	into 	triplet4
		triplet4 = triplet3
		#. move triplet2 	into 	triplet3
		triplet3 = triplet2
		#. move triplet1 	into 	triplet2
		triplet2 = triplet1
		#. move saved 		into 	triplet1
		triplet1 = savedTriplet
		return triplet1, triplet2, triplet3, triplet4

	def rotateCounterClockWise(self, triplet1, triplet2, triplet3, triplet4):
		savedTriplet = [' ', ' ',  ' ']
		#1. save triplet1
		savedTriplet = triplet1 	
		#1. move triplet2 	into 	triplet1
		triplet1 = triplet2
		#1. move triplet3 	into 	triplet2
		triplet2 = triplet3
		#1. move triplet4 	into 	triplet3
		triplet3 = triplet4
		#1. move saved 		into 	triplet4
		triplet4 = savedTriplet
		return triplet1, triplet2, triplet3, triplet4

	def executeMove(self,move):
		if move=="UL" :#TopLeft":
			print(" no moves so far")
			t1 = self.faceList['rear'].getTopTriplet()
			t2 = self.faceList['right'].getTopTriplet()
			t3 = self.faceList['front'].getTopTriplet()
			t4 = self.faceList['left'].getTopTriplet()
			[ t1,t2,t3,t4 ]	 = self.rotateClockWise( t1,t2,t3,t4 )
			self.faceList['rear'].setTopTriplet(t1)
			self.faceList['right'].setTopTriplet(t2)
			self.faceList['front'].setTopTriplet(t3)
			self.faceList['left'].setTopTriplet(t4)
			
			self.faceList['top'].rotateFaceClockWise()
		if move=="UR" :#"TopRight":
			t1 = self.faceList['rear'].getTopTriplet()
			t2 = self.faceList['right'].getTopTriplet()
			t3 = self.faceList['front'].getTopTriplet()
			t4 = self.faceList['left'].getTopTriplet()
			[ t1,t2,t3,t4 ]	 = self.rotateCounterClockWise( t1,t2,t3,t4 )
			self.faceList['rear'].setTopTriplet(t1)
			self.faceList['right'].setTopTriplet(t2)
			self.faceList['front'].setTopTriplet(t3)
			self.faceList['left'].setTopTriplet(t4)
			
			self.faceList['top'].rotateFaceCounterClockWise()

		if move == "LU" :#"LeftUp":
			print( " NOT FULLY TESTED")
			t1 = self.faceList['top'].getLeftTriplet()
			t2 = self.faceList['front'].getLeftTriplet()
			t3 = self.faceList['bottom'].getLeftTriplet()
			t4 = self.faceList['rear'].getRightTriplet()
			[ t1,t2,t3,t4 ]	 = self.rotateCounterClockWise( t1,t2,t3,t4 )
			self.faceList['top'].setLeftTriplet(t1)
			self.faceList['front'].setLeftTriplet(t2)
			self.faceList['bottom'].setLeftTriplet(t3)
			self.faceList['rear'].setRightTriplet(t4)
			
			self.faceList['left'].rotateFaceCounterClockWise()

		if move == "LD" :#"LeftDown":
			t1 = self.faceList['top'].getLeftTriplet()
			t2 = self.faceList['front'].getLeftTriplet()
			t3 = self.faceList['bottom'].getLeftTriplet()
			t3.reverse()
			t4 = self.faceList['rear'].getRightTriplet()
			t4.reverse()
			[ t1,t2,t3,t4 ]	 = self.rotateClockWise( t1,t2,t3,t4 )
			self.faceList['top'].setLeftTriplet(t1)
			self.faceList['front'].setLeftTriplet(t2)
			self.faceList['bottom'].setLeftTriplet(t3)
			self.faceList['rear'].setRightTriplet(t4)
			
			self.faceList['left'].rotateFaceClockWise()

		if move=="FC" :#"FrontClockWise":	
			t1 = self.faceList['top'].getBottomTriplet()
			t2 = self.faceList['right'].getLeftTriplet()
			t2.reverse()
			t3 = self.faceList['bottom'].getTopTriplet()
			t4 = self.faceList['left'].getRightTriplet()
			t4.reverse()
			[ t1,t2,t3,t4 ]	 = self.rotateClockWise( t1,t2,t3,t4 )
			self.faceList['top'].setBottomTriplet(t1)
			self.faceList['right'].setLeftTriplet(t2)
			self.faceList['bottom'].setTopTriplet(t3)
			self.faceList['left'].setRightTriplet(t4)
			self.faceList['front'].rotateFaceClockWise()

		if move=="FA" :#FrontCounterClockWise"
			t1 = self.faceList['top'].getBottomTriplet()
			t1.reverse()
			t2 = self.faceList['right'].getLeftTriplet()
			t3 = self.faceList['bottom'].getTopTriplet()
			t3.reverse()
			t4 = self.faceList['left'].getRightTriplet()
			[ t1,t2,t3,t4 ]	 = self.rotateCounterClockWise( t1,t2,t3,t4 )
			self.faceList['top'].setBottomTriplet(t1)
			self.faceList['right'].setLeftTriplet(t2)
			self.faceList['bottom'].setTopTriplet(t3)
			self.faceList['left'].setRightTriplet(t4)
			self.faceList['front'].rotateFaceCounterClockWise()

		if move == "RU" :#"RightUp":
			t1 = self.faceList['top'].getRightTriplet()
			t2 = self.faceList['rear'].getLeftTriplet()
			t3 = self.faceList['bottom'].getRightTriplet()
			t4 = self.faceList['front'].getRightTriplet()
			[ t1,t2,t3,t4 ]	 = self.rotateClockWise( t1,t2,t3,t4 )
			self.faceList['top'].setRightTriplet(t1)
			t2.reverse()
			self.faceList['rear'].setLeftTriplet(t2)
			t3.reverse()
			self.faceList['bottom'].setRightTriplet(t3)
			#t4.reverse()
			self.faceList['front'].setRightTriplet(t4)
			
			self.faceList['right'].rotateFaceClockWise()

		if move == "RD" :#"RightDown":
			print( " NOT FULLY TESTED")
			t1 = self.faceList['top'].getRightTriplet()
			t2 = self.faceList['rear'].getLeftTriplet()
			t3 = self.faceList['bottom'].getRightTriplet()
			t4 = self.faceList['front'].getRightTriplet()
			[ t1,t2,t3,t4 ]	 = self.rotateCounterClockWise( t1,t2,t3,t4 )
			t1.reverse()
			self.faceList['top'].setRightTriplet(t1)
			self.faceList['rear'].setLeftTriplet(t2)
			self.faceList['bottom'].setRightTriplet(t3)
			self.faceList['front'].setRightTriplet(t4)
			
			self.faceList['right'].rotateFaceCounterClockWise()

		if move== "BC" :#"RearClockWise":
			t1 = self.faceList['top'].getTopTriplet()
			t2 = self.faceList['left'].getLeftTriplet()
			t3 = self.faceList['bottom'].getBottomTriplet()
			t4 = self.faceList['right'].getRightTriplet()			
			[ t1,t2,t3,t4 ]	 = self.rotateCounterClockWise( t1,t2,t3,t4 )
			self.faceList['top'].setTopTriplet(t1)
			self.faceList['left'].setLeftTriplet(t2)
			t3.reverse()
			self.faceList['bottom'].setBottomTriplet(t3)
			self.faceList['right'].setRightTriplet(t4)
			
			self.faceList['rear'].rotateFaceCounterClockWise()

		if move=="BA" :#"RearCounterClockWise":
			t1 = self.faceList['top'].getTopTriplet()
			t2 = self.faceList['left'].getLeftTriplet()
			t3 = self.faceList['bottom'].getBottomTriplet()
			t4 = self.faceList['right'].getRightTriplet()			
			[ t1,t2,t3,t4 ]	 = self.rotateClockWise( t1,t2,t3,t4 )
			self.faceList['top'].setTopTriplet(t1)
			self.faceList['left'].setLeftTriplet(t2)
			t3.reverse()
			self.faceList['bottom'].setBottomTriplet(t3)
			self.faceList['right'].setRightTriplet(t4)
			
			self.faceList['rear'].rotateFaceClockWise()


		if move=="DL" :#"BottomLeft":
			t1 = self.faceList['front'].getBottomTriplet()
			t2 = self.faceList['right'].getBottomTriplet()
			t3 = self.faceList['rear'].getBottomTriplet()
			t4 = self.faceList['left'].getBottomTriplet()
			[ t1,t2,t3,t4 ]	 = self.rotateCounterClockWise( t1,t2,t3,t4 )
			self.faceList['front'].setBottomTriplet(t1)
			self.faceList['right'].setBottomTriplet(t2)
			self.faceList['rear'].setBottomTriplet(t3)
			self.faceList['left'].setBottomTriplet(t4)
			
			self.faceList['bottom'].rotateFaceCounterClockWise()
		
		if move=="DR" : #"BottomRight":
			t1 = self.faceList['front'].getBottomTriplet()
			t2 = self.faceList['right'].getBottomTriplet()
			t3 = self.faceList['rear'].getBottomTriplet()
			t4 = self.faceList['left'].getBottomTriplet()
			[ t1,t2,t3,t4 ]	 = self.rotateClockWise( t1,t2,t3,t4 )
			self.faceList['front'].setBottomTriplet(t1)
			self.faceList['right'].setBottomTriplet(t2)
			self.faceList['rear'].setBottomTriplet(t3)
			self.faceList['left'].setBottomTriplet(t4)
			
			self.faceList['bottom'].rotateFaceClockWise()