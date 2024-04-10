from typing import Literal
from PySide6.QtWidgets import QMessageBox

IconType = Literal['information', 'warning', 'critical', 'question']
icons = {'information': QMessageBox.Icon.Information,
         'warning': QMessageBox.Icon.Warning,
         'critical': QMessageBox.Icon.Critical,
         'question': QMessageBox.Icon.Question}


def msg_box(title: str, txt: str, icon: IconType = 'information') -> None:
    msg = QMessageBox()
    msg.setWindowTitle(title)
    msg.setText(txt)
    msg.setStyleSheet('color: #f8f8f2; background-color: #282a36;')
    msg.setIcon(icons[icon])
    msg.exec()
