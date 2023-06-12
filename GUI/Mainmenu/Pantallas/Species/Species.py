from GUI.Mainmenu.Pantallas.Species.Ui_EspecieScreen import Ui_EspecieScreen
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys

class Species(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_EspecieScreen()
        self.ui.setupUi(self)



app = QApplication(sys.argv)
w = Species()
w.show()
sys.exit(app.exec_())