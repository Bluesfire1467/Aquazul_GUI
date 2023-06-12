from GUI.Mainmenu.Pantallas.Animal.Ui_AnimalScreen import Ui_AnimalScreen
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
from Oracle.Connection_Oracle import Connection_Oracle


class Animal(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_AnimalScreen()
        self.ui.setupUi(self)



app = QApplication(sys.argv)
w = Animal()
w.show()
sys.exit(app.exec_())