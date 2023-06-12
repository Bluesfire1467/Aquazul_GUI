from GUI.Mainmenu.Pantallas.Habitat.Ui_HabitatScreen import Ui_HabitatScreen
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys

class Habitat(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_HabitatScreen()
        self.ui.setupUi(self)



app = QApplication(sys.argv)
w = Habitat()
w.show()
sys.exit(app.exec_())