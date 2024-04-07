from platform import system

from PySide6.QtWidgets import QFileDialog, QMainWindow

from interface.UI_main_window import Ui_MainWindow
from utils.cli_gen import generate_password
from utils.pop_up import pop_up


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # Buttons actions
        self.pushGeneratePassword.clicked.connect(self.main)
        self.pushClean.clicked.connect(self.listOutput.clear)
        self.pushExit.clicked.connect(self.close)

    def save_password(self, password: str) -> None:
        # Save options for the file dialog
        options = QFileDialog.Options()
        options |= QFileDialog.DontConfirmOverwrite
        if system() == 'Linux':
            options |= QFileDialog.DontUseNativeDialog

        file_path = QFileDialog.getSaveFileName(  # Open the file dialog
            self,
            caption='Salvar senha',
            dir='senhas.txt',
            filter='Arquivo de texto (*.txt);;Todos os arquivos (*)',
            options=options
        )[0]

        if file_path == '':
            return False

        with open(file_path, 'a') as senhas:
            senhas.write(f'{password}\n')

        return True

    def main(self) -> None:
        num_letters = int(self.spinLetters.value())
        num_numbers = int(self.spinNumbers.value())
        num_chars = int(self.spinChars.value())

        if num_letters == num_numbers == num_chars == 0:
            pop_up('Erro', 'Impossível gerar senha vazia!', 'critical')
            return

        password = generate_password(num_letters, num_numbers, num_chars)

        self.listOutput.addItem(password)
        self.listOutput.scrollToBottom()

        if not self.checkSavePassword.isChecked():
            return

        saved = self.save_password(password)

        if not saved:
            # Se a senha não foi salva mostra uma mensagem de erro e retorna
            pop_up('Erro!', 'Erro ao salvar senha!', 'information')
            return

        pop_up('Senha Salva!', 'Senha salva com sucesso!', 'information')
