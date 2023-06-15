from GUI.Mainmenu.Pantallas.AquariumBranch.Ui_SucursalScreen import Ui_SucursalScreen
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSignal


class AquariumBranch(QMainWindow):
    closed = pyqtSignal()

    def __init__(self, conn):
        super().__init__()
        self.ui = Ui_SucursalScreen()
        self.ui.setupUi(self)
        self.conn = conn

    def closeEvent(self, event):
        self.closed.emit()
        event.accept()
