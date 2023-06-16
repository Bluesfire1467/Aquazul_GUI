from GUI.Mainmenu.Pantallas.Employe.Ui_EmpleadoScreen import Ui_EmpleadoScreen
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from PyQt5.QtCore import pyqtSignal


class Employe(QMainWindow):
    closed = pyqtSignal()

    def __init__(self, conn):
        super().__init__()
        self.ui = Ui_EmpleadoScreen()
        self.ui.setupUi(self)
        self.conn = conn

        self.ui.table_empleado.cellClicked.connect(self.get_row)

    def closeEvent(self, event):
        self.closed.emit()
        event.accept()

    def showEvent(self, event):
        super().showEvent(event)
        self.refreshtable()
        self.set_sucursal()

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

    def get_row(self, row, col):
        print(self.db_data[row])
        #self.ui.line_nombre.setText(self.db_data[row][0])
        #self.ui.line_apellidopaterno.setText(self.db_data[row][1])
        #self.ui.line_apellidomaterno.setText(self.db_data[row][2])
        #self.ui.line_descripcion.setText(self.db_data[row][3])
        #self.ui.line_sucursal.setEditText(self.db_data[row][4])
        #self.ui.line_direccion.setText(self.db_data[row][5])
        #self.ui.line_correo.setText(self.db_data[row][6])
