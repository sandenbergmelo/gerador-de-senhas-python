from PyQt5 import QtWidgets, uic
from gerador_cli import gerar_senha, salvar_senha

def main():
    letras = int(form.spinLetras.value())
    numeros = int(form.spinNumeros.value())
    caracteres = int(form.spinCaracteres.value())

    if letras != 0 or numeros != 0 or caracteres != 0:
        senha = gerar_senha(letras, numeros, caracteres)

        saida = form.listSaida
        saida.addItem(senha)

        if form.checkSalvarSenha.isChecked():
            salvar(senha)
    else:
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Erro")
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setText("Impossível gerar senha vazia!")
        msg.exec()

def limpar_saida():
    form.listSaida.clear()

def salvar(senha):
    salvar_senha(senha)

    msg = QtWidgets.QMessageBox()
    msg.setWindowTitle("Senha salva!")
    msg.setIcon(QtWidgets.QMessageBox.Information)
    msg.setText("Senha salva com sucesso em senhas.txt")
    msg.exec()

app = QtWidgets.QApplication([])
form = uic.loadUi("ui/form.ui")
form.pushGerarSenha.clicked.connect(main)
form.pushLimpar.clicked.connect(limpar_saida)
form.pushSair.clicked.connect(app.quit)

form.show()
app.exec()
