from GUI.Mainmenu.Pantallas.Feeding.Ui_AlimentacionScreen import Ui_AlimentacionScreen
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSignal


class Feeding(QMainWindow):
    closed = pyqtSignal()

    def __init__(self, conn):
        super().__init__()
        self.ui = Ui_AlimentacionScreen()
        self.ui.setupUi(self)
        self.conn = conn

    def closeEvent(self, event):
        self.closed.emit()
        event.accept()
