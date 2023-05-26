import sys
import os
from Oracle.Connection_Oracle import Connection_Oracle
from PyQt5.QtWidgets import QApplication, QMainWindow
from LogInInterface import Ui_LogIn

class LogIn(QMainWindow):

	def __init__(self):
		super().__init__()
		self.ui = Ui_LogIn()
		self.ui.setupUi(self)

		# Conectar la accion al boton
		self.ui.pushButtonAccept.clicked.connect(self.button_clicked)

	def button_clicked(self):

		user = self.ui.lineEditUser.text()
		password = self.ui.lineEditPassword.text()
		print(user)
		print(password)
		connection = Connection_Oracle()
		connection.open(user, password)
		# print("desconectando...")
		# connection.close()


app = QApplication(sys.argv)
w = LogIn()
w.show()
sys.exit(app.exec_())