# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(580, 467)
        MainWindow.setMinimumSize(QSize(580, 467))
        MainWindow.setMaximumSize(QSize(580, 467))
        self.actionDeveloper = QAction(MainWindow)
        self.actionDeveloper.setObjectName(u"actionDeveloper")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionOpenFolder = QAction(MainWindow)
        self.actionOpenFolder.setObjectName(u"actionOpenFolder")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")

        self.verticalLayout_4.addWidget(self.label)

        self.leLink = QLineEdit(self.frame_5)
        self.leLink.setObjectName(u"leLink")
        self.leLink.setMinimumSize(QSize(0, 35))
        self.leLink.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_4.addWidget(self.leLink)

        self.btnDownload = QPushButton(self.frame_5)
        self.btnDownload.setObjectName(u"btnDownload")
        self.btnDownload.setMinimumSize(QSize(0, 35))
        self.btnDownload.setMaximumSize(QSize(16777215, 35))
        self.btnDownload.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnDownload.setStyleSheet(u"background-color: rgb(164, 0, 0);\n"
"color: #FFFFFF")

        self.verticalLayout_4.addWidget(self.btnDownload)

        self.cbPlayList = QCheckBox(self.frame_5)
        self.cbPlayList.setObjectName(u"cbPlayList")
        self.cbPlayList.setChecked(True)

        self.verticalLayout_4.addWidget(self.cbPlayList)


        self.horizontalLayout_2.addWidget(self.frame_5)

        self.lbLogo = QLabel(self.frame_4)
        self.lbLogo.setObjectName(u"lbLogo")
        self.lbLogo.setMinimumSize(QSize(120, 90))
        self.lbLogo.setMaximumSize(QSize(120, 90))
        self.lbLogo.setPixmap(QPixmap(u"assets/icon.png"))
        self.lbLogo.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.lbLogo)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.teResult = QTextEdit(self.frame)
        self.teResult.setObjectName(u"teResult")
        self.teResult.setStyleSheet(u"border-radius: 100px;")
        self.teResult.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.teResult)

        self.lbStatus = QLabel(self.frame)
        self.lbStatus.setObjectName(u"lbStatus")

        self.verticalLayout_3.addWidget(self.lbStatus)

        self.pbStatus = QProgressBar(self.frame)
        self.pbStatus.setObjectName(u"pbStatus")
        self.pbStatus.setMaximum(0)
        self.pbStatus.setValue(-1)

        self.verticalLayout_3.addWidget(self.pbStatus)


        self.verticalLayout_2.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 580, 25))
        self.menuOp_es = QMenu(self.menuBar)
        self.menuOp_es.setObjectName(u"menuOp_es")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuOp_es.menuAction())
        self.menuOp_es.addAction(self.actionOpenFolder)
        self.menuOp_es.addAction(self.actionDeveloper)
        self.menuOp_es.addAction(self.actionExit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Youtube to MP3", None))
        self.actionDeveloper.setText(QCoreApplication.translate("MainWindow", u"Site do Desenvolvedor", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Sair", None))
        self.actionOpenFolder.setText(QCoreApplication.translate("MainWindow", u"Abrir pasta de Download", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Link do v\u00eddeo ou PlayList", None))
        self.btnDownload.setText(QCoreApplication.translate("MainWindow", u"Baixar agora", None))
        self.cbPlayList.setText(QCoreApplication.translate("MainWindow", u"\u00c9 uma PlayList", None))
        self.lbLogo.setText("")
        self.lbStatus.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.menuOp_es.setTitle(QCoreApplication.translate("MainWindow", u"Op\u00e7\u00f5es", None))
    # retranslateUi

