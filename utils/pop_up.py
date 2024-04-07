from typing import Literal
from PySide6.QtWidgets import QMessageBox

IconType = Literal['information', 'warning', 'critical', 'question']
icons = {'information': QMessageBox.Information,
         'warning': QMessageBox.Warning,
         'critical': QMessageBox.Critical,
         'question': QMessageBox.Question}


def pop_up(title: str, txt: str, icon: IconType = 'information') -> None:
    msg = QMessageBox()
    msg.setWindowTitle(title)
    msg.setIcon(icons[icon])
    msg.setText(txt)
    msg.setStyleSheet('color: #f8f8f2; background-color: #282a36;')
    msg.exec()
