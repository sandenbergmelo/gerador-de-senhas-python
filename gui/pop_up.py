from PyQt5 import QtWidgets

def pop_up(titulo, icone, texto):
    msg = QtWidgets.QMessageBox()
    msg.setWindowTitle(titulo)
    msg.setIcon(icone)
    msg.setText(texto)
    msg.setStyleSheet('color: #f8f8f2; background-color: #282a36;')
    msg.exec()
