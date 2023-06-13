from GUI.Mainmenu.Pantallas.Habitat.Ui_HabitatScreen import Ui_HabitatScreen
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import pyqtSignal
import sys

class Habitat(QMainWindow):
    closed = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.ui = Ui_HabitatScreen()
        self.ui.setupUi(self)

    def closeEvent(self, event):
        self.closed.emit()
        event.accept()
