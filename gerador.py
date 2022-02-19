from PyQt5 import QtWidgets, uic
from gerador_cli import gerar_senha
from ui.pop_up import pop_up

def salvar_senha(senha):

    options = QtWidgets.QFileDialog.Options()
    options |= QtWidgets.QFileDialog.DontUseNativeDialog
    options |= QtWidgets.QFileDialog.DontConfirmOverwrite

    arquivo = QtWidgets.QFileDialog.getSaveFileName(
        None,
        caption='Salvar senha',
        directory='senhas.txt',
        filter='Arquivo de texto (*.txt);;Todos os arquivos (*)',
        options=options
    )[0]

    if arquivo != '':
        with open(arquivo, 'a') as senhas:
            senhas.write(f'{senha}\n')
        return True
    else:
        return False

def main():
    letras = int(form.spinLetras.value())
    numeros = int(form.spinNumeros.value())
    caracteres = int(form.spinCaracteres.value())

    if letras != 0 or numeros != 0 or caracteres != 0:
        senha = gerar_senha(letras, numeros, caracteres)

        saida = form.listSaida
        saida.addItem(senha)
        saida.scrollToBottom()

        if form.checkSalvarSenha.isChecked():
            salvo = salvar_senha(senha)
            if salvo:
                pop_up(
                    'Senha Salva!',
                    QtWidgets.QMessageBox.Information,
                    'Senha salva com sucesso!'
                )
            else:
                pop_up(
                    'Erro ao salvar senha!',
                    QtWidgets.QMessageBox.Critical,
                    'Erro ao salvar senha!'
                )
    else:
        pop_up(
            'Erro',
            QtWidgets.QMessageBox.Warning,
            'Impossível gerar senha vazia!'
        )

app = QtWidgets.QApplication([])
form = uic.loadUi("ui/form.ui")
form.pushGerarSenha.clicked.connect(main)
form.pushLimpar.clicked.connect(form.listSaida.clear)
form.pushSair.clicked.connect(app.quit)

form.show()
app.exec()
