from GUI.Mainmenu.Pantallas.State.Ui_EstadoScreen import Ui_EstadoScreen
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidget, QTableWidgetItem
import sys
from Oracle import Connection_Oracle as conn
from GUI.PopUpWindow.PopUpWindow import ok_information_window

class State(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_EstadoScreen()
        self.ui.setupUi(self)

        #agregar estado
        self.ui.btn_agregar.clicked.connect(self.agregarEstado)

        #eliminar estado
        self.ui.btn_borrar.clicked.connect(self.eliminarEstado)

        #refrescar tabla
        self.ui.pushButton.clicked.connect(self.refreshTable)

    def showEvent(self,event):
        super().showEvent(event)
        # Mostrar tabla Tipo de agua en la tabla
        #self.ui.btn_borrar.clicked.connect(self.show_table)
        coneccionTemp = conn.Connection_Oracle()
        coneccionTemp.open("developer", "PassDev")

        consulta = str("SELECT * FROM estado")

        States = coneccionTemp.query_execution(consulta)

        f = len(States)  # No. filas
        c = len(States[0])  # No. columnas

        print(States)

        self.ui.table_estado.setRowCount(f)
        self.ui.table_estado.setColumnCount(c)
        self.ui.table_estado.setHorizontalHeaderLabels(['ID', 'Estado'])
        self.ui.table_estado.verticalHeader().setVisible(False)

        for i in range(f):
            for j in range(c):
                self.ui.table_estado.setItem(i, j, QTableWidgetItem(str(States[i][j])))
                print(States[i][j])
        self.ui.table_estado.show()
        coneccionTemp.close()

    def agregarEstado(self):
        coneccionTemp = conn.Connection_Oracle()
        coneccionTemp.open("developer","PassDev")

        regist = str(self.ui.line_estado.text())

        if len(regist) == 0:
            ok_information_window("Ingresa el estado!!","ayuda")
            return

        consulta = str(f"""insert into estado (id_estado, nombre_estado) values ((select max(estado.id_estado)from estado)+1,'{regist}')""")

        print(consulta)
        print(type(consulta))
        coneccionTemp.query_insert(consulta)
        coneccionTemp.close()

    def eliminarEstado(self):
        coneccionTemp = conn.Connection_Oracle()
        coneccionTemp.open("developer", "PassDev")

        regist = str(self.ui.line_estado.text())

        if len(regist) == 0:
            ok_information_window("Ingresa el estado!!", "ayuda")
            return

        buscar = str(f"""select id_estado from estado where nombre_estado = '{regist}'""")
        print(buscar)
        IDreg = (coneccionTemp.query_execution(buscar))
        ID = IDreg[0][0]
        print(ID)
        consulta = str(f"""delete from estado where id_estado = {ID}""")
        print(consulta)
        coneccionTemp.query_insert(consulta)
        coneccionTemp.close()

    def refreshTable(self):
        coneccionTemp = conn.Connection_Oracle()
        coneccionTemp.open("developer", "PassDev")

        consulta = str("SELECT * FROM estado")

        States = coneccionTemp.query_execution(consulta)

        f = len(States)  # No. filas
        c = len(States[0])  # No. columnas

        print(States)

        self.ui.table_estado.setRowCount(f)
        self.ui.table_estado.setColumnCount(c)
        self.ui.table_estado.setHorizontalHeaderLabels(['ID', 'Estado'])
        self.ui.table_estado.verticalHeader().setVisible(False)

        for i in range(f):
            for j in range(c):
                self.ui.table_estado.setItem(i, j, QTableWidgetItem(str(States[i][j])))
                print(States[i][j])
        self.ui.table_estado.show()
        coneccionTemp.close()




app = QApplication(sys.argv)
w = State()
w.show()
sys.exit(app.exec_())