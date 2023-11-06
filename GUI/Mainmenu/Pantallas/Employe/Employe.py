from GUI.Mainmenu.Pantallas.Employe.Ui_EmpleadoScreen import Ui_EmpleadoScreen
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import pyqtSignal
from Oracle.Connection_Oracle import Connection_Oracle
from PyQt5.QtWidgets import *
from GUI.PopUpWindow.PopUpWindow import ok_information_window
import sys


class Employe(QMainWindow):
    closed = pyqtSignal()

    def __init__(self, conn):
        super().__init__()
        self.ui = Ui_EmpleadoScreen()
        self.ui.setupUi(self)
        self.id_inter = None
        self.conn = conn

        #self.ui.table_empleado.cellClicked.connect(self.get_row)

    def closeEvent(self, event):
        self.closed.emit()
        event.accept()

    def showEvent(self, event):
        super().showEvent(event)
        self.refreshtable()
        #self.set_sucursal()

    def set_sucursal(self):
        query = str('''SELECT NOMBRE_SUCURSAL FROM SUCURSAL''')
        self.conn.q_open()
        db_data = self.conn.query_execution(query)
        db_data = [element[0] for element in db_data]
        print(db_data)

        self.ui.line_sucursal.addItems(db_data)
        self.ui.line_sucursal.show()
        self.conn.close()

    def refreshtable(self):
        query = str('''SELECT 
        ID_EMPLEADO, 
        NOMBRE_EMPLEADO, 
        APELLIDO_PATERNO, 
        APELLIDO_MATERNO, 
        TIPO_DE_EMPLEADO, 
        NOMBRE_SUCURSAL, 
        ALCALDIA_MUNICIPIO ||\' '|| COLONIA ||\' '|| CALLE ||\' '|| CP, 
        CORREO
        FROM EMPLEADO E
        JOIN SUCURSAL S ON E.ID_SUCURSAL = S.ID_SUCURSAL
        JOIN DIRECCION D ON E.ID_DIRECCION = D.ID_DIRECCION
        JOIN CORREO C ON E.ID_CORREO = C.ID_CORREO
        ORDER BY ID_EMPLEADO ASC''')
        self.conn.q_open()
        self.db_data = self.conn.query_execution(query)
        print(self.db_data)

        f = len(self.db_data)  # No. filas
        c = len(self.db_data[0])  # No. columnas
        headers = ['No.',
                   'Nombre',
                   'Apellido paterno',
                   'Apellido materno',
                   'Tipo de empleado',
                   'Sucursal',
                   'Direccion',
                   'Correo']

        self.ui.table_empleado.setRowCount(f)
        self.ui.table_empleado.setColumnCount(c)
        self.ui.table_empleado.setHorizontalHeaderLabels(headers)
        self.ui.table_empleado.verticalHeader().setVisible(False)
        self.print_table(f, c)
        self.ui.table_empleado.show()
        self.conn.close()

    def addEmploye(self):
        self.conn.q_open()

        register = str(self.ui.line)

    def print_table(self, f, c):
        for i in range(f):
            for j in range(c):
                self.ui.table_empleado.setItem(i, j, QTableWidgetItem(str(self.db_data[i][j])))
                print(self.db_data[i][j])

    def cell_to_line(self, row, column):
        self.conn.q_open()

        print(row, column)
        listcell = []
        for i in range(8):
            listcell.append(self.ui.table_animal.item(row,i).text())

        self.id_inter = listcell
        self.ui.line_nombre.setText(listcell[1])
        self.ui.line_apellidopaterno.setText(listcell[2])
        self.ui.line_apellidomaterno.setText(listcell[3])
        self.ui.line_descripcion.setText(listcell[4])

        ID_ALIMENTACION = int(listcell[4])
        ID_PELIGRO = int(listcell[5])
        ID_HABITAT = int(listcell[6])
        ID_ESPECIE = int(listcell[7])
        ID_SUCURSAL = int(listcell[8])


        #extrayendo compos para que coincidan
        buscar = str(f"""SELECT alimentacion FROM alimentacion WHERE id_alimentacion = '{ID_ALIMENTACION}'""")
        ID_ALIMENTACION = (self.conn.query_execution(buscar))
        ID_ALIMENTACION = ID_ALIMENTACION[0][0]

        buscar = str(f"""SELECT peligro FROM peligro WHERE id_peligro = '{ID_PELIGRO}'""")
        ID_PELIGRO = (self.conn.query_execution(buscar))
        ID_PELIGRO = ID_PELIGRO[0][0]

        buscar = str(f"""SELECT nombre_habitat FROM habitat WHERE id_habitat = '{ID_HABITAT}'""")
        ID_HABITAT = (self.conn.query_execution(buscar))
        ID_HABITAT = ID_HABITAT[0][0]

        buscar = str(f"""SELECT nombre_comun FROM especie WHERE id_especie = '{ID_ESPECIE}'""")
        ID_ESPECIE = (self.conn.query_execution(buscar))
        ID_ESPECIE = ID_ESPECIE[0][0]

        buscar = str(f"""SELECT nombre_sucursal FROM sucursal WHERE id_sucursal = '{ID_SUCURSAL}'""")
        ID_SUCURSAL = (self.conn.query_execution(buscar))
        ID_SUCURSAL = ID_SUCURSAL[0][0]

        self.ui.comboBox_tipoalimentacion.setCurrentText(ID_ALIMENTACION)
        self.ui.comboBox_peligro.setCurrentText(ID_PELIGRO)
        self.ui.comboBox_habitat.setCurrentText(ID_HABITAT)
        self.ui.comboBox_especie.setCurrentText(ID_ESPECIE)
        self.ui.comboBox_sucursal.setCurrentText(ID_SUCURSAL)

        self.conn.close()

