from GUI.Mainmenu.Pantallas.Feeding.Ui_AlimentacionScreen import Ui_AlimentacionScreen
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys

class Feeding(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_AlimentacionScreen()
        self.ui.setupUi(self)



app = QApplication(sys.argv)
w = Feeding()
w.show()
sys.exit(app.exec_())