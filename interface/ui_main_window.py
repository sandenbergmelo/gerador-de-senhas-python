# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QHBoxLayout,
    QLabel, QLayout, QListView, QListWidget,
    QListWidgetItem, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(371, 526)
        MainWindow.setStyleSheet(u"background-color: rgb(40, 42, 54);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(248, 248, 242);")

        self.verticalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(248, 248, 242);")

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(248, 248, 242);")

        self.verticalLayout_2.addWidget(self.label_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.spinLetters = QSpinBox(self.centralwidget)
        self.spinLetters.setObjectName(u"spinLetters")
        font1 = QFont()
        font1.setPointSize(12)
        self.spinLetters.setFont(font1)
        self.spinLetters.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.spinLetters.setMaximum(16)
        self.spinLetters.setValue(8)

        self.verticalLayout_3.addWidget(self.spinLetters)

        self.spinNumbers = QSpinBox(self.centralwidget)
        self.spinNumbers.setObjectName(u"spinNumbers")
        self.spinNumbers.setFont(font1)
        self.spinNumbers.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.spinNumbers.setMaximum(16)
        self.spinNumbers.setValue(4)

        self.verticalLayout_3.addWidget(self.spinNumbers)

        self.spinChars = QSpinBox(self.centralwidget)
        self.spinChars.setObjectName(u"spinChars")
        self.spinChars.setFont(font1)
        self.spinChars.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.spinChars.setMaximum(16)
        self.spinChars.setValue(2)

        self.verticalLayout_3.addWidget(self.spinChars)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.checkSavePassword = QCheckBox(self.centralwidget)
        self.checkSavePassword.setObjectName(u"checkSavePassword")
        font2 = QFont()
        font2.setPointSize(11)
        self.checkSavePassword.setFont(font2)
        self.checkSavePassword.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.checkSavePassword.setStyleSheet(u"color: rgb(248, 248, 242);")

        self.verticalLayout.addWidget(self.checkSavePassword)

        self.buttonsLayout = QHBoxLayout()
        self.buttonsLayout.setSpacing(8)
        self.buttonsLayout.setObjectName(u"buttonsLayout")
        self.buttonsLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.buttonsLayout.setContentsMargins(5, 5, 5, 5)
        self.pushGeneratePassword = QPushButton(self.centralwidget)
        self.pushGeneratePassword.setObjectName(u"pushGeneratePassword")
        self.pushGeneratePassword.setMinimumSize(QSize(0, 40))
        font3 = QFont()
        font3.setPointSize(14)
        self.pushGeneratePassword.setFont(font3)
        self.pushGeneratePassword.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushGeneratePassword.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(80, 250, 123);")

        self.buttonsLayout.addWidget(self.pushGeneratePassword)

        self.pushClean = QPushButton(self.centralwidget)
        self.pushClean.setObjectName(u"pushClean")
        self.pushClean.setMinimumSize(QSize(0, 40))
        self.pushClean.setFont(font3)
        self.pushClean.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushClean.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(98, 114, 164);")

        self.buttonsLayout.addWidget(self.pushClean)

        self.pushExit = QPushButton(self.centralwidget)
        self.pushExit.setObjectName(u"pushExit")
        self.pushExit.setMinimumSize(QSize(0, 40))
        self.pushExit.setFont(font3)
        self.pushExit.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushExit.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 85, 85);")

        self.buttonsLayout.addWidget(self.pushExit)

        self.buttonsLayout.setStretch(0, 3)
        self.buttonsLayout.setStretch(1, 2)
        self.buttonsLayout.setStretch(2, 2)

        self.verticalLayout.addLayout(self.buttonsLayout)

        self.listOutput = QListWidget(self.centralwidget)
        self.listOutput.setObjectName(u"listOutput")
        font4 = QFont()
        font4.setFamilies([u"Monospace"])
        font4.setPointSize(14)
        self.listOutput.setFont(font4)
        self.listOutput.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.ArrowCursor))
        self.listOutput.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.listOutput.setStyleSheet(u"color: rgb(248, 248, 242);\n"
"background-color: rgb(68, 71, 90);")
        self.listOutput.setAutoScrollMargin(16)
        self.listOutput.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listOutput.setProperty(u"showDropIndicator", False)
        self.listOutput.setDragEnabled(False)
        self.listOutput.setDragDropOverwriteMode(False)
        self.listOutput.setDragDropMode(QAbstractItemView.DragOnly)
        self.listOutput.setSelectionMode(QAbstractItemView.SingleSelection)
        self.listOutput.setMovement(QListView.Free)
        self.listOutput.setProperty(u"isWrapping", False)
        self.listOutput.setResizeMode(QListView.Fixed)
        self.listOutput.setSelectionRectVisible(True)

        self.verticalLayout.addWidget(self.listOutput)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 371, 22))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Gerador de senhas", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Quantidate de letras:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Quantidade de n\u00fameros:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Quantidade de caracteres especiais:", None))
        self.checkSavePassword.setText(QCoreApplication.translate("MainWindow", u"Salvar senha", None))
        self.pushGeneratePassword.setText(QCoreApplication.translate("MainWindow", u"Gerar Senha", None))
        self.pushClean.setText(QCoreApplication.translate("MainWindow", u"Limpar", None))
        self.pushExit.setText(QCoreApplication.translate("MainWindow", u"Sair", None))
    # retranslateUi
