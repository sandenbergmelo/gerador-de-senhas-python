from PyQt5 import QtWidgets, uic
from gerador_cli import gerar_senha
from platform import system
from ui.pop_up import pop_up

def salvar_senha(senha):

    options = QtWidgets.QFileDialog.Options()
    options |= QtWidgets.QFileDialog.DontConfirmOverwrite
    if system() == 'Linux':
        options |= QtWidgets.QFileDialog.DontUseNativeDialog

    arquivo = QtWidgets.QFileDialog.getSaveFileName(
        None,
        caption='Salvar senha',
        directory='senhas.txt',
        filter='Arquivo de texto (*.txt);;Todos os arquivos (*)',
        options=options
    )[0]

    if arquivo == '':
        return False
    
    with open(arquivo, 'a') as senhas:
            senhas.write(f'{senha}\n')
    return True

def main():
    
    letras = int(tela.spinLetras.value())
    numeros = int(tela.spinNumeros.value())
    caracteres = int(tela.spinCaracteres.value())

    if letras != 0 or numeros != 0 or caracteres != 0:
        senha = gerar_senha(letras, numeros, caracteres)

        saida = tela.listSaida
        saida.addItem(senha)
        saida.scrollToBottom()

        if tela.checkSalvarSenha.isChecked():
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
tela = uic.loadUi("ui/tela.ui")
tela.pushGerarSenha.clicked.connect(main)
tela.pushLimpar.clicked.connect(tela.listSaida.clear)
tela.pushSair.clicked.connect(app.quit)

tela.show()
app.exec()
