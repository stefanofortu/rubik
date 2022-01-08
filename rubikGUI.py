from PySide2 import QtWidgets
from Classes.CubeSolver import CubeSolver
from Classes.CubeApp import CubeQtApp

if __name__ == '__main__':
    app = QtWidgets.QApplication()
    s = CubeSolver()
    qt_app = CubeQtApp(s)
    qt_app.show()
    app.exec_()
