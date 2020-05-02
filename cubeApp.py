from solver import CubeSolver

from uiCubeApp import Ui_CubeApp

from PySide2 import QtWidgets

class CubeQtApp(Ui_CubeApp, QtWidgets.QMainWindow):
    def __init__(self, solver):
        super().__init__()
        self.setupUi(self)
        self.cubeSolver = solver
        self.simulationStepShown = 0
        self.CreateNewButton.clicked.connect(self.setSolver)
        self.LoadConfigurationButton.clicked.connect(self.loadSolver)
        self.SaveConfigurationButton.clicked.connect(self.saveSolver)
        self.pushButtonSimulationSolve.clicked.connect(self.solveSimulation)
        self.pushButtonSimulationBackward.clicked.connect(self.stepBackward)
        self.pushButtonSimulationForward.clicked.connect(self.stepForward)
        self.moves = [] # da cancellare e sostiture con chiamata a solver

    def getCurrentCubeSimulationString(self):
        return self.cubeSolver.getCubeAtSimulatorStep(self.simulationStepShown).stringify()

    def createHtmlForTextEditMovesList(self, moves, currentMove):
        htmlString = "<style> td </style>"
        #htmlString += "table, th, td { border: 1px solid black; }"
        htmlString += "<table width=\"100%\">"

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

    def stepForward(self):
        if 0 <= self.simulationStepShown < self.cubeSolver.getSimulatorStep():
            self.simulationStepShown += 1
            self.pushButtonSimulationBackward.setDisabled(False)

        if self.simulationStepShown == self.cubeSolver.getSimulatorStep() - 1:
            self.pushButtonSimulationForward.setDisabled(True)
        self.widget_cubePreview.updateGui()
        # moves = self.textEditMovesList.toPlainText().split("\n")
        htmlString = self.createHtmlForTextEditMovesList(self.moves,self.simulationStepShown)
        self.textEditMovesList.setHtml(htmlString)

    def stepBackward(self):
        if self.simulationStepShown > 0:
            self.simulationStepShown -= 1
            self.pushButtonSimulationForward.setDisabled(False)

        if self.simulationStepShown == 0:
            self.pushButtonSimulationBackward.setDisabled(True)
        self.widget_cubePreview.updateGui()
        self.textEditMovesList.repaint()
        #self.moves = self.textEditMovesList.toPlainText().split("\n")
        '''
        string = ""
        for num, elem in enumerate(moves):
            if num == self.simulationStepShown:
                string += "<span style=\"color:#55aa00;\">" + elem + "</span>" + "<br/>"
            else:
                string += elem + "<br/>"
        self.textEditMovesList.setHtml(string)
        '''
        htmlString = self.createHtmlForTextEditMovesList(self.moves,self.simulationStepShown)
        self.textEditMovesList.setHtml(htmlString)


    def solveSimulation(self):
        self.moves = self.cubeSolver.solve()
        self.pushButtonSimulationForward.setDisabled(False)
        # self.pushButtonSimulationBackward.setDisabled(False)
        self.simulationStepShown = 0
        '''
        self.textEditMovesList.setHtml("")
        string = "<span style=\"color:#55aa00;\">" + "Start" + "</span>" + "<br/>"
        for elem in res:
            string += elem + "<br/>"
        self.textEditMovesList.insertHtml(string)  # + str(elem).lower() ) # + "<br/>
        '''
        htmlString = self.createHtmlForTextEditMovesList(self.moves,self.simulationStepShown)
        self.textEditMovesList.setHtml(htmlString)
        self.textEditMovesList.verticalScrollBar().setValue(self.textEditMovesList.verticalScrollBar().maximum())
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
        self.cubeSolver.cube.printCube()
        self.pushButtonSimulationSolve.setDisabled(False)

    def loadSolver(self):
        self.cubeSolver.loadCube(self.lineEditLoadConfiguration.text())
        self.widget_cubePreview.updateGui()
        self.pushButtonSimulationSolve.setDisabled(False)

    def saveSolver(self):
        self.cubeSolver.saveCube(self.lineEditSaveConfiguration.text())
