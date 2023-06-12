from GUI.Mainmenu.Pantallas.Material.Ui_MaterialScreen import Ui_MaterialScreen
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys

class Material(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MaterialScreen()
        self.ui.setupUi(self)



app = QApplication(sys.argv)
w = Material()
w.show()
sys.exit(app.exec_())