# Ventanas emergentes que se lleguen a utilizar
from PyQt5.QtWidgets import QMessageBox


def ok_information_window(msg, type_inf):
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Information)
    msg_box.setText(msg)
    msg_box.setWindowTitle(type_inf)
    msg_box.setStandardButtons(QMessageBox.Ok)
    msg_box.exec_()
