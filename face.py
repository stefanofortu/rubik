
dict_allowed_input={'b': 1,
					'B': 1,
					'w': 2,
					'W': 2,
					'r': 3,
					'R': 3,
					'y': 4,
					'Y': 4,
					'o': 5,
					'O': 5,
					'g': 6,
					'G': 6}

allowed_char=dict_allowed_input.keys()


class Face:
	def __init__(self):
		self.face=[ " " for i in range(0,9)]
	
	def __init__(self,num):
		if (len(str(num))==1):
			self.face=[ str(num) for i in range(0,9)]
		elif (len(str(num))==9):
			self.initFaceFromStr(num);
		else:
			print "Cannot Initialize Face correctly"

	def initFaceFromStr(self,str):
		if ( len(str)==9 ):
			self.face=[ str[i] for i in range(0,9)]
		else:
			print "Cannot Initialize Face correctly"

	def printFace(self):
		for i in range(0,9):
			if ((i)%3 == 0):
				print "",
			print self.face[i],
			if ((i+1)%3 == 0):
				print ""

	def getFaceFromUser(self,nameFace):
		valid=False;
		while (valid == False ):
			print "============> Insert " + nameFace + " face : ",
			inputStr=raw_input();
			if len(inputStr) != 9:
				print "Insert correct number of elements"
				continue;
			numCorrectChars=0;
			for i in range(0,9):
				if inputStr[i] in allowed_char:
					numCorrectChars +=1;
			if numCorrectChars!=9:
				print "Insert valid letters"
				valid=False
				continue;
			else:
				valid=True;
		self.initFaceFromStr(inputStr)
		
	def stringify(self):
		faceNum=[ dict_allowed_input[self.face[i]] for i in range(0,9)]
		return ''.join( [str(x) for x in faceNum ] )