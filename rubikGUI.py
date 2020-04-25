import sys

from PySide2 import QtWidgets
from PySide2.QtGui import  QPainter, QBrush , QPen , QColor
from PySide2.QtCore import QRect , Qt
import mainW
from solver import CubeSolver

class MyQtApp(mainW.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self, solver):
        super().__init__(solver)
        self.setupUi(self)
        self.cubeSolver = solver
        self.simulationStepShown = 0
        self.CreateNewButton.clicked.connect(self.setSolver)
        self.LoadConfigurationButton.clicked.connect(self.loadSolver)
        self.SaveConfigurationButton.clicked.connect(self.saveSolver)
        self.pushButtonSimulationSolve.clicked.connect(self.solveSimulation)
        self.pushButtonSimulationBackward.clicked.connect(self.stepBackward)
        self.pushButtonSimulationForward.clicked.connect(self.stepForward)

    def getCurrentCubeSimuationString(self):
        return self.cubeSolver.getCubeAtSimulatorStep(self.simulationStepShown).stringify()

    def stepForward(self):
        if self.simulationStepShown >= 0 and self.simulationStepShown < self.cubeSolver.getSimulatorStep() :
            self.simulationStepShown += 1
            self.pushButtonSimulationBackward.setDisabled(False)

        if self.simulationStepShown == self.cubeSolver.getSimulatorStep()-1:
            self.pushButtonSimulationForward.setDisabled(True)
        self.widget_cubePreview.updateGui()
        moves = self.textEditMovesList.toPlainText().split("\n")
        string = ""
        for num, elem in enumerate(moves):
            if num == self.simulationStepShown:
                string += "<span style=\"color:#55aa00;\">" + elem + "</span>" + "<br/>"
            else:
                string += elem + "<br/>"
        self.textEditMovesList.setHtml(string)

    def stepBackward(self):
        if self.simulationStepShown > 0:
            self.simulationStepShown -= 1
            self.pushButtonSimulationForward.setDisabled(False)

        if self.simulationStepShown == 0:
            self.pushButtonSimulationBackward.setDisabled(True)
        self.widget_cubePreview.updateGui()
        self.textEditMovesList.repaint()
        moves = self.textEditMovesList.toPlainText().split("\n")
        string=""
        #string = "<span style=\"color:#55aa00;\">" + "Start" + "</span>" + "<br/>"
        for num, elem in enumerate(moves):
            if num == self.simulationStepShown:
                string += "<span style=\"color:#55aa00;\">" + elem + "</span>" + "<br/>"
            else:
                string += elem + "<br/>"
        self.textEditMovesList.setHtml(string)

    def solveSimulation(self):
        res = self.cubeSolver.solve()
        self.pushButtonSimulationForward.setDisabled(False)
        #self.pushButtonSimulationBackward.setDisabled(False)
        self.textEditMovesList.setHtml("")
        self.simulationStepShown = 0
        string = "<span style=\"color:#55aa00;\">" + "Start" + "</span>" + "<br/>"
        for elem in res:
            string += elem + "<br/>"
        self.textEditMovesList.insertHtml(string) # + str(elem).lower() ) # + "<br/>
        #print(self.textEditMovesList.toPlainText())
        #print(res)

    def setSolver(self):
        stringArray = [self.lineEditInsertTop.text(), self.lineEditInsertLeft.text(), self.lineEditInsertFront.text(),
                       self.lineEditInsertRight.text(), self.lineEditInsertBack.text(), self.lineEditInsertBottom.text()]
        res = s.setSolverFromString(stringArray)
        if res != 0:
            print("Error in input string")
        else:
            print("Input inserted correctly")
        s.cube.printCube()

    def loadSolver(self):
        s.loadCube(self.lineEditLoadConfiguration.text())
        self.widget_cubePreview.updateGui()
        print("load Solver")

    def saveSolver(self):
        s.saveCube(self.lineEditSaveConfiguration.text())
        print("save Solver")

    def paintEvent(self, e):
        pass
        #print(self.widget_2.pos().x())
        #print(self.widget_2.pos().y())
    #    painter = QPainter(self)
    #    painter.begin(self)
    # qp = QPen()
    # qp.setColor(QColor().cyan())
    # painter.setPen(QPen());
    # qb = QBrush()
    # qb.setColor(QColor().cyan())
    # painter.setBrush(qb) #QBrush(Qt.BrushStyle.SolidPattern))
    #painter.drawRect(QRect(self.widget_2.x(), self.widget_2.y(), self.widget_2.width() - 1, self.widget_2.height() - 1));

    #painter.begin(self.widget_2)
    #painter.save()
    #painter.translate(10, 10)

    #painter.drawRect(QRect(self.widget_2.x(), self.widget_2.y(), 10, 10))
    #painter.drawRect(QRect(self.widget_2.x(), self.widget_2.y(), 10, 10))
    #painter.restore()
    #painter.end()



if __name__ == '__main__':
    app = QtWidgets.QApplication()
    s = CubeSolver()
    qt_app = MyQtApp(s)
    qt_app.show()
    app.exec_()
