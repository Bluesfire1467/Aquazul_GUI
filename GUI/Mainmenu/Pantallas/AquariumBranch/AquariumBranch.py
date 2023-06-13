from GUI.Mainmenu.Pantallas.AquariumBranch.Ui_SucursalScreen import Ui_SucursalScreen
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import pyqtSignal
import sys
from Oracle.Connection_Oracle import Connection_Oracle


class AquariumBranch(QMainWindow):
    closed = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.ui = Ui_SucursalScreen()
        self.ui.setupUi(self)

    def closeEvent(self, event):
        self.closed.emit()
        event.accept()
