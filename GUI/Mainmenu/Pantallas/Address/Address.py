from GUI.Mainmenu.Pantallas.Address.Ui_DireccionScreen import Ui_DireccionScreen
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
from Oracle.Connection_Oracle import Connection_Oracle


class Address(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_DireccionScreen()
        self.ui.setupUi(self)

    def show_table(self):
        self.ui.table_direccion()
        print('')


app = QApplication(sys.argv)
w = Address()
w.show()
sys.exit(app.exec_())