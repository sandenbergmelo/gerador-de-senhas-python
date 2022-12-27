# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
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
        self.spinLetras = QSpinBox(self.centralwidget)
        self.spinLetras.setObjectName(u"spinLetras")
        font1 = QFont()
        font1.setPointSize(12)
        self.spinLetras.setFont(font1)
        self.spinLetras.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.spinLetras.setMaximum(16)
        self.spinLetras.setValue(8)

        self.verticalLayout_3.addWidget(self.spinLetras)

        self.spinNumeros = QSpinBox(self.centralwidget)
        self.spinNumeros.setObjectName(u"spinNumeros")
        self.spinNumeros.setFont(font1)
        self.spinNumeros.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.spinNumeros.setMaximum(16)
        self.spinNumeros.setValue(4)

        self.verticalLayout_3.addWidget(self.spinNumeros)

        self.spinCaracteres = QSpinBox(self.centralwidget)
        self.spinCaracteres.setObjectName(u"spinCaracteres")
        self.spinCaracteres.setFont(font1)
        self.spinCaracteres.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.spinCaracteres.setMaximum(16)
        self.spinCaracteres.setValue(2)

        self.verticalLayout_3.addWidget(self.spinCaracteres)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.checkSalvarSenha = QCheckBox(self.centralwidget)
        self.checkSalvarSenha.setObjectName(u"checkSalvarSenha")
        font2 = QFont()
        font2.setPointSize(11)
        self.checkSalvarSenha.setFont(font2)
        self.checkSalvarSenha.setCursor(QCursor(Qt.PointingHandCursor))
        self.checkSalvarSenha.setStyleSheet(u"color: rgb(248, 248, 242);")

        self.verticalLayout.addWidget(self.checkSalvarSenha)

        self.buttonsLayout = QHBoxLayout()
        self.buttonsLayout.setSpacing(8)
        self.buttonsLayout.setObjectName(u"buttonsLayout")
        self.buttonsLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.buttonsLayout.setContentsMargins(5, 5, 5, 5)
        self.pushGerarSenha = QPushButton(self.centralwidget)
        self.pushGerarSenha.setObjectName(u"pushGerarSenha")
        self.pushGerarSenha.setMinimumSize(QSize(0, 40))
        font3 = QFont()
        font3.setPointSize(14)
        self.pushGerarSenha.setFont(font3)
        self.pushGerarSenha.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushGerarSenha.setStyleSheet(u"background-color: rgb(80, 250, 123);")

        self.buttonsLayout.addWidget(self.pushGerarSenha)

        self.pushLimpar = QPushButton(self.centralwidget)
        self.pushLimpar.setObjectName(u"pushLimpar")
        self.pushLimpar.setMinimumSize(QSize(0, 40))
        self.pushLimpar.setFont(font3)
        self.pushLimpar.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushLimpar.setStyleSheet(u"background-color: rgb(98, 114, 164);")

        self.buttonsLayout.addWidget(self.pushLimpar)

        self.pushSair = QPushButton(self.centralwidget)
        self.pushSair.setObjectName(u"pushSair")
        self.pushSair.setMinimumSize(QSize(0, 40))
        self.pushSair.setFont(font3)
        self.pushSair.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushSair.setStyleSheet(u"background-color: rgb(255, 85, 85);")

        self.buttonsLayout.addWidget(self.pushSair)

        self.buttonsLayout.setStretch(0, 3)
        self.buttonsLayout.setStretch(1, 2)
        self.buttonsLayout.setStretch(2, 2)

        self.verticalLayout.addLayout(self.buttonsLayout)

        self.listSaida = QListWidget(self.centralwidget)
        self.listSaida.setObjectName(u"listSaida")
        font4 = QFont()
        font4.setFamilies([u"Monospace"])
        font4.setPointSize(14)
        self.listSaida.setFont(font4)
        self.listSaida.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.listSaida.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.listSaida.setStyleSheet(u"color: rgb(248, 248, 242);\n"
"background-color: rgb(68, 71, 90);")
        self.listSaida.setAutoScrollMargin(16)
        self.listSaida.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listSaida.setProperty("showDropIndicator", False)
        self.listSaida.setDragEnabled(False)
        self.listSaida.setDragDropOverwriteMode(False)
        self.listSaida.setDragDropMode(QAbstractItemView.DragOnly)
        self.listSaida.setSelectionMode(QAbstractItemView.SingleSelection)
        self.listSaida.setMovement(QListView.Free)
        self.listSaida.setProperty("isWrapping", False)
        self.listSaida.setResizeMode(QListView.Fixed)
        self.listSaida.setSelectionRectVisible(True)

        self.verticalLayout.addWidget(self.listSaida)

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
        self.checkSalvarSenha.setText(QCoreApplication.translate("MainWindow", u"Salvar senha", None))
        self.pushGerarSenha.setText(QCoreApplication.translate("MainWindow", u"Gerar Senha", None))
        self.pushLimpar.setText(QCoreApplication.translate("MainWindow", u"Limpar", None))
        self.pushSair.setText(QCoreApplication.translate("MainWindow", u"Sair", None))
    # retranslateUi

