from Classes.Cube import Cube
import sys
import subprocess
import pickle
import copy

from Classes.CubeMove import CubeMove
#from Classes.MotorMovementStepList import MotorMovementStepList
from Classes.motorStepsConverter import movesConverter, getNextArmPosition, stringMoveConverter
from Classes.MotorHandlerClient import MotorHandlerClient

class CubeSolver:
    def __init__(self):
        # self.args="random"
        self.cubeSerialized = "random"
        # self.cube = Cube()
        # self.solverPath = "C:\\Users\\Stefano\\PycharmProjects\\rubik\\solver\\cubex.exe"
        self.solverPath = "C:/Users/Stefano/Documents/Progetti/rubik/solver/cubex.exe"
        # self.solverPath = "/home/pi/Desktop/ftp/rubik/solver/cubex"
        self.cubeSimulator = []
        self.cubeSimulatorMovesList = []
        self.cubeMotorSimulator = []
        self.cubeMotorMovementsList = []
        self.motorHandlerClient = MotorHandlerClient(run_server_locally=True, simulateMotors=True)
        self.currentMotorMovementPos = 0
        # self.motorHandler("192.168.1.1", 80)

        cube = Cube()
        self.cubeSimulator.append(cube)
        self.cubeMotorSimulator.append(cube)

    def getUserInput(self):
        cube = Cube()
        cube.getCubeFromUser()
        self.cubeSimulator.clear()
        self.cubeSimulator.append(cube)
        self.cubeMotorSimulator.clear()
        self.cubeMotorSimulator.append(cube)#{"cube": self.cube, "armPosition": "GO"})

    def setSolverFromString(self, stringArray):
        cube = Cube()
        res = cube.setCubeFromString(stringArray)
        self.cubeSimulator.clear()
        self.cubeSimulator.append(cube)
        self.cubeMotorSimulator.clear()
        self.cubeMotorSimulator.append(cube)#{"cube": cube, "armPosition": "GO"})
        return res

    def saveCube(self, fileName):
        pickle.dump(self.cubeSimulator[0], open(fileName + ".p", 'wb'))

    def loadCube(self, fileName):
        cube = pickle.load(open(fileName + ".p", 'rb'))
        self.cubeSimulator.clear()
        self.cubeSimulator.append(cube)
        self.cubeMotorSimulator.clear()
        self.cubeMotorSimulator.append(cube)#{"cube": cube, "armPosition": "GO"})

    def printCube(self, step):
        self.cubeSimulator[step].printCube()

    def verifyFaces(self, step):
        self.cubeSimulator[step].verifyFaces()

    def isAlreadySolved(self):
        if (len(self.cubeSerialized) != 6 * 9):
            print("Error : inputSolverString")
            exit()
        else:
            equalsSubString = 0
            for i in range(6):
                partialString = self.cubeSerialized[i * 9:(i + 1) * 9]
                firstC = partialString[4]
                if partialString == firstC * 9:
                    equalsSubString += 1;
            if equalsSubString == 6:
                return True
            else:
                return False

    def solve(self):
        self.cubeSerialized = self.cubeSimulator[0].serialize()

        if self.isAlreadySolved():
            print("*" * 80)
            print("Cube already solved")
            print("*" * 80)
            return []
        # print(self.cubeString)
        try:
            print(self.solverPath + " " + self.cubeSerialized)
            p = subprocess.Popen([self.solverPath, self.cubeSerialized], stdout=subprocess.PIPE)
            (output, err) = p.communicate()
            # output = ""
        except:
            print("Unexpected Error", sys.exc_info()[0])
            return
        outputStr = str(output)
        moves = outputStr.split(", ")
        numMoves = len(moves)
        movesNoBytePrefix = list([x[-2:] for x in moves])
        moves2Char = list(filter(lambda x: len(x) == 2, movesNoBytePrefix))
        if (numMoves != len(moves2Char) + 1):
            print("Not 2 chars moves")
            print("numMoves", output)
            print("numMoves", numMoves)
            print("moves2Char", moves2Char)
            sys.exit()
        # fill simulator
        self.cubeSimulatorMovesList = []
        # moves2Char = ['UL', 'DR', 'LU']
        print(moves2Char)
        for m in moves2Char:
            mv = CubeMove(m)
            #mv = stringMoveConverter(m)
            #mv = side_dict[m[0]] + "_" + direction_dict[m[1]]
            self.cubeSimulatorMovesList.append(mv)
            cubeTmp = copy.deepcopy(self.cubeSimulator[-1])  # select the last cube in the array
            cubeTmp.executeMove(mv)
            self.cubeSimulator.append(cubeTmp)

        for move in self.cubeSimulatorMovesList:
            for movement in move.motor_movements_list:
                self.cubeMotorMovementsList.append(movement)
                cubeTmp = copy.deepcopy(self.cubeMotorSimulator[-1])
                cubeTmp.executeMotorStep(movement)
                self.cubeMotorSimulator.append(cubeTmp)#{"cube": cubeTmp})


        print(self.getCubeSimulatorMoves())
        print(self.getCurrentMotorMovementPos())
        print(self.getCubeAtMotorMovement(self.getCurrentMotorMovementPos()))
        #self.cubeMotorMovementsList = movesConverter(self.cubeSimulatorMovesList)

        #for movement in self.cubeMotorMovementsList:
        #    simulatorStatus = self.cubeMotorSimulator[-1]  # select the last cube in the array
        #    cubeTmp = copy.deepcopy(simulatorStatus["cube"])
        #    cubeTmp.executeMotorStep(movement)
        #    currentArmPosition = simulatorStatus["armPosition"]
        #    newArmPosition = getNextArmPosition(currentArmPosition, movement)
        #    self.cubeMotorSimulator.append({"cube": cubeTmp, "armPosition": newArmPosition})


    def getCubeSimulatorMoves(self):
        return self.cubeSimulatorMovesList

    def getCubeSimulatorMove(self, pos):
        return self.cubeSimulatorMovesList[pos]

    def getCubeAtSimulatorStep(self, pos):
        if pos == -1:
            return None
        return self.cubeSimulator[pos]

    def getNumSimulatorSteps(self):
        return len(self.cubeSimulator)

########################## MOTOR MOVEMENTS #################################
    def getMotorMovementsList(self):
        return self.cubeMotorMovementsList

    def getNumSimulatorMotorMovements(self):
        return len(self.cubeMotorSimulator)

    def getCurrentMotorMovementPos(self):
        return self.currentMotorMovementPos

    def getCurrentSingleMotorMovement(self):
        return self.cubeMotorMovementsList[self.currentMotorMovementPos]

    def getSingleMotorMovementAtPos(self, pos):
        return self.cubeMotorMovementsList[pos]

    def increaseMotorMovementPos(self):
        self.currentMotorMovementPos += 1

    def executeCurrentMovement(self):
        movement = self.getCurrentSingleMotorMovement()
        self.motorHandlerClient.executeMovement(movement=movement)

    def getCubeAtMotorMovement(self, pos):
        if pos == -1:
            return None
        return self.cubeMotorSimulator[pos]#["cube"]