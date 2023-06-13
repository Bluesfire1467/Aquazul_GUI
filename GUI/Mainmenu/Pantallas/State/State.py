from GUI.Mainmenu.Pantallas.State.Ui_EstadoScreen import Ui_EstadoScreen
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import pyqtSignal
import sys

class State(QMainWindow):
    closed = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.ui = Ui_EstadoScreen()
        self.ui.setupUi(self)

    def closeEvent(self, event):
        self.closed.emit()
        event.accept()
