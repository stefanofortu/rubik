from solver import CubeSolver
import sys
import pickle

s = CubeSolver()

inUnser = "L"
while inUnser.lower() != "e":
    inUnser = str(input("What you want to do?[S]:Save,[L]Load,[I]:Insert,[R]:Resolve],[E]:Exit : "))
    if inUnser.lower() == "l":
        s.loadCube('combo39moves')
        s.verifyFaces(step=0)
        s.printCube(step=0)
    elif inUnser.lower() == "i":
        s.getUserInput()
        s.verifyFaces(step=0)
        s.printCube(step=0)
    elif inUnser.lower() == "s":
        s.saveCube('combo39moves')
        print("Configuration saved")
    elif inUnser.lower() == "r":
        s.solve()
        moveList = s.getCubeSimulatorMoves()
        # motorMovementList = s.getMotorMovements()
        # from moves import executeMove
        for n, move in enumerate(moveList):
            print(str(n) + " : move " + move)
            s.printCube(step=n)
    else:
        print("Choice not valid. Try again")

print("Program ended")
