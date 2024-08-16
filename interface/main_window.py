from platform import system

from PySide6.QtWidgets import QFileDialog, QMainWindow

from interface.ui_main_window import Ui_MainWindow
from utils.cli_gen import generate_password
from utils.msg_box import msg_box


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # Buttons actions
        self.pushGeneratePassword.clicked.connect(self.main)
        self.pushClean.clicked.connect(self.listOutput.clear)
        self.pushExit.clicked.connect(self.close)

    def save_password(self, password: str) -> bool:
        # Save options for the file dialog
        file_dialog = QFileDialog()

        options = file_dialog.options()
        options |= file_dialog.Option.DontConfirmOverwrite
        if system() == 'Linux':
            options |= file_dialog.Option.DontUseNativeDialog

        file_path = file_dialog.getSaveFileName(  # Open the file dialog
            self,
            caption='Salvar senha',
            dir='senhas.txt',
            filter='Arquivo de texto (*.txt);;Todos os arquivos (*)',
            options=options,
        )[0]

        if not file_path:
            return False

        with open(file_path, 'a') as senhas:  # noqa: PLW1514
            senhas.write(f'{password}\n')

        return True

    def main(self) -> None:
        num_letters = int(self.spinLetters.value())
        num_numbers = int(self.spinNumbers.value())
        num_chars = int(self.spinChars.value())

        if num_letters == num_numbers == num_chars == 0:
            msg_box('Erro', 'Impossível gerar senha vazia!', 'critical')
            return

        password = generate_password(num_letters, num_numbers, num_chars)

        self.listOutput.addItem(password)
        self.listOutput.scrollToBottom()

        if not self.checkSavePassword.isChecked():
            return

        saved = self.save_password(password)

        if not saved:
            # Se a senha não foi salva mostra uma mensagem de erro e retorna
            msg_box('Erro!', 'Erro ao salvar senha!', 'information')
            return

        msg_box('Senha Salva!', 'Senha salva com sucesso!', 'information')
