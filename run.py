from solver import CubeSolver
import sys
import pickle

print("MISSING : evaluation INPUTS")
print("MISSING : testing sul cubo")

# solverPath="/home/pi/rubik/solver/cubex")
solverPath = "C:\\Users\\Stefano\\Progetti\\rubik\\solver\\cubex"
s = CubeSolver()

in1 = str(input("Want to load a cube configuration? [Y/N]"))
if in1 == "Y" or in1 == "y":
    s = pickle.load(open("solver.p", 'rb'))
    print("Configuration loaded")
    s.cube.verifyFaces()
    s.cube.printCube()
else:
    s.getUserInput()
    s.cube.verifyFaces()
    s.cube.printCube()
    in1 = str(input("Want to save this cube configuration? [Y/N]"))
    if in1 == "Y" or in1 == "y":
        pickle.dump(s, open("solver.p", 'wb'))
        print("Configuration saved")

moveList = s.solve(solverPath=solverPath)

# from moves import executeMove
for n, move in enumerate(moveList):
    print(str(n) + " : move " + move)
    s.cube.executeMove(move)
    s.cube.printCube()
