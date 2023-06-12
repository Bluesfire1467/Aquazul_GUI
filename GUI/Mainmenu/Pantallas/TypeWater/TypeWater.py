from GUI.Mainmenu.Pantallas.TypeWater.Ui_TipoAguaScreen import Ui_TipoAguaScreen
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
from Oracle.Connection_Oracle import Connection_Oracle as conn

class TypeofWater(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_TipoAguaScreen()
        self.ui.setupUi(self)

    def show_table(self):
        self.ui.table_tipoagua()
        print('')


app = QApplication(sys.argv)
w = TypeofWater()
w.show()
sys.exit(app.exec_())