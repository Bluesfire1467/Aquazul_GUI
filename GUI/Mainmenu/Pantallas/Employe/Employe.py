from GUI.Mainmenu.Pantallas.Employe.Ui_EmpleadoScreen import Ui_EmpleadoScreen
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys

class Employe(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_EmpleadoScreen()
        self.ui.setupUi(self)


app = QApplication(sys.argv)
w = Employe()
w.show()
sys.exit(app.exec_())