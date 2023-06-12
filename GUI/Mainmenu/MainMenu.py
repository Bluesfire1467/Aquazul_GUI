from GUI.Mainmenu.Ui_WIndow_Aquazul import Ui_WIndow_Aquazul
from Oracle import Connection_Oracle as conn
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMainWindow


class MainMenu(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_WIndow_Aquazul()
        self.ui.setupUi(self)


app = QApplication(sys.argv)
w = MainMenu()
w.show()
sys.exit(app.exec_())
