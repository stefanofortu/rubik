from PySide2.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, Qt)
from PySide2.QtWidgets import QGridLayout, QLineEdit, QPushButton, QFrame, QLabel, QSizePolicy, QTextEdit, QSpacerItem, \
    QMenuBar
from PySide2.QtGui import QPalette, QColor, QBrush
from PySide2.QtWidgets import QWidget
from cubeWidget import MyWidget
from axisCubeWidget import AxisCubeWidget


# from PySide2 import QtWidgets

class Ui_CubeApp(object):
    def __init__(self):
        super().__init__()

    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(350, 700)
        palette = QPalette()
        palette.setBrush(QPalette.Active, QPalette.Window, QBrush(QColor(200, 200, 200, 255)))
        MainWindow.setPalette(palette)
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
        # sizePolicy1.setHorizontalStretch(0)
        # sizePolicy1.setVerticalStretch(0)
        # sizePolicy1.setHeightForWidth(self.lineEditSaveConfiguration.sizePolicy().hasHeightForWidth())
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
        self.widget_cubePreview = MyWidget(self.centralwidget, self)
        self.widget_cubePreview.setObjectName(u"widget_cubePreview")
        self.widget_cubePreview.setMinimumSize(QSize(0, 50))
        self.gridLayout.addWidget(self.widget_cubePreview, 11, 0, 3, 4)

        # push button - Solve the Cube
        self.pushButtonSimulationSolve = QPushButton(self.centralwidget)
        self.pushButtonSimulationSolve.setObjectName(u"pushButtonSimulationSolve")
        self.pushButtonSimulationSolve.setDisabled(True)
        self.gridLayout.addWidget(self.pushButtonSimulationSolve, 11, 4, 1, 2)

        # Widget - TBD
        self.widget_cubeMotorResolutor = MyWidget(self.centralwidget, self)
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
        self.textEditMovesList.setStyleSheet("background-color: rgb(200, 200, 200);\n")
        self.textEditMovesList.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.gridLayout.addWidget(self.textEditMovesList, 12, 4, 1, 2)

        # push button - move simulation forward
        self.pushButtonSimulationBackward = QPushButton(self.centralwidget)
        self.pushButtonSimulationBackward.setObjectName(u"pushButtonSimulationBackward")
        self.pushButtonSimulationBackward.setDisabled(True)
        self.gridLayout.addWidget(self.pushButtonSimulationBackward, 13, 4, 1, 1)

        # push button - move simulation forward
        self.pushButtonSimulationForward = QPushButton(self.centralwidget)
        self.pushButtonSimulationForward.setObjectName(u"pushButtonSimulationForward")
        self.pushButtonSimulationForward.setDisabled(True)
        self.gridLayout.addWidget(self.pushButtonSimulationForward, 13, 5, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 4, 1, 2)

        # Widget axes
        self.widgetAxisCube = AxisCubeWidget(self.centralwidget, self)
        self.widgetAxisCube.setObjectName(u"widgetAxisCube")
        self.widgetAxisCube.setAutoFillBackground(False)
        self.widgetAxisCube.setStyleSheet(u"background-color: rgb(200, 200, 200);")
        self.gridLayout.addWidget(self.widgetAxisCube, 16, 4, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout.addItem(self.verticalSpacer_2, 16, 5, 1, 1)

        self.pushButtonStartMotorMovement = QPushButton(self.centralwidget)
        self.pushButtonStartMotorMovement.setObjectName(u"pushButtonStartMotorMovement")
        self.gridLayout.addWidget(self.pushButtonStartMotorMovement, 17, 5, 1, 1)

        # label Current Step
        self.labelCurrentStep = QLabel(self.centralwidget)
        self.labelCurrentStep.setObjectName(u"labelCurrentStep")
        self.labelCurrentStep.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.gridLayout.addWidget(self.labelCurrentStep, 18, 4, 1, 1)

        self.labelcurrentStepName = QLabel(self.centralwidget)
        self.labelcurrentStepName.setObjectName(u"labelcurrentStepName")
        self.gridLayout.addWidget(self.labelcurrentStepName, 18, 5, 1, 1)

        # Label Current Movement
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

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
        # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("MainWindow")
        self.lineEditInsertTop.setText("ggggggggg")
        self.lineEditInsertLeft.setText("yyyyyyyyy")
        self.lineEditInsertFront.setText("rrrrrrrrr")
        self.lineEditInsertRight.setText("wwwwwwwww")
        self.lineEditInsertBack.setText("ooooooooo")
        self.lineEditInsertBottom.setText("bbbbbbbbb")
        self.CreateNewButton.setText("Insert New Cube")
        self.labelLoadConfiguration.setText("Load from file : ")
        self.lineEditLoadConfiguration.setText("solver")
        self.LoadConfigurationButton.setText("Load")
        self.label_SaveConfiguration.setText("Save from file : ")
        self.lineEditSaveConfiguration.setText("solver")
        self.SaveConfigurationButton.setText("Save")
        self.pushButtonSimulationSolve.setText("Solve Cube")
        self.pushButtonSimulationBackward.setText("<")
        self.pushButtonSimulationForward.setText(">")
        self.pushButtonStartMotorMovement.setText("StartSimulation")
        self.labelCurrentStep.setText("Current Step")
        self.labelcurrentStepName.setText("step xx")
        self.labelCurrentMovement.setText("Current movement")
        self.labelCurrentMovementName.setText("step yy")