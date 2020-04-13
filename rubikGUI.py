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
        self.CreateNewButton.clicked.connect(self.setSolver)
        self.LoadConfigurationButton.clicked.connect(self.loadSolver)
        self.SaveConfigurationButton.clicked.connect(self.saveSolver)
        self.pushButtonSimulationSolve.clicked.connect(self.solveSimulation)
        # self.widget_2.setMinimumHeight(100)
        # @#self.widget_2.setMinimumWidth(100)

    def solveSimulation(self):
        res = self.cubeSolver.solve()
        print(res)

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
        s.loadCube(self.lineEditLoadFromFile.text())
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
