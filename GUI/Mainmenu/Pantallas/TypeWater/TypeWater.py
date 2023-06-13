from GUI.Mainmenu.Pantallas.TypeWater.Ui_TipoAguaScreen import Ui_TipoAguaScreen
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import pyqtSignal
import sys
from Oracle.Connection_Oracle import Connection_Oracle as conn

class TypeofWater(QMainWindow):
    closed = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.ui = Ui_TipoAguaScreen()
        self.ui.setupUi(self)

    def closeEvent(self, event):
        self.closed.emit()
        event.accept()
