from PySide2 import QtWidgets
from solver import CubeSolver
from cubeApp import CubeQtApp

if __name__ == '__main__':
    app = QtWidgets.QApplication()
    s = CubeSolver()
    qt_app = CubeQtApp(s)
    qt_app.show()
    app.exec_()
