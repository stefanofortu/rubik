from cube import Cube
import sys
import subprocess


side_dict={'U':"Top", 'D':"Bottom", 'L':"Left", 'R':"Right", 'F':"Front", 'B':"Rear"}
direction_dict={'L':"Left", 'R':"Right", 'U':"Up", 'D':"Down", 'C':"Clockwise", 'A':"Counterclockwise"}



class CubeSolver:
	def __init__(self,solverPath):
		#self.args="random"
		self.cubeString="random"
		self.cube=Cube()
		self.solverPath=solverPath

	def getUserInput(self):
		self.cube.getCubeFromUser()

	def isAlreadySolved(self):
		if (len(self.cubeString)!=6*9):
			print("Error : inputSolverString")
			exit()
		else:
			equalsSubString=0
			for i in range(6):
				partialString=self.cubeString[i*9:i*9+6]
				firstC=partialString[0]
				if partialString== firstC*6:
					equalsSubString+=1;
			if equalsSubString==6:
				return True
			else:
				return False

	def solve(self):
		self.cubeString=self.cube.stringify()
		
		if self.isAlreadySolved():
			print("*"*80)
			print("Cube already solved")
			print("*"*80)
			return
		# print(self.cubeString)
		try:
			p = subprocess.Popen([self.solverPath, self.cubeString], stdout=subprocess.PIPE)
			(output, err) = p.communicate()
		except:
			print("Unexpected Error", sys.exc_info()[0])
			return            
		outputStr=str(output)        
		moves=outputStr.split(", ")
		numMoves=len(moves);
		movesNoBytePrefix = list([ x[-2:] for x in moves])
		moves2Char = list(filter(lambda x: len(x) == 2,movesNoBytePrefix))
		if ( numMoves != len(moves2Char)  +1 ):
			print ("Not 2 chars moves")
			sys.exit()
		movesVerbose = []
		for m in moves2Char:
			movesVerbose.append(side_dict[m[0]] + "_" +  direction_dict[m[1]])
		return movesVerbose
