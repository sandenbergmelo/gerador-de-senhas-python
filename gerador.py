from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
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
        pop_up("Erro", QMessageBox.Warning, "Impossível gerar senha vazia!")

def limpar_saida():
    form.listSaida.clear()

def salvar(senha):
    salvar_senha(senha)
    pop_up("Senha Salva", QMessageBox.Information, "Senha salva em senhas.txt")

def pop_up(titulo, icone, texto):
    msg = QMessageBox()
    msg.setWindowTitle(titulo)
    msg.setIcon(icone)
    msg.setText(texto)
    msg.exec()

app = QtWidgets.QApplication([])
form = uic.loadUi("ui/form.ui")
form.pushGerarSenha.clicked.connect(main)
form.pushLimpar.clicked.connect(limpar_saida)
form.pushSair.clicked.connect(app.quit)

form.show()
app.exec()
