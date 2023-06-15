from GUI.Mainmenu.Pantallas.Habitat.Ui_HabitatScreen import Ui_HabitatScreen
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSignal


class Habitat(QMainWindow):
    closed = pyqtSignal()

    def __init__(self, conn):
        super().__init__()
        self.ui = Ui_HabitatScreen()
        self.ui.setupUi(self)
        self.conn = conn

    def closeEvent(self, event):
        self.closed.emit()
        event.accept()
