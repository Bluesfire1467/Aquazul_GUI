from GUI.Mainmenu.Pantallas.Animal.Ui_AnimalScreen import Ui_AnimalScreen
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSignal


class Animal(QMainWindow):
    closed = pyqtSignal()

    def __init__(self, conn):
        super().__init__()
        self.ui = Ui_AnimalScreen()
        self.ui.setupUi(self)
        self.conn = conn

    def closeEvent(self, event):
        self.closed.emit()
        event.accept()
