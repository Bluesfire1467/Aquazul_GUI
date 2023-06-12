from GUI.Mainmenu.Pantallas.Address.Ui_DireccionScreen import Ui_DireccionScreen
from PyQt5.QtWidgets import QMainWindow


class Address(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_DireccionScreen()
        self.ui.setupUi(self)
