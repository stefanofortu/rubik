from cube import Cube
from face import Face
from solver import CubeSolver


print("MISSING : evaluation INPUTS")
print("MISSING : testing sul cubo")
import pickle


s=CubeSolver(solverPath="/home/stefano/Desktop/rubik/solver/cubex")
s.cube.printCube()
s.getUserInput()

pickle.dump(s, open("solver.p",'wb'))

s=pickle.load(open("solver.p",'r'))
###
s.solve()


