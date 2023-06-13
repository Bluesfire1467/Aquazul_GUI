from GUI.Mainmenu.Pantallas.Email.Ui_CorreoScreen import Ui_CorreoScreen
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import pyqtSignal
import sys

class Email(QMainWindow):
    closed = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.ui = Ui_CorreoScreen()
        self.ui.setupUi(self)

    def closeEvent(self, event):
        self.closed.emit()
        event.accept()
