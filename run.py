from cube import Cube
from face import Face
from solver import CubeSolver


print("MISSING : evaluation INPUTS")
print("MISSING : testing sul cubo")
import pickle

s=CubeSolver(solverPath="/home/pi/rubik/solver/cubex")

in1 = str(raw_input("Want to load a cube configuration? [Y/N]"))
if in1 == "Y" or in1 == "y":
	s=pickle.load(open("solver.p",'r'))
	print("Configuration loaded")
	s.cube.verifyFaces()
	s.cube.printCube()
else:
	s.getUserInput()
	s.cube.verifyFaces()
	s.cube.printCube()
	in1 = str(raw_input("Want to save this cube configuration? [Y/N]"))
	if in1 == "Y" or in1 == "y":
		pickle.dump(s, open("solver.p",'wb'))
		print("Configuration saved")

moveList = s.solve()
print (moveList)
from moves import executeMove
s.cube.executeMove("FrontCounterClockWise")

s.cube.printCube()