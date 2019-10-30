
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

	def rotateFaceClockWise(self):
		# 0 | 1 | 2			# 6 | 3 | 0 
		# 3 | 4 | 5   -->   # 7 | 4 | 1
		# 6 | 7 | 8 		# 8 | 5 | 2
		faceNew=[ " " for i in range(0,9)]	
		faceNew[0]=self.face[6]
		faceNew[1]=self.face[3]
		faceNew[2]=self.face[0]
		faceNew[3]=self.face[7]
		faceNew[4]=self.face[4]
		faceNew[5]=self.face[1]
		faceNew[6]=self.face[8]
		faceNew[7]=self.face[5]
		faceNew[8]=self.face[2]
		self.face=faceNew

	def rotateFaceCounterClockWise(self):
		# 0 | 1 | 2			# 2 | 5 | 8 
		# 3 | 4 | 5   -->   # 1 | 4 | 7
		# 6 | 7 | 8 		# 0 | 3 | 6
		faceNew=[ " " for i in range(0,9)]	
		faceNew[0]=self.face[2]
		faceNew[1]=self.face[5]
		faceNew[2]=self.face[8]
		faceNew[3]=self.face[1]
		faceNew[4]=self.face[4]
		faceNew[5]=self.face[7]
		faceNew[6]=self.face[0]
		faceNew[7]=self.face[3]
		faceNew[8]=self.face[6]
		self.face=faceNew