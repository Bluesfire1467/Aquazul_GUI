from GUI.Mainmenu.Pantallas.Email.Ui_CorreoScreen import Ui_CorreoScreen
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys

class Email(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_CorreoScreen()
        self.ui.setupUi(self)


app = QApplication(sys.argv)
w = Email()
w.show()
sys.exit(app.exec_())