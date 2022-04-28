from platform import system
from PyQt5 import QtWidgets, uic
from gerador_cli import gerar_senha
from gui.pop_up import pop_up

def salvar_senha(senha):
    # Opções de salvamento
    options = QtWidgets.QFileDialog.Options()
    options |= QtWidgets.QFileDialog.DontConfirmOverwrite
    if system() == 'Linux':
        options |= QtWidgets.QFileDialog.DontUseNativeDialog

    arquivo = QtWidgets.QFileDialog.getSaveFileName(# Abre janela de salvamento
        None,
        caption='Salvar senha',
        directory='senhas.txt',
        filter='Arquivo de texto (*.txt);;Todos os arquivos (*)',
        options=options
    )[0]

    if arquivo == '': # Se o usuário não selecionou um arquivo
        return False

    # Salva a senha no arquivo
    with open(arquivo, 'a') as senhas:
            senhas.write(f'{senha}\n')
    return True


def main():
    # Pega os valores dos campos
    letras = int(tela.spinLetras.value())
    numeros = int(tela.spinNumeros.value())
    caracteres = int(tela.spinCaracteres.value())

    if letras == 0 and numeros == 0 and caracteres == 0:
        pop_up(
            'Erro',
            QtWidgets.QMessageBox.Warning,
            'Impossível gerar senha vazia!'
        )
        return

    senha = gerar_senha(letras, numeros, caracteres)

    # Mostra a senha na tela
    saida = tela.listSaida
    saida.addItem(senha)
    saida.scrollToBottom()

    if not tela.checkSalvarSenha.isChecked():
        # Se o usuário não quer salvar a senha, retorna
        return

    salvo = salvar_senha(senha)
    if not salvo:
        # Se a senha não foi salva mostra uma mensagem de erro e retorna
        pop_up(
            'Erro ao salvar senha!',
            QtWidgets.QMessageBox.Critical,
            'Erro ao salvar senha!'
        )
        return

    pop_up(
        'Senha Salva!',
        QtWidgets.QMessageBox.Information,
        'Senha salva com sucesso!'
    )

# Inicialização do programa
app = QtWidgets.QApplication([])
tela = uic.loadUi("gui/ui/tela.ui")

app.setStyle('Fusion')

# Eventos dos botões da tela
tela.pushGerarSenha.clicked.connect(main)
tela.pushLimpar.clicked.connect(tela.listSaida.clear)
tela.pushSair.clicked.connect(app.quit)

# Exibir tela
tela.show()
app.exec()
