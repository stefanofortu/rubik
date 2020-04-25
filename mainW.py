# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainW.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                            QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
                           QRadialGradient)
from PySide2.QtWidgets import *

from PySide2.QtWidgets import QWidget

# from PySide2 import QtWidgets
from solver import CubeSolver

CubeColorMap    = { 'b': QColor(0,0,255) ,
					'w': QColor(255,255,255),
					'r': QColor(255,0,0),
					'y': QColor(255,255,0),
					'o': QColor(255,69,0),
					'g': QColor(0,255,0),
                    '-': QColor(180,180,180) }


class myWidget(QWidget):
    def __init__(self, parent, qtApp):
        super().__init__(parent)
        self.qtApp = qtApp

    def updateGui(self):
        self.repaint()

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.begin(self)
        # qp = QPen()
        # qp.setColor(QColor().cyan())
        # painter.setPen(QPen());
        # qb = QBrush()
        # qb.setColor(QColor().cyan())
        # painter.setBrush(qb) #QBrush(Qt.BrushStyle.SolidPattern))
        # painter.drawRect(QRect(0, 0, self.width() - 1, self.height() - 1))
        height_rect = 25
        width_rect = 25
        offset = 1
        stringCube = self.qtApp.getCurrentCubeSimuationString()
        # stringCube = '-'*9*6
        cnt = 0
        for y in range(offset, height_rect * 3 + offset, height_rect):
            for x in range(offset + width_rect * 3, width_rect * 6 + offset, width_rect):
                painter.save()
                painter.setBrush(QBrush(CubeColorMap[stringCube[cnt]]))
                cnt += 1
                painter.drawRect(x, y, width_rect, height_rect)
                painter.restore()

        for y in range(offset + height_rect * 3, height_rect * 6 + offset, height_rect):
            for x in range(offset, width_rect * 3 + offset, width_rect):
                painter.save()
                painter.setBrush(QBrush(CubeColorMap[stringCube[cnt]]))
                cnt += 1
                painter.drawRect(x, y, width_rect, height_rect)
                painter.restore()

        for y in range(offset + height_rect * 3, height_rect * 6 + offset, height_rect):
            for x in range(offset + width_rect*3, width_rect * 6 + offset, width_rect):
                painter.save()
                painter.setBrush(QBrush(CubeColorMap[stringCube[cnt]]))
                cnt += 1
                painter.drawRect(x, y, width_rect, height_rect)
                painter.restore()

        for y in range(offset + height_rect * 3, height_rect * 6 + offset, height_rect):
            for x in range(offset + width_rect*6 , width_rect * 9 + offset, width_rect):
                painter.save()
                painter.setBrush(QBrush(CubeColorMap[stringCube[cnt]]))
                cnt += 1
                painter.drawRect(x, y, width_rect, height_rect)
                painter.restore()

        for y in range(offset + height_rect * 3, height_rect * 6 + offset, height_rect):
            for x in range(offset + width_rect*9, width_rect * 12 + offset, width_rect):
                painter.save()
                painter.setBrush(QBrush(CubeColorMap[stringCube[cnt]]))
                cnt += 1
                painter.drawRect(x, y, width_rect, height_rect)
                painter.restore()

        for y in range(offset + height_rect * 6, height_rect * 9 + offset, height_rect):
            for x in range(offset + width_rect * 3, width_rect * 6 + offset, width_rect):
                painter.save()
                painter.setBrush(QBrush(CubeColorMap[stringCube[cnt]]))
                cnt += 1
                painter.drawRect(x, y, width_rect, height_rect)
                painter.restore()
        # painter.begin(self.widget_2)
        # painter.save()
        # painter.translate(10, 10)

        painter.drawRect(30, 30, 10, 10)
        # painter.drawRect(QRect(self.x(), self.y(), 10, 10))
        # painter.restore()
        painter.end()


class Ui_MainWindow(object):
    def __init__(self, cubeSolver):
        super().__init__()
        self.cubeSolver = cubeSolver

    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(837, 671)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")

        # Manual Insert
        # Line Edit - insert top Face
        self.lineEditInsertTop = QLineEdit(self.centralwidget)
        self.lineEditInsertTop.setObjectName(u"lineEditInsertTop")
        self.lineEditInsertTop.setMinimumSize(QSize(75, 0))
        self.gridLayout.addWidget(self.lineEditInsertTop, 0, 1, 1, 1)
        # Line Edit - insert Left Face
        self.lineEditInsertLeft = QLineEdit(self.centralwidget)
        self.lineEditInsertLeft.setObjectName(u"lineEditInsertLeft")
        self.gridLayout.addWidget(self.lineEditInsertLeft, 1, 0, 1, 1)
        # Line Edit - insert Front Face
        self.lineEditInsertFront = QLineEdit(self.centralwidget)
        self.lineEditInsertFront.setObjectName(u"lineEditInsertFront")
        self.lineEditInsertFront.setMinimumSize(QSize(75, 0))
        self.gridLayout.addWidget(self.lineEditInsertFront, 1, 1, 1, 1)
        # Line Edit - insert Right Face
        self.lineEditInsertRight = QLineEdit(self.centralwidget)
        self.lineEditInsertRight.setObjectName(u"lineEditInsertRight")
        self.gridLayout.addWidget(self.lineEditInsertRight, 1, 2, 1, 1)
        # Line Edit - insert Back Face
        self.lineEditInsertBack = QLineEdit(self.centralwidget)
        self.lineEditInsertBack.setObjectName(u"lineEditInsertBack")
        self.gridLayout.addWidget(self.lineEditInsertBack, 1, 3, 1, 1)
        # Line Edit - insert Bottom Face
        self.lineEditInsertBottom = QLineEdit(self.centralwidget)
        self.lineEditInsertBottom.setObjectName(u"lineEditInsertBottom")
        self.lineEditInsertBottom.setMinimumSize(QSize(75, 0))
        self.gridLayout.addWidget(self.lineEditInsertBottom, 2, 1, 1, 1)
        # Button - insert Datta
        self.CreateNewButton = QPushButton(self.centralwidget)
        self.CreateNewButton.setObjectName(u"CreateNewButton")
        self.gridLayout.addWidget(self.CreateNewButton, 2, 3, 1, 1)

        self.separator1 = QFrame(self.centralwidget)
        self.separator1.setObjectName(u"separator1")
        self.separator1.setEnabled(True)
        self.separator1.setLineWidth(2)
        self.separator1.setFrameShape(QFrame.HLine)
        self.separator1.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.separator1, 3, 0, 1, 6)

        # Load from file
        # Label for Save Configuration
        self.labelLoadConfiguration = QLabel(self.centralwidget)
        self.labelLoadConfiguration.setObjectName(u"labelLoadConfiguration")
        self.labelLoadConfiguration.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.gridLayout.addWidget(self.labelLoadConfiguration, 6, 0, 1, 1)
        # Line Edit for Save Configuration
        self.lineEditLoadConfiguration = QLineEdit(self.centralwidget)
        self.lineEditLoadConfiguration.setObjectName(u"lineEditLoadConfiguration")
        self.gridLayout.addWidget(self.lineEditLoadConfiguration, 6, 1, 1, 1)
        # Push Button for Load
        self.LoadConfigurationButton = QPushButton(self.centralwidget)
        self.LoadConfigurationButton.setObjectName(u"LoadConfigurationButton")
        self.LoadConfigurationButton.setMinimumSize(QSize(0, 0))
        self.gridLayout.addWidget(self.LoadConfigurationButton, 6, 2, 1, 1)


        # Save to File
        # Label for Save Configuration
        self.label_SaveConfiguration = QLabel(self.centralwidget)
        self.label_SaveConfiguration.setObjectName(u"label_SaveConfiguration")
        self.label_SaveConfiguration.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.gridLayout.addWidget(self.label_SaveConfiguration, 7, 0, 1, 1)
        # Line Edit for Save Configuration
        self.lineEditSaveConfiguration = QLineEdit(self.centralwidget)
        self.lineEditSaveConfiguration.setObjectName(u"lineEditSaveConfiguration")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        #sizePolicy1.setHorizontalStretch(0)
        #sizePolicy1.setVerticalStretch(0)
        #sizePolicy1.setHeightForWidth(self.lineEditSaveConfiguration.sizePolicy().hasHeightForWidth())
        self.lineEditSaveConfiguration.setSizePolicy(sizePolicy1)
        self.gridLayout.addWidget(self.lineEditSaveConfiguration, 7, 1, 1, 1)
        # Push Button for Save Configuration
        self.SaveConfigurationButton = QPushButton(self.centralwidget)
        self.SaveConfigurationButton.setObjectName(u"SaveConfigurationButton")
        self.gridLayout.addWidget(self.SaveConfigurationButton, 7, 2, 1, 1)

        # Line Separator
        self.separator2 = QFrame(self.centralwidget)
        self.separator2.setObjectName(u"separator2")
        self.separator2.setLineWidth(1)
        self.separator2.setFrameShape(QFrame.HLine)
        self.separator2.setFrameShadow(QFrame.Sunken)
        self.gridLayout.addWidget(self.separator2, 10, 0, 1, 6)

        # Widget - canvas for cube preview
        self.widget_cubePreview = myWidget(self.centralwidget, self)
        self.widget_cubePreview.setObjectName(u"widget_cubePreview")
        self.widget_cubePreview.setMinimumSize(QSize(0, 50))
        self.gridLayout.addWidget(self.widget_cubePreview, 11, 0, 3, 4)

        #push button - Solve the Cube
        self.pushButtonSimulationSolve = QPushButton(self.centralwidget)
        self.pushButtonSimulationSolve.setObjectName(u"pushButtonSimulationSolve")
        self.gridLayout.addWidget(self.pushButtonSimulationSolve, 11, 4, 1, 2)

        # Widget - TBD
        self.widget_cubeMotorResolutor = myWidget(self.centralwidget, self)
        self.widget_cubeMotorResolutor.setObjectName(u"widget_cubeMotorResolutor")
        self.widget_cubeMotorResolutor.setMinimumSize(QSize(50, 50))
        self.widget_cubeMotorResolutor.setStyleSheet(u"background-color: rgb(205, 0, 255);")
        self.gridLayout.addWidget(self.widget_cubeMotorResolutor, 16, 0, 5, 4)

        # TEXT EDIT PER LISTA MOSSE
        self.textEditMovesList = QTextEdit(self.centralwidget)
        self.textEditMovesList.setObjectName(u"textEditMovesList")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.textEditMovesList.sizePolicy().hasHeightForWidth())
        self.textEditMovesList.setSizePolicy(sizePolicy3)
        self.textEditMovesList.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.gridLayout.addWidget(self.textEditMovesList, 12, 4, 1, 2)

        #push button - move simulation forward
        self.pushButtonSimulationBackward = QPushButton(self.centralwidget)
        self.pushButtonSimulationBackward.setObjectName(u"pushButtonSimulationBackward")
        self.pushButtonSimulationBackward.setDisabled(True)
        self.gridLayout.addWidget(self.pushButtonSimulationBackward, 13, 4, 1, 1)

        #push button - move simulation forward
        self.pushButtonSimulationForward = QPushButton(self.centralwidget)
        self.pushButtonSimulationForward.setObjectName(u"pushButtonSimulationForward")
        self.pushButtonSimulationForward.setDisabled(True)
        self.gridLayout.addWidget(self.pushButtonSimulationForward, 13, 5, 1, 1)



        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 4, 1, 2)



        #Widget axes
        self.widget_3 = myWidget(self.centralwidget, self)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setAutoFillBackground(False)
        self.widget_3.setStyleSheet(u"background-color: rgb(200, 200, 200);")
        self.gridLayout.addWidget(self.widget_3, 16, 4, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout.addItem(self.verticalSpacer_2, 16, 5, 1, 1)

        self.pushButtonStartMotorMovement = QPushButton(self.centralwidget)
        self.pushButtonStartMotorMovement.setObjectName(u"pushButtonStartMotorMovement")
        self.gridLayout.addWidget(self.pushButtonStartMotorMovement, 17, 5, 1, 1)

        #label Current Step
        self.labelCurrentStep = QLabel(self.centralwidget)
        self.labelCurrentStep.setObjectName(u"labelCurrentStep")
        self.labelCurrentStep.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.gridLayout.addWidget(self.labelCurrentStep, 18, 4, 1, 1)

        self.labelcurrentStepName = QLabel(self.centralwidget)
        self.labelcurrentStepName.setObjectName(u"labelcurrentStepName")
        self.gridLayout.addWidget(self.labelcurrentStepName, 18, 5, 1, 1)

        #Label Current Movement
        self.labelCurrentMovement = QLabel(self.centralwidget)
        self.labelCurrentMovement.setObjectName(u"labelCurrentMovement")
        self.labelCurrentMovement.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.gridLayout.addWidget(self.labelCurrentMovement, 19, 4, 1, 1)

        self.labelCurrentMovementName = QLabel(self.centralwidget)
        self.labelCurrentMovementName.setObjectName(u"labelCurrentMovementName")
        self.gridLayout.addWidget(self.labelCurrentMovementName, 19, 5, 1, 1)

        #############################

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 837, 21))
        MainWindow.setMenuBar(self.menubar)




        # QWidget.setTabOrder(self.lineEdit, self.lineEdit6)
        # QWidget.setTabOrder(self.lineEdit6, self.lineEdit2)
        # QWidget.setTabOrder(self.lineEdit2, self.lineEdit3)
        # QWidget.setTabOrder(self.lineEdit3, self.lineEdit4)
        # QWidget.setTabOrder(self.lineEdit4, self.lineEdit5)
        # QWidget.setTabOrder(self.lineEdit5, self.CreateNewButton)
        # QWidget.setTabOrder(self.CreateNewButton, self.lineEdit7)
        # QWidget.setTabOrder(self.lineEdit7, self.LoadConfigurationButton)
        # QWidget.setTabOrder(self.LoadConfigurationButton, self.LoadCheckBox)
        # QWidget.setTabOrder(self.LoadCheckBox, self.lineEdit8)
        # QWidget.setTabOrder(self.lineEdit8, self.SaveConfigurationButton)
        # QWidget.setTabOrder(self.SaveConfigurationButton, self.SaveCheckBox)
        # QWidget.setTabOrder(self.SaveCheckBox, self.pushButton)
        # QWidget.setTabOrder(self.pushButton, self.textEdit)
        # QWidget.setTabOrder(self.textEdit, self.pushButton_4)
        # QWidget.setTabOrder(self.pushButton_4, self.pushButton_5)
        # QWidget.setTabOrder(self.pushButton_5, self.pushButton_2)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
        # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lineEditInsertTop.setText("ggggggggg")
        self.lineEditInsertLeft.setText("yyyyyyyyy")
        self.lineEditInsertFront.setText("rrrrrrrrr")
        self.lineEditInsertRight.setText("wwwwwwwww")
        self.lineEditInsertBack.setText("ooooooooo")
        self.lineEditInsertBottom.setText("bbbbbbbbb")
        self.CreateNewButton.setText(QCoreApplication.translate("MainWindow", u"Insert New Cube", None))

        self.labelLoadConfiguration.setText(QCoreApplication.translate("MainWindow", u"Load from file : ", None))
        self.lineEditLoadConfiguration.setText("solver")
        self.LoadConfigurationButton.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.label_SaveConfiguration.setText(QCoreApplication.translate("MainWindow", u"Save from file : ", None))
        self.lineEditSaveConfiguration.setText("solver")
        self.SaveConfigurationButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))

        self.pushButtonSimulationSolve.setText(QCoreApplication.translate("MainWindow", u"Solve Cube", None))

        self.textEditMovesList.setHtml("<br/>LR; <br/>GH; <br/> FS; <br/>")
        self.textEditMovesList.insertHtml("<span style=\"color:#55aa00;\">AS;</span>")

        self.pushButtonSimulationBackward.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.pushButtonSimulationForward.setText(QCoreApplication.translate("MainWindow", u">", None))


        self.pushButtonStartMotorMovement.setText(QCoreApplication.translate("MainWindow", u"StartSimulation", None))
        self.labelCurrentStep.setText(QCoreApplication.translate("MainWindow", u"Current Step", None))
        self.labelcurrentStepName.setText(QCoreApplication.translate("MainWindow", u"step xx", None))
        self.labelCurrentMovement.setText(QCoreApplication.translate("MainWindow", u"Current movement", None))
        self.labelCurrentMovementName.setText(QCoreApplication.translate("MainWindow", u"step yy", None))

    # retranslateUi
