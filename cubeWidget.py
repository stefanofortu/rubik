from PySide2.QtWidgets import QWidget
from PySide2.QtGui import QPainter, QBrush, QColor

CubeColorMap = {'b': QColor(0, 0, 255),
                'w': QColor(255, 255, 255),
                'r': QColor(255, 0, 0),
                'y': QColor(255, 255, 0),
                'o': QColor(255, 69, 0),
                'g': QColor(0, 255, 0),
                '-': QColor(180, 180, 180)}


class MyWidget(QWidget):
    def __init__(self, parent, qtApp, typeOfWidget):
        super().__init__(parent)
        self.qtApp = qtApp
        self.typeOfWidget = typeOfWidget

    def updateGui(self):
        self.repaint()

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.begin(self)
        height_rect = 25
        width_rect = 25
        offsetX = 15
        offsetY = 1
        if self.typeOfWidget == "cubePreview":
            stringCube = self.qtApp.getCurrentCubeSimulationString()
        elif self.typeOfWidget == "motorMovement":
            stringCube = self.qtApp.getCurrentCubeMotorMovementString()
        else:
            print("MyWidget() : paintEvent() : Error")
        # stringCube = '-'*9*6
        cnt = 0
        for y in range(offsetY, height_rect * 3 + offsetY, height_rect):
            for x in range(offsetX + width_rect * 3, width_rect * 6 + offsetX, width_rect):
                painter.save()
                painter.setBrush(QBrush(CubeColorMap[stringCube[cnt]]))
                cnt += 1
                painter.drawRect(x, y, width_rect, height_rect)
                painter.restore()

        for y in range(offsetY + height_rect * 3, height_rect * 6 + offsetY, height_rect):
            for x in range(offsetX, width_rect * 3 + offsetX, width_rect):
                painter.save()
                painter.setBrush(QBrush(CubeColorMap[stringCube[cnt]]))
                cnt += 1
                painter.drawRect(x, y, width_rect, height_rect)
                painter.restore()

        for y in range(offsetY + height_rect * 3, height_rect * 6 + offsetY, height_rect):
            for x in range(offsetX + width_rect * 3, width_rect * 6 + offsetX, width_rect):
                painter.save()
                painter.setBrush(QBrush(CubeColorMap[stringCube[cnt]]))
                cnt += 1
                painter.drawRect(x, y, width_rect, height_rect)
                painter.restore()

        for y in range(offsetY + height_rect * 3, height_rect * 6 + offsetY, height_rect):
            for x in range(offsetX + width_rect * 6, width_rect * 9 + offsetX, width_rect):
                painter.save()
                painter.setBrush(QBrush(CubeColorMap[stringCube[cnt]]))
                cnt += 1
                painter.drawRect(x, y, width_rect, height_rect)
                painter.restore()

        for y in range(offsetY + height_rect * 3, height_rect * 6 + offsetY, height_rect):
            for x in range(offsetX + width_rect * 9, width_rect * 12 + offsetX, width_rect):
                painter.save()
                painter.setBrush(QBrush(CubeColorMap[stringCube[cnt]]))
                cnt += 1
                painter.drawRect(x, y, width_rect, height_rect)
                painter.restore()

        for y in range(offsetY + height_rect * 6, height_rect * 9 + offsetY, height_rect):
            for x in range(offsetX + width_rect * 3, width_rect * 6 + offsetX, width_rect):
                painter.save()
                painter.setBrush(QBrush(CubeColorMap[stringCube[cnt]]))
                cnt += 1
                painter.drawRect(x, y, width_rect, height_rect)
                painter.restore()

        painter.end()
