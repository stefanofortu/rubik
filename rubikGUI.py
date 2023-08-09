from PySide2 import QtWidgets
from Classes.CubeApp import CubeQtApp

if __name__ == '__main__':
    app = QtWidgets.QApplication()
    qt_app = CubeQtApp()
    qt_app.show()
    app.exec_()
