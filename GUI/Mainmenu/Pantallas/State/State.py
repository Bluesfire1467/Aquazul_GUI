from GUI.Mainmenu.Pantallas.State.Ui_EstadoScreen import Ui_EstadoScreen
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys

class State(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_EstadoScreen()
        self.ui.setupUi(self)



app = QApplication(sys.argv)
w = State()
w.show()
sys.exit(app.exec_())