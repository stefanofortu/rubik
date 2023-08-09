from Classes.UI_CubeApp import UI_CubeApp
from Classes.CubeSolver import CubeSolver
from PySide2 import QtWidgets

class CubeQtApp(UI_CubeApp, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.cubeSolver = CubeSolver()
        self.simulationStepShown = 0
        self.simulationMotorMovementShown = 0
        self.CreateNewButton.clicked.connect(self.setSolver)
        self.LoadConfigurationButton.clicked.connect(self.loadSolver)
        self.SaveConfigurationButton.clicked.connect(self.saveSolver)
        self.pushButtonSimulationSolve.clicked.connect(self.solveSimulation)
        self.pushButtonSimulationBackward.clicked.connect(self.stepBackward)
        self.pushButtonSimulationForward.clicked.connect(self.stepForward)
        self.pushButtonStartMotorMovement.clicked.connect(self.motorMovementForward)
        self.pushButtonStartAllMotorMovements.clicked.connect(self.startAllMotorMovements)

        self.moves = []  # da cancellare e sostiture con chiamata a solver

    @staticmethod
    def createHtmlForTextEditMovesList(moves, currentMove):
        htmlString = ""
        # htmlString += "<style> table, th, td { border: 1px solid black;   border-collapse: collapse;} </style>"
        htmlString += "<style> table, th, td { border-collapse: collapse;} </style>"
        htmlString += "<table width=\"100%\" height=\"100%\" style=\"font:13px\">"

        if currentMove == 0:
            htmlString += "<tr style=\" color: white; background-color:black \" ><td>" + "Start" + "</td></tr>"
        else:
            htmlString += "<tr><td>" + "Start" + "</td></tr>"

        for num, elem in enumerate(moves, start=1):
            if num == currentMove:
                htmlString += "<tr style=\" color: white; background-color:black; \" ><td>" + elem + "</td></tr>"
            else:
                htmlString += "<tr><td>" + elem + "</td></tr>"
        htmlString += "</table>"
        return htmlString

    def getCurrentCubeSimulationString(self):
        return self.cubeSolver.getCubeAtSimulatorStep(self.simulationStepShown).stringify()

    def getCurrentCubeMotorMovementString(self):
        return self.cubeSolver.getCubeAtMotorMovement(self.simulationMotorMovementShown).stringify()

    def setScrollBarStepsUpperPlace(self, pos):
        # funzione da migliorare :
        # calcolare bene le posizioni delle barre per tutti i valori
        # memorizzarle in una variabile ed evitare di ricalcolarle ogni volta
        scrollbarSteps = []
        if self.cubeSolver.getNumSimulatorSteps() <= 11:
            scrollbarSteps = [0 for i in range(self.cubeSolver.getNumSimulatorSteps())]
        else:
            for i in range(0, self.cubeSolver.getNumSimulatorSteps()):
                value = self.textEditMovesList.verticalScrollBar().minimum() + \
                        i / (self.cubeSolver.getNumSimulatorSteps() - 11) * \
                        (self.textEditMovesList.verticalScrollBar().maximum() -
                         self.textEditMovesList.verticalScrollBar().minimum())
                if value > self.textEditMovesList.verticalScrollBar().maximum():
                    value = self.textEditMovesList.verticalScrollBar().maximum()
                elif value < self.textEditMovesList.verticalScrollBar().minimum():
                    value = self.textEditMovesList.verticalScrollBar().minimum()
                scrollbarSteps.append(value)

        return scrollbarSteps[pos]

    def setScrollBarStepsLowerPlace(self, pos):
        # funzione da migliorare :
        # calcolare bene le posizioni delle barre per tutti i valori
        # memorizzarle in una variabile ed evitare di ricalcolarle ogni volta
        scrollbarSteps = []
        if self.cubeSolver.getNumSimulatorSteps() <= 11:
            scrollbarSteps = [0 for i in range(self.cubeSolver.getNumSimulatorSteps())]
        else:
            for i in range(0, self.cubeSolver.getNumSimulatorSteps()):
                value = self.textEditMovesList.verticalScrollBar().maximum() - \
                        i / (self.cubeSolver.getNumSimulatorSteps() - 11) * \
                        (self.textEditMovesList.verticalScrollBar().maximum() -
                         self.textEditMovesList.verticalScrollBar().minimum())
                if value > self.textEditMovesList.verticalScrollBar().maximum():
                    value = self.textEditMovesList.verticalScrollBar().maximum()
                elif value < self.textEditMovesList.verticalScrollBar().minimum():
                    value = self.textEditMovesList.verticalScrollBar().minimum()
                scrollbarSteps.append(value)
        scrollbarSteps.reverse()
        return scrollbarSteps[pos]

    def stepForward(self):
        # necessario leggere qui la posizione della barra barra,
        # perchè poi viene settata a zero da setHtml()
        scrollBarPosition = self.textEditMovesList.verticalScrollBar().value()

        if 0 <= self.simulationStepShown < self.cubeSolver.getNumSimulatorSteps():
            self.simulationStepShown += 1
            self.pushButtonSimulationBackward.setDisabled(False)

        if self.simulationStepShown == self.cubeSolver.getNumSimulatorSteps() - 1:
            self.pushButtonSimulationForward.setDisabled(True)
        self.widget_cubePreview.updateGui()

        htmlString = CubeQtApp.createHtmlForTextEditMovesList(self.moves, self.simulationStepShown)
        self.textEditMovesList.setHtml(htmlString)

        if scrollBarPosition < self.setScrollBarStepsLowerPlace(self.simulationStepShown):
            self.textEditMovesList.verticalScrollBar().setValue(
                self.setScrollBarStepsLowerPlace(self.simulationStepShown))
        else:
            self.textEditMovesList.verticalScrollBar().setValue(scrollBarPosition)

    def stepBackward(self):
        # necessario leggere qui la posizione della barra barra,
        # perchè poi viene settata a zero da setHtml()
        scrollBarPosition = self.textEditMovesList.verticalScrollBar().value()
        if self.simulationStepShown > 0:
            self.simulationStepShown -= 1
            self.pushButtonSimulationForward.setDisabled(False)

        if self.simulationStepShown == 0:
            self.pushButtonSimulationBackward.setDisabled(True)
        self.widget_cubePreview.updateGui()

        htmlString = CubeQtApp.createHtmlForTextEditMovesList(self.moves, self.simulationStepShown)
        self.textEditMovesList.setHtml(htmlString)

        if scrollBarPosition > self.setScrollBarStepsUpperPlace(self.simulationStepShown):
            self.textEditMovesList.verticalScrollBar().setValue(
                self.setScrollBarStepsUpperPlace(self.simulationStepShown))
        else:
            self.textEditMovesList.verticalScrollBar().setValue(scrollBarPosition)
        # self.textEditMovesList.repaint()

    def updateMotorMovementGui(self):
        updateLabels = False
        # print(str(self.motorMovementShown) + " out of " + str(self.cubeSolver.getNumMotorMovements()-1))
        simulationMotorMovementShown = self.cubeSolver.getCurrentMotorMovementPos()
        if simulationMotorMovementShown > 0:
            prevMotorMovement = self.cubeSolver.getSingleMotorMovementAtPos(simulationMotorMovementShown - 1)
            self.labelPreviousStepValue.setText(prevMotorMovement.name)
                                                #+ "  (" +
                                                #str(prevMotorMovement["moveNumber"]) + "/" +
                                                #str(self.cubeSolver.getNumSimulatorSteps() - 1) + ") ")

            # if prevMotorMovement['motor'] == "BASE":  # and nextMotorMovement['movement'] == "change":
            #    directionPrevString = " " + "{:+}".format(prevMotorMovement['direction'])
            # else:
            #     directionPrevString = ""

            #prevMotorMovementLabel = str(prevMotorMovement['motor']) + "-->" + str(prevMotorMovement['movement']) \
            #                         + directionPrevString + "  (" + str(
            #    prevMotorMovement['movementNumWithinStep']) + "/" \
            #                         + str(prevMotorMovement['totalMovementWithinStep']) + ")"
            #
            #prevMotorMovementLabel += "      (total counter: " + str(simulationMotorMovementShown) + "/" \
            #                          + str(self.cubeSolver.getNumSimulatorMotorMovements() - 1) + ")"

            prevMotorMovementLabel = str(prevMotorMovement['movement'].__dict__)

            self.labelPreviousMotorMovementValue.setText(prevMotorMovementLabel)

        if simulationMotorMovementShown < self.cubeSolver.getNumSimulatorMotorMovements() - 1:
            #nextMotorMovement = self.cubeSolver.getSingleMotorMovement(simulationMotorMovementShown)
            nextMotorMovement = self.cubeSolver.getCurrentSingleMotorMovement()
            if updateLabels:
                self.labelNextStepName.setText(nextMotorMovement["moveName"])
                if nextMotorMovement['motor'] == "BASE":  # and nextMotorMovement['movement'] == "change":
                    directionNextString = " " + "{:+}".format(nextMotorMovement['direction'])
                else:
                    directionNextString = ""
                motorMovementNameStr = str(nextMotorMovement['motor']) + "-->" + str(nextMotorMovement['movement']) + \
                    directionNextString + "  (" + str(nextMotorMovement['movementNumWithinStep']) + "/" + \
                    str(nextMotorMovement['totalMovementWithinStep']) + ")"

                self.labelNextMovementName.setText(motorMovementNameStr)
        else:
            self.labelNextStepName.setText("-")
            self.labelNextMovementName.setText("-")

    def startAllMotorMovements(self):
        for k in range(self.cubeSolver.getNumSimulatorMotorMovements()-1):
            self.motorMovementForward()

    def motorMovementForward(self):
        self.pushButtonStartMotorMovement.setDisabled(True)
        self.pushButtonStartMotorMovement.repaint()
        self.pushButtonStartAllMotorMovements.setDisabled(True)
        self.pushButtonStartAllMotorMovements.repaint()
        # self.gridLayout.update()
        # self.widget_cubeMotorResolutor.updateGui()
        if 0 <= self.simulationMotorMovementShown < self.cubeSolver.getNumSimulatorMotorMovements() - 1:
            self.simulationMotorMovementShown += 1
            self.cubeSolver.executeCurrentMovement()
            #self.simulationMotorMovementShown += 1
            self.updateMotorMovementGui()
            self.cubeSolver.increaseMotorMovementPos()

        if self.simulationMotorMovementShown >= self.cubeSolver.getNumSimulatorMotorMovements() - 1:
            self.pushButtonStartMotorMovement.setDisabled(True)
            self.pushButtonStartAllMotorMovements.setDisabled(True)
        else:
            self.pushButtonStartMotorMovement.setDisabled(False)
            self.pushButtonStartAllMotorMovements.setDisabled(False)

        self.pushButtonStartMotorMovement.repaint()
        self.pushButtonStartAllMotorMovements.repaint()

    def solveSimulation(self):
        self.cubeSolver.solve()
        self.moves = [n.name for n in self.cubeSolver.getCubeSimulatorMoves()]
        # k = self.moves[0]
        # self.moves = []
        # self.moves = [k + " " + str(i+2) for i in range(0, 15)]

        self.pushButtonSimulationForward.setDisabled(False)
        # self.pushButtonSimulationBackward.setDisabled(False)
        self.simulationStepShown = 0
        self.simulationMotorMovementShown = 0
        '''
        self.textEditMovesList.setHtml("")
        string = "<span style=\"color:#55aa00;\">" + "Start" + "</span>" + "<br/>"
        for elem in res:
            string += elem + "<br/>"
        self.textEditMovesList.insertHtml(string)  # + str(elem).lower() ) # + "<br/>
        '''
        htmlString = CubeQtApp.createHtmlForTextEditMovesList(self.moves, self.simulationStepShown)
        self.textEditMovesList.setHtml(htmlString)
        self.updateMotorMovementGui()
        # self.textEditMovesList.verticalScrollBar().setValue(self.textEditMovesList.verticalScrollBar().minimum())
        # print(self.textEditMovesList.toPlainText())
        # print(res)

    def setSolver(self):
        stringArray = [self.lineEditInsertTop.text(), self.lineEditInsertLeft.text(), self.lineEditInsertFront.text(),
                       self.lineEditInsertRight.text(), self.lineEditInsertBack.text(),
                       self.lineEditInsertBottom.text()]
        res = self.cubeSolver.setSolverFromString(stringArray)
        if res != 0:
            print("Error in input string")
        else:
            print("Input inserted correctly")
        self.cubeSolver.cubeSimulator[0].printCube()
        self.widget_cubePreview.updateGui()
        self.widget_cubeMotorResolutor.updateGui()
        self.pushButtonSimulationSolve.setDisabled(False)
        self.pushButtonStartMotorMovement.setDisabled(False)

    def loadSolver(self):
        self.cubeSolver.loadCube(self.lineEditLoadConfiguration.text())
        self.widget_cubePreview.updateGui()
        self.widget_cubeMotorResolutor.updateGui()
        self.pushButtonSimulationSolve.setDisabled(False)
        self.pushButtonStartMotorMovement.setDisabled(False)
        self.pushButtonStartAllMotorMovements.setDisabled(False)

    def saveSolver(self):
        self.cubeSolver.saveCube(self.lineEditSaveConfiguration.text())
