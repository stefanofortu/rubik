from Classes.Face import Face
from Classes.Face import dict_allowed_input
from termcolor import colored

indexFaces = {'top': 0,
              'left': 1,
              'front': 2,
              'right': 3,
              'rear': 4,
              'bottom': 5}

colorFace = {'b': ['blue'],
             'w': ['white'],
             'r': ['red'],
             'y': ['yellow'],
             'o': ['yellow', "on_red"],
             'g': ['green']}


class Cube:
    def __init__(self):
        self.faceList = {}
        self.faceListPrint = [0] * 12;
        string = "bwryog"
        for name in indexFaces:  # range(0,6):
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

    def printFourFaces(self, row):
        self.prepareForPrint();
        for k in range(0, 36):
            i = int(int(k / 3) % 4)
            j = int(k % 3 + 3 * int(k / 12))
            if (j % 3 == 0):
                print("", end='')
            charToPrint = self.faceListPrint[i + 4 * row].face[j]
            print(" ", end='')
            if charToPrint == " ":
                print(charToPrint, end='')
            else:
                if len(colorFace[charToPrint.lower()]) == 1:
                    print(colored(charToPrint, colorFace[charToPrint.lower()][0], attrs=['bold']), end='')
                else:
                    print(colored(charToPrint, colorFace[charToPrint.lower()][0], colorFace[charToPrint.lower()][1],
                                  attrs=['bold']), end='')
            if ((i + 1) % 4 == 0) and ((j + 1) % 3 == 0):
                print("")

    def printCube(self):
        for row in range(0, 3):
            self.printFourFaces(row)

    ######### INPUT ##########################
    def verifyFaces(self):
        colorList = list(set([x.lower() for x in dict_allowed_input.keys()]))
        numRipetition = [0] * 6;
        for nameFace in indexFaces:
            for j in range(0, 9):
                numRipetition[colorList.index(self.faceList[nameFace].face[j].lower())] += 1;
        numRipetition = list(filter(lambda x: x == 9, numRipetition))
        if len(numRipetition) == 6:
            print("Face inserted were valid")
            return True
        else:
            print("FACES NOT VALID")
            return False

    def getCubeFromUser(self):
        for i in range(0, 6):
            print("     top")
            print("left-front-right-rear")
            print("     bottom")
            for nameFace in indexFaces:
                if indexFaces[nameFace] == i:
                    self.faceList[nameFace].getFaceFromUser(nameFace)

    def setCubeFromString(self, arrayString):
        for faceName in indexFaces:
            a = self.faceList[faceName].setFaceFromString(arrayString[indexFaces[faceName]])
            if a != 0:
                return a
        return 0

    def serialize(self):
        cubeStr = ""
        for i in range(0, 6):
            for nameFace in indexFaces:
                if indexFaces[nameFace] == i:
                    cubeStr += self.faceList[nameFace].serialize()
        return cubeStr

    def stringify(self):
        cubeStr = ""
        for i in range(0, 6):
            for nameFace in indexFaces:
                if indexFaces[nameFace] == i:
                    cubeStr += self.faceList[nameFace].stringify()
        return cubeStr

    def rotateClockWise(self, triplet1, triplet2, triplet3, triplet4):
        savedTriplet = [' ', ' ', ' ']
        # . save triplet4
        savedTriplet = triplet4
        # . move triplet3 	into 	triplet4
        triplet4 = triplet3
        # . move triplet2 	into 	triplet3
        triplet3 = triplet2
        # . move triplet1 	into 	triplet2
        triplet2 = triplet1
        # . move saved 		into 	triplet1
        triplet1 = savedTriplet
        return triplet1, triplet2, triplet3, triplet4

    def rotateCounterClockWise(self, triplet1, triplet2, triplet3, triplet4):
        savedTriplet = [' ', ' ', ' ']
        # 1. save triplet1
        savedTriplet = triplet1
        # 1. move triplet2 	into 	triplet1
        triplet1 = triplet2
        # 1. move triplet3 	into 	triplet2
        triplet2 = triplet3
        # 1. move triplet4 	into 	triplet3
        triplet3 = triplet4
        # 1. move saved 		into 	triplet4
        triplet4 = savedTriplet
        return triplet1, triplet2, triplet3, triplet4

    def executeMove(self, move):
        if move == "Top_Left":  # TopLeft":
            t1 = self.faceList['rear'].getTopTriplet()
            t2 = self.faceList['right'].getTopTriplet()
            t3 = self.faceList['front'].getTopTriplet()
            t4 = self.faceList['left'].getTopTriplet()
            [t1, t2, t3, t4] = self.rotateClockWise(t1, t2, t3, t4)
            self.faceList['rear'].setTopTriplet(t1)
            self.faceList['right'].setTopTriplet(t2)
            self.faceList['front'].setTopTriplet(t3)
            self.faceList['left'].setTopTriplet(t4)

            self.faceList['top'].rotateFaceClockWise()

        elif move == "Top_Right":  # "TopRight"
            t1 = self.faceList['rear'].getTopTriplet()
            t2 = self.faceList['right'].getTopTriplet()
            t3 = self.faceList['front'].getTopTriplet()
            t4 = self.faceList['left'].getTopTriplet()
            [t1, t2, t3, t4] = self.rotateCounterClockWise(t1, t2, t3, t4)
            self.faceList['rear'].setTopTriplet(t1)
            self.faceList['right'].setTopTriplet(t2)
            self.faceList['front'].setTopTriplet(t3)
            self.faceList['left'].setTopTriplet(t4)

            self.faceList['top'].rotateFaceCounterClockWise()

        elif move == "Left_Up":  # "LeftUp":
            t1 = self.faceList['top'].getLeftTriplet()
            t2 = self.faceList['front'].getLeftTriplet()
            t3 = self.faceList['bottom'].getLeftTriplet()
            t4 = self.faceList['rear'].getRightTriplet()
            [t1, t2, t3, t4] = self.rotateCounterClockWise(t1, t2, t3, t4)
            self.faceList['top'].setLeftTriplet(t1)
            self.faceList['front'].setLeftTriplet(t2)
            t3.reverse()
            self.faceList['bottom'].setLeftTriplet(t3)
            t4.reverse()
            self.faceList['rear'].setRightTriplet(t4)

            self.faceList['left'].rotateFaceCounterClockWise()

        elif move == "Left_Down":  # "LeftDown":
            t1 = self.faceList['top'].getLeftTriplet()
            t2 = self.faceList['front'].getLeftTriplet()
            t3 = self.faceList['bottom'].getLeftTriplet()
            t3.reverse()
            t4 = self.faceList['rear'].getRightTriplet()
            t4.reverse()
            [t1, t2, t3, t4] = self.rotateClockWise(t1, t2, t3, t4)
            self.faceList['top'].setLeftTriplet(t1)
            self.faceList['front'].setLeftTriplet(t2)
            self.faceList['bottom'].setLeftTriplet(t3)
            self.faceList['rear'].setRightTriplet(t4)

            self.faceList['left'].rotateFaceClockWise()

        elif move == "Front_Clockwise":  # "FrontClockWise":
            t1 = self.faceList['top'].getBottomTriplet()
            t2 = self.faceList['right'].getLeftTriplet()
            t2.reverse()
            t3 = self.faceList['bottom'].getTopTriplet()
            t4 = self.faceList['left'].getRightTriplet()
            t4.reverse()
            [t1, t2, t3, t4] = self.rotateClockWise(t1, t2, t3, t4)
            self.faceList['top'].setBottomTriplet(t1)
            self.faceList['right'].setLeftTriplet(t2)
            self.faceList['bottom'].setTopTriplet(t3)
            self.faceList['left'].setRightTriplet(t4)
            self.faceList['front'].rotateFaceClockWise()

        elif move == "Front_Counterclockwise":
            t1 = self.faceList['top'].getBottomTriplet()
            t1.reverse()
            t2 = self.faceList['right'].getLeftTriplet()
            t3 = self.faceList['bottom'].getTopTriplet()
            t3.reverse()
            t4 = self.faceList['left'].getRightTriplet()
            [t1, t2, t3, t4] = self.rotateCounterClockWise(t1, t2, t3, t4)
            self.faceList['top'].setBottomTriplet(t1)
            self.faceList['right'].setLeftTriplet(t2)
            self.faceList['bottom'].setTopTriplet(t3)
            self.faceList['left'].setRightTriplet(t4)
            self.faceList['front'].rotateFaceCounterClockWise()

        elif move == "Right_Up":  # "RightUp":
            t1 = self.faceList['top'].getRightTriplet()
            t2 = self.faceList['rear'].getLeftTriplet()
            t3 = self.faceList['bottom'].getRightTriplet()
            t4 = self.faceList['front'].getRightTriplet()
            [t1, t2, t3, t4] = self.rotateClockWise(t1, t2, t3, t4)
            self.faceList['top'].setRightTriplet(t1)
            t2.reverse()
            self.faceList['rear'].setLeftTriplet(t2)
            t3.reverse()
            self.faceList['bottom'].setRightTriplet(t3)
            # t4.reverse()
            self.faceList['front'].setRightTriplet(t4)

            self.faceList['right'].rotateFaceClockWise()

        elif move == "Right_Down":  # "RightDown":
            t1 = self.faceList['top'].getRightTriplet()
            t2 = self.faceList['rear'].getLeftTriplet()
            t3 = self.faceList['bottom'].getRightTriplet()
            t4 = self.faceList['front'].getRightTriplet()
            [t1, t2, t3, t4] = self.rotateCounterClockWise(t1, t2, t3, t4)
            t1.reverse()
            self.faceList['top'].setRightTriplet(t1)
            t2.reverse()
            self.faceList['rear'].setLeftTriplet(t2)
            self.faceList['bottom'].setRightTriplet(t3)
            self.faceList['front'].setRightTriplet(t4)

            self.faceList['right'].rotateFaceCounterClockWise()

        elif move == "Rear_Clockwise":  # "RearClockWise":
            t1 = self.faceList['top'].getTopTriplet()
            t2 = self.faceList['left'].getLeftTriplet()
            t3 = self.faceList['bottom'].getBottomTriplet()
            t4 = self.faceList['right'].getRightTriplet()
            [t1, t2, t3, t4] = self.rotateCounterClockWise(t1, t2, t3, t4)
            t1.reverse()
            self.faceList['top'].setTopTriplet(t1)
            self.faceList['left'].setLeftTriplet(t2)
            t3.reverse()
            self.faceList['bottom'].setBottomTriplet(t3)
            self.faceList['right'].setRightTriplet(t4)

            self.faceList['rear'].rotateFaceCounterClockWise()

        elif move == "Rear_Counterclockwise":  # "RearCounterClockWise":
            t1 = self.faceList['top'].getTopTriplet()
            t2 = self.faceList['left'].getLeftTriplet()
            t3 = self.faceList['bottom'].getBottomTriplet()
            t4 = self.faceList['right'].getRightTriplet()
            [t1, t2, t3, t4] = self.rotateClockWise(t1, t2, t3, t4)
            self.faceList['top'].setTopTriplet(t1)
            t2.reverse()
            self.faceList['left'].setLeftTriplet(t2)
            # t3.reverse()
            self.faceList['bottom'].setBottomTriplet(t3)
            t4.reverse()
            self.faceList['right'].setRightTriplet(t4)

            self.faceList['rear'].rotateFaceClockWise()


        elif move == "Bottom_Left":  # "BottomLeft":
            t1 = self.faceList['front'].getBottomTriplet()
            t2 = self.faceList['right'].getBottomTriplet()
            t3 = self.faceList['rear'].getBottomTriplet()
            t4 = self.faceList['left'].getBottomTriplet()
            [t1, t2, t3, t4] = self.rotateCounterClockWise(t1, t2, t3, t4)
            self.faceList['front'].setBottomTriplet(t1)
            self.faceList['right'].setBottomTriplet(t2)
            self.faceList['rear'].setBottomTriplet(t3)
            self.faceList['left'].setBottomTriplet(t4)

            self.faceList['bottom'].rotateFaceCounterClockWise()

        elif move == "Bottom_Right":  # "BottomRight":
            t1 = self.faceList['front'].getBottomTriplet()
            t2 = self.faceList['right'].getBottomTriplet()
            t3 = self.faceList['rear'].getBottomTriplet()
            t4 = self.faceList['left'].getBottomTriplet()
            [t1, t2, t3, t4] = self.rotateClockWise(t1, t2, t3, t4)
            self.faceList['front'].setBottomTriplet(t1)
            self.faceList['right'].setBottomTriplet(t2)
            self.faceList['rear'].setBottomTriplet(t3)
            self.faceList['left'].setBottomTriplet(t4)

            self.faceList['bottom'].rotateFaceClockWise()

        else:
            print("move not found")

    def executeMotorStep(self, movement):
        if movement['motor'] == "ARM" and movement['movement'] == "flipCube":
            self.faceList['front'].rotateFaceCounterClockWise()
            self.faceList['rear'].rotateFaceClockWise()

            savedTriplet = self.faceList['left']

            self.faceList['left'] = self.faceList['top']
            self.faceList['left'].rotateFaceCounterClockWise()

            self.faceList['top'] = self.faceList['right']
            self.faceList['top'].rotateFaceCounterClockWise()

            self.faceList['right'] = self.faceList['bottom']
            self.faceList['right'].rotateFaceCounterClockWise()

            # 1. move saved 		into 	triplet4
            self.faceList['bottom'] = savedTriplet
            self.faceList['bottom'].rotateFaceCounterClockWise()

        elif movement['motor'] == "ARM" and movement['movement'] == "goUp":
            pass
        elif movement['motor'] == "ARM" and movement['movement'] == "goDown":
            pass
        elif movement['motor'] == "BASE" and movement['movement'] == "change" and movement['direction'] == +90:
            t1 = self.faceList['front'].getBottomTriplet()
            t2 = self.faceList['right'].getBottomTriplet()
            t3 = self.faceList['rear'].getBottomTriplet()
            t4 = self.faceList['left'].getBottomTriplet()
            [t1, t2, t3, t4] = self.rotateClockWise(t1, t2, t3, t4)
            self.faceList['front'].setBottomTriplet(t1)
            self.faceList['right'].setBottomTriplet(t2)
            self.faceList['rear'].setBottomTriplet(t3)
            self.faceList['left'].setBottomTriplet(t4)
            self.faceList['bottom'].rotateFaceClockWise()
        elif movement['motor'] == "BASE" and movement['movement'] == "change" and movement['direction'] == -90:
            t1 = self.faceList['front'].getBottomTriplet()
            t2 = self.faceList['right'].getBottomTriplet()
            t3 = self.faceList['rear'].getBottomTriplet()
            t4 = self.faceList['left'].getBottomTriplet()
            [t1, t2, t3, t4] = self.rotateCounterClockWise(t1, t2, t3, t4)
            self.faceList['front'].setBottomTriplet(t1)
            self.faceList['right'].setBottomTriplet(t2)
            self.faceList['rear'].setBottomTriplet(t3)
            self.faceList['left'].setBottomTriplet(t4)

            self.faceList['bottom'].rotateFaceCounterClockWise()
        elif movement['motor'] == "BASE" and movement['movement'] == "rotation" and movement['direction'] == +90:
            self.faceList['top'].rotateFaceCounterClockWise()
            self.faceList['bottom'].rotateFaceClockWise()
            temp = self.faceList['rear']
            self.faceList['rear'] = self.faceList['right']
            self.faceList['right'] = self.faceList['front']
            self.faceList['front'] = self.faceList['left']
            self.faceList['left'] = temp
        elif movement['motor'] == "BASE" and movement['movement'] == "rotation" and movement['direction'] == -90:
            self.faceList['top'].rotateFaceClockWise()
            self.faceList['bottom'].rotateFaceCounterClockWise()
            temp = self.faceList['left']
            self.faceList['left'] = self.faceList['front']
            self.faceList['front'] = self.faceList['right']
            self.faceList['right'] = self.faceList['rear']
            self.faceList['rear'] = temp
        else:
            print("move not found : executeMotorStep() " + movement['motor'] + " " + movement['movement'])
