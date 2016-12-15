from cube import Cube

side_dict={'U':"Top", 'D':"Bottom", 'L':"Left", 'R':"Right", 'F':"Front", 'B':"Back"}
direction_dict={'L':"Left", 'R':"Right", 'U':"Up", 'D':"Down", 'C':"Clockwise", 'A':"Counterclockwise"}



class Solver:
	def __init__(self):
		#self.args="random"
		self.movesString="random"
		self.cube=Cube()

	def getUserInput(self):
		self.cube.getCubeFromUser()
		self.cube.printCube()

	def solve(self,result):
		#print result
		moves=result.split(", ")
		numMoves=len(moves);
		moves_ok = filter(lambda x: len(x) == 2,moves)
		if ( numMoves != len(moves_ok)  +1 ):
			print "Not 2 chars moves"
			exit();
		#numMoves = len(moves_ok)
		for num, m in enumerate(moves_ok):
			print str(num) +" : move " + side_dict[m[0]] + " " +  direction_dict[m[1]]
		#with open('file.csv', 'rb') as f:
		#    reader = csv.reader(f)
		#    your_list = list(reader)

