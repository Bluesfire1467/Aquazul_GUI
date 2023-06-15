from GUI.Mainmenu.Pantallas.Material.Ui_MaterialScreen import Ui_MaterialScreen
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSignal


class Material(QMainWindow):
    closed = pyqtSignal()

    def __init__(self, conn):
        super().__init__()
        self.ui = Ui_MaterialScreen()
        self.ui.setupUi(self)
        self.conn = conn

    def closeEvent(self, event):
        self.closed.emit()
        event.accept()
