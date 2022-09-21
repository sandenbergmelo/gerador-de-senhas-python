from PySide6.QtWidgets import QMessageBox


def pop_up(title, txt, icon='information'):
    icons = {'information': QMessageBox.Information,
             'warning': QMessageBox.Warning,
             'critical': QMessageBox.Critical,
             'question': QMessageBox.Question,
             'no_icon': QMessageBox.NoIcon}

    msg = QMessageBox()
    msg.setWindowTitle(title)
    msg.setIcon(icons[icon])
    msg.setText(txt)
    msg.setStyleSheet('color: #f8f8f2; background-color: #282a36;')
    msg.exec()
