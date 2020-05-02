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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(820, 732)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_7 = QLineEdit(self.centralwidget)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_7.sizePolicy().hasHeightForWidth())
        self.lineEdit_7.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.lineEdit_7, 6, 1, 1, 1)

        self.separator2 = QFrame(self.centralwidget)
        self.separator2.setObjectName(u"separator2")
        self.separator2.setLineWidth(1)
        self.separator2.setFrameShape(QFrame.HLine)
        self.separator2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.separator2, 10, 0, 1, 6)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.widget_2, 11, 0, 3, 4)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(75, 0))

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.SaveCheckBox = QCheckBox(self.centralwidget)
        self.SaveCheckBox.setObjectName(u"SaveCheckBox")
        self.SaveCheckBox.setCheckable(False)

        self.gridLayout.addWidget(self.SaveCheckBox, 7, 3, 1, 1)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(50, 50))
        self.widget.setStyleSheet(u"background-color: rgb(205, 255, 255);")

        self.gridLayout.addWidget(self.widget, 16, 0, 5, 4)

        self.LoadConfigurationButton = QPushButton(self.centralwidget)
        self.LoadConfigurationButton.setObjectName(u"LoadConfigurationButton")
        self.LoadConfigurationButton.setMinimumSize(QSize(0, 0))

        self.gridLayout.addWidget(self.LoadConfigurationButton, 6, 2, 1, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_4, 19, 4, 1, 1)

        self.lineEdit_8 = QLineEdit(self.centralwidget)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit_8.sizePolicy().hasHeightForWidth())
        self.lineEdit_8.setSizePolicy(sizePolicy1)
        self.lineEdit_8.setAutoFillBackground(False)

        self.gridLayout.addWidget(self.lineEdit_8, 7, 1, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 7, 0, 1, 1)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 11, 4, 1, 2)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 18, 5, 1, 1)

        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout.addWidget(self.lineEdit_4, 1, 3, 1, 1)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 17, 5, 1, 1)

        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(50, 0))

        self.gridLayout.addWidget(self.pushButton_4, 13, 4, 1, 1)

        self.lineEdit_5 = QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMinimumSize(QSize(75, 0))

        self.gridLayout.addWidget(self.lineEdit_5, 2, 1, 1, 1)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 19, 5, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 4, 1, 2)

        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(75, 0))

        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 18, 4, 1, 1)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 15, 0, 1, 6)

        self.lineEdit_6 = QLineEdit(self.centralwidget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout.addWidget(self.lineEdit_6, 1, 0, 1, 1)

        self.LoadCheckBox = QCheckBox(self.centralwidget)
        self.LoadCheckBox.setObjectName(u"LoadCheckBox")
        self.LoadCheckBox.setCheckable(False)
        self.LoadCheckBox.setTristate(False)

        self.gridLayout.addWidget(self.LoadCheckBox, 6, 3, 1, 1)

        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy2)
        self.pushButton_5.setMinimumSize(QSize(50, 0))

        self.gridLayout.addWidget(self.pushButton_5, 13, 5, 1, 1)

        self.separator1 = QFrame(self.centralwidget)
        self.separator1.setObjectName(u"separator1")
        self.separator1.setEnabled(True)
        self.separator1.setLineWidth(2)
        self.separator1.setFrameShape(QFrame.HLine)
        self.separator1.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.separator1, 3, 0, 1, 6)

        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout.addWidget(self.lineEdit_3, 1, 2, 1, 1)

        self.SaveConfigurationButton = QPushButton(self.centralwidget)
        self.SaveConfigurationButton.setObjectName(u"SaveConfigurationButton")

        self.gridLayout.addWidget(self.SaveConfigurationButton, 7, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 16, 5, 1, 1)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setAutoFillBackground(False)
        self.widget_3.setStyleSheet(u"background-color: rgb(200, 200, 200);")

        self.gridLayout.addWidget(self.widget_3, 16, 4, 1, 1)

        self.CreateNew_Button = QPushButton(self.centralwidget)
        self.CreateNew_Button.setObjectName(u"CreateNew_Button")

        self.gridLayout.addWidget(self.CreateNew_Button, 2, 3, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 6, 0, 1, 1)

        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy3)
        self.textEdit.setStyleSheet(u"font: 8pt \"MS Shell Dlg 2\";\n"
"selection-background-color: rgb(255, 255, 0);\n"
"background-color: rgb(85, 255, 255);\n"
"alternate-background-color: rgb(255, 0, 127);")
        self.textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.textEdit.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.textEdit.setAutoFormatting(QTextEdit.AutoNone)

        self.gridLayout.addWidget(self.textEdit, 12, 4, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 820, 21))
        MainWindow.setMenuBar(self.menubar)
        QWidget.setTabOrder(self.lineEdit, self.lineEdit_6)
        QWidget.setTabOrder(self.lineEdit_6, self.lineEdit_2)
        QWidget.setTabOrder(self.lineEdit_2, self.lineEdit_3)
        QWidget.setTabOrder(self.lineEdit_3, self.lineEdit_4)
        QWidget.setTabOrder(self.lineEdit_4, self.lineEdit_5)
        QWidget.setTabOrder(self.lineEdit_5, self.CreateNew_Button)
        QWidget.setTabOrder(self.CreateNew_Button, self.lineEdit_7)
        QWidget.setTabOrder(self.lineEdit_7, self.LoadConfigurationButton)
        QWidget.setTabOrder(self.LoadConfigurationButton, self.LoadCheckBox)
        QWidget.setTabOrder(self.LoadCheckBox, self.lineEdit_8)
        QWidget.setTabOrder(self.lineEdit_8, self.SaveConfigurationButton)
        QWidget.setTabOrder(self.SaveConfigurationButton, self.SaveCheckBox)
        QWidget.setTabOrder(self.SaveCheckBox, self.pushButton)
        QWidget.setTabOrder(self.pushButton, self.textEdit)
        QWidget.setTabOrder(self.textEdit, self.pushButton_4)
        QWidget.setTabOrder(self.pushButton_4, self.pushButton_5)
        QWidget.setTabOrder(self.pushButton_5, self.pushButton_2)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lineEdit.setText("")
        self.SaveCheckBox.setText("")
        self.LoadConfigurationButton.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Current movement", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Save from file : ", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.lineEdit_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Current Step", None))
        self.LoadCheckBox.setText("")
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.SaveConfigurationButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.CreateNew_Button.setText(QCoreApplication.translate("MainWindow", u"Insert New Cube", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Load from file : ", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">LR;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">RH;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">GH;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">FS;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">WS;</p>\n"
"<p style=\" margin-"
                        "top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">AS;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#55aa00;\">FA;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#55aa00;\">AS;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">GT;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">AS;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">TR;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">WQ;</p></body></html>", None))
    # retranslateUi

