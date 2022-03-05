from PyQt5 import QtWidgets

def pop_up(titulo, icone, texto):
    msg = QtWidgets.QMessageBox()
    msg.setWindowTitle(titulo)
    msg.setIcon(icone)
    msg.setText(texto)
    msg.exec()
