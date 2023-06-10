from Oracle.Connection_Oracle import Connection_Oracle
from PyQt5.QtWidgets import QMainWindow
from GUI.LogIn.LogInInterface import Ui_LogIn
from GUI.PopUpWindow.PopUpWindow import ok_information_window


class LogIn(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_LogIn()
        self.connection = None
        self.ui.setupUi(self)

        # Conectar la accion al boton
        self.ui.pushButtonAccept.clicked.connect(self.button_clicked)
        # Saltar de un lineEdit a otro
        self.ui.lineEditUser.returnPressed.connect(self.enter_jump_key_press_event)
        # Conectar el evento de la tecla enter a enterKeyPressEvent
        self.ui.lineEditPassword.returnPressed.connect(self.enter_key_press_event)

    def button_clicked(self):
        user = self.ui.lineEditUser.text()
        password = self.ui.lineEditPassword.text()
        self.connection = Connection_Oracle()

        if self.connection.open(user, password):
            print('Exito')  # mandar a llamar a la siguiente ventana
        else:
            # Ventana emergente de información
            msg = 'El usuario o la contraseña son incorrectos, vuelva a intentarlo'
            type_inf = 'Ayuda'
            ok_information_window(msg, type_inf)

        self.connection.close()

    def enter_key_press_event(self):
        self.button_clicked()

    def enter_jump_key_press_event(self):
        current_widget = self.focusWidget()
        current_widget.focusNextPrevChild(True)

    def get_connection(self) -> Connection_Oracle:
        return self.connection
