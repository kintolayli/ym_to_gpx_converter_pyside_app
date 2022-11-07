# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
                               QMainWindow, QPushButton, QSizePolicy,
                               QVBoxLayout,
                               QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(787, 111)
        MainWindow.setStyleSheet(u"QWidget {\n"
                                 "	color: black;\n"
                                 "	background-color: white;\n"
                                 "	font-family: Textbook;\n"
                                 "	font-size: 12pt;\n"
                                 "}\n"
                                 "QLineEdit {\n"
                                 "	placeholder-text-color: #feeba3;\n"
                                 "}\n"
                                 "QPushButton {\n"
                                 "	background-color: transparent;\n"
                                 "	border: none;\n"
                                 "}\n"
                                 "QPushButton:hover {\n"
                                 "	background-color: #feeba3;\n"
                                 "}\n"
                                 "QPushButton:pressed {\n"
                                 "	background-color: #888;\n"
                                 "}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.textLabel = QLabel(self.centralwidget)
        self.textLabel.setObjectName(u"textLabel")

        self.gridLayout.addWidget(self.textLabel, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setPlaceholderText("paste url here...")

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout.addWidget(self.pushButton_2)

        self.textLabel_2 = QLabel(self.centralwidget)
        self.textLabel.setObjectName(u"textLabel_2")
        self.textLabel_2.setText("Status bar")

        self.verticalLayout.addWidget(self.textLabel_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", u"YMtoGPX", None))
        self.textLabel.setText(
            QCoreApplication.translate("MainWindow", u"URL", None))
        self.pushButton.setText(
            QCoreApplication.translate("MainWindow", u"Download GPX", None))
        # if QT_CONFIG(shortcut)
        self.pushButton.setShortcut(
            QCoreApplication.translate("MainWindow", u"Return", None))
        # endif // QT_CONFIG(shortcut)
        self.pushButton_2.setText(
            QCoreApplication.translate("MainWindow", u"Open files directory", None))
    # retranslateUi
