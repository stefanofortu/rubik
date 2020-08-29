from PySide2.QtWidgets import QWidget
from PySide2.QtGui import QPainter, QBrush, QColor, QPen, Qt

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
        xOrigin = int(painter.device().width() / 2)
        yOrigin = int(painter.device().height() / 2)
        print(xOrigin,yOrigin)
        xLenght = painter.device().width() / 2
        yLenght = painter.device().height()
        offset_XYaxis = 3
        offset_Zaxis  = 7
        painter.save()
        #painter.setBrush(QBrush(QColor(240, 240, 240)))
        #painter.drawRect(0, 0, painter.device().width() - 1, painter.device().height() - 1)
        painter.setBrush(QBrush(QColor(210, 210, 210)))

        painter.drawRect(painter.device().width() / 4, 0, painter.device().width()/2, painter.device().height()-1)

        penAxisEnable = QPen()
        penAxisEnable.setStyle(Qt.DotLine)
        penAxisEnable.setWidth(2)
        penAxisEnable.setBrush(Qt.gray)
        penAxisDisable = QPen()
        penAxisDisable.setStyle(Qt.DashLine)
        penAxisDisable.setWidth(2)
        penAxisDisable.setBrush(Qt.blue)

        #self.qtApp.get ######get the value of the x,y,z versors
        xVersor = 1
        yVersor = -1
        zVersor = -1
        if xVersor == 1:
            painter.setPen(penAxisEnable)
        else:
            painter.setPen(penAxisDisable)
        painter.drawLine(xOrigin - xLenght / 2 + offset, yOrigin, xOrigin, yOrigin)
        if xVersor == -1:
            painter.setPen(penAxisEnable)
        else:
            painter.setPen(penAxisDisable)
        painter.drawLine(xOrigin, yOrigin, xOrigin + xLenght/2 - offset, yOrigin)

        if yVersor == 1:
            painter.setPen(penAxisEnable)
        else:
            painter.setPen(penAxisDisable)
        painter.drawLine(xOrigin, yOrigin, xOrigin, yOrigin + yLenght/2 - offset)

        if yVersor == -1:
            painter.setPen(penAxisEnable)
        else:
            painter.setPen(penAxisDisable)
        painter.drawLine(xOrigin, yOrigin - yLenght / 2 + offset, xOrigin, yOrigin)

        if zVersor == 1:
            painter.setPen(penAxisEnable)
        else:
            painter.setPen(penAxisDisable)
        painter.drawLine(xOrigin - xLenght / 2 + offset_Zaxis, yOrigin + yLenght / 2 - offset_Zaxis, xOrigin, yOrigin)
        if zVersor == -1:
            painter.setPen(penAxisEnable)
        else:
            painter.setPen(penAxisDisable)
        painter.drawLine(xOrigin, yOrigin, xOrigin + xLenght / 2 - offset_Zaxis, yOrigin - yLenght / 2 + offset_Zaxis)

        painter.restore()

        painter.end()
