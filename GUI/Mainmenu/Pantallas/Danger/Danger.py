from GUI.Mainmenu.Pantallas.Danger.Ui_PeligroScreen import Ui_PeligroScreen
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys

class Danger(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_PeligroScreen()
        self.ui.setupUi(self)


app = QApplication(sys.argv)
w = Danger()
w.show()
sys.exit(app.exec_())