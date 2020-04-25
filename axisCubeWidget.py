from PySide2.QtWidgets import QWidget
from PySide2.QtGui import QPainter, QBrush, QColor

CubeColorMap = {'b': QColor(0, 0, 255),
                'w': QColor(255, 255, 255),
                'r': QColor(255, 0, 0),
                'y': QColor(255, 255, 0),
                'o': QColor(255, 69, 0),
                'g': QColor(0, 255, 0),
                '-': QColor(180, 180, 180)}


class AxisCubeWidget(QWidget):
    def __init__(self, parent, qtApp):
        super().__init__(parent)
        self.qtApp = qtApp

    def updateGui(self):
        self.repaint()

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.begin(self)
        height_rect = 25
        width_rect = 25
        offset = 1
        # stringCube = self.qtApp.getCurrentCubeSimulationString()
        cnt = 0
        for y in range(offset, height_rect * 3 + offset, height_rect):
            for x in range(offset, width_rect * 3 + offset, width_rect):
                painter.save()
                painter.setBrush(QBrush(QColor(126, 126, 126)))
                cnt += 1
                painter.drawRect(x, y, width_rect, height_rect)
                painter.restore()
        painter.end()
