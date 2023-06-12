import sys
from Oracle import Connection_Oracle as conn
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from GUI.LogIn.LogIn import LogIn
from GUI.Mainmenu.MainMenu import MainMenu
from GUI.LogIn.LogInInterface import Ui_LogIn


def main():
    app = QApplication(sys.argv)

    # Crear la primera interfaz
    #log_in = LogIn()
    main_menu = MainMenu()
    #log_in.login_successful.connect(main_menu.show())
    #log_in.show()
    #conn = log_in.get_connection()
    main_menu.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
