from GUI.Mainmenu.Pantallas.Address.Ui_DireccionScreen import Ui_DireccionScreen
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import pyqtSignal
import sys
from Oracle.Connection_Oracle import Connection_Oracle


class Address(QMainWindow):
    closed = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.ui = Ui_DireccionScreen()
        self.ui.setupUi(self)

    def closeEvent(self, event):
        self.closed.emit()
        event.accept()
