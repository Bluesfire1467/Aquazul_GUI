from PyQt5.QtCore import pyqtSignal
from GUI.Mainmenu.Pantallas.Species.Ui_EspecieScreen import Ui_EspecieScreen
from PyQt5.QtWidgets import QMainWindow


class Species(QMainWindow):
    closed = pyqtSignal()

    def __init__(self, conn):
        super().__init__()
        self.ui = Ui_EspecieScreen()
        self.ui.setupUi(self)
        self.conn = conn

    def closeEvent(self, event):
        self.closed.emit()
        event.accept()
