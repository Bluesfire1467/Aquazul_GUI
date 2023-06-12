from GUI.Mainmenu.Pantallas.AquariumBranch.Ui_SucursalScreen import Ui_SucursalScreen
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
from Oracle.Connection_Oracle import Connection_Oracle


class AquariumBranch(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_SucursalScreen()
        self.ui.setupUi(self)



app = QApplication(sys.argv)
w = AquariumBranch()
w.show()
sys.exit(app.exec_())