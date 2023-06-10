from Oracle import Connection_Oracle as conn
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from GUI.LogIn.LogIn import LogIn
from GUI.LogIn.LogInInterface import Ui_LogIn

app = QApplication(sys.argv)
w = LogIn()
w.show()
sys.exit(app.exec_())