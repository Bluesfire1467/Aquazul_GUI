from GUI.Mainmenu.Pantallas.State.Ui_EstadoScreen import Ui_EstadoScreen
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from PyQt5.QtCore import pyqtSignal
from GUI.PopUpWindow.PopUpWindow import ok_information_window


class State(QMainWindow):
    closed = pyqtSignal()

    def __init__(self, conn):
        super().__init__()
        self.ui = Ui_EstadoScreen()
        self.ui.setupUi(self)
        self.ui.id_inter = None
        self.conn = conn

        # Agregar estado
        self.ui.btn_agregar.clicked.connect(self.agregarEstado)

        # Eliminar estado
        self.ui.btn_borrar.clicked.connect(self.eliminarEstado)

        # Editar
        self.ui.btn_editar.clicked.connect(self.editTable)

        # Evento click en la tabla
        self.ui.table_estado.cellClicked.connect(self.cell_to_line)

    def showEvent(self, event):
        super().showEvent(event)
        # Mostrar tabla Tipo de agua en la tabla
        # self.ui.btn_borrar.clicked.connect(self.show_table)
        self.refreshTable()

    def cell_to_line(self, row, column):
        item = self.ui.table_estado.item(row, column)
        listcell = []
        for i in range(2):
            listcell.append(self.ui.table_estado.item(row, i).text())

        print(listcell)
        self.id_inter = listcell

        NewRegist = str(item.text())
        self.ui.line_estado.setText(NewRegist)

    def agregarEstado(self):
        self.conn.q_open()

        regist = str(self.ui.line_estado.text())

        if len(regist) == 0:
            ok_information_window("Ingresa el estado!!", "ayuda")
            return

        consulta = str(
            f"""insert into estado (id_estado, nombre_estado) values ((select max(estado.id_estado)from estado)+1,'{regist}')""")

        self.conn.query_insert(consulta)
        self.conn.close()
        self.refreshTable()

    def eliminarEstado(self):
        self.conn.q_open()

        regist = str(self.ui.line_estado.text())

        if len(regist) == 0:
            ok_information_window("Ingresa el estado!!", "ayuda")
            return

        buscar = str(f"""select id_estado from estado where nombre_estado = '{regist}'""")
        IDreg = (self.conn.query_execution(buscar))
        ID = IDreg[0][0]

        consulta = str(f"""delete from estado where id_estado = {ID}""")

        self.conn.query_insert(consulta)
        self.conn.close()
        self.ui.line_estado.setText("")
        self.refreshTable()

    def refreshTable(self):
        self.conn.q_open()

        consulta = str("SELECT * FROM estado")

        States = self.conn.query_execution(consulta)

        f = len(States)  # No. filas
        c = len(States[0])  # No. columnas

        self.ui.table_estado.setRowCount(f)
        self.ui.table_estado.setColumnCount(c)
        self.ui.table_estado.setHorizontalHeaderLabels(['ID', 'Estado'])
        self.ui.table_estado.verticalHeader().setVisible(False)

        self.print_table(f, c, States)
        self.ui.table_estado.show()
        self.conn.close()

    def editTable(self):
        self.conn.q_open()

        Estado = str(self.ui.line_estado.text())
        print("Estado: ",Estado)

        consulta = "UPDATE estado SET nombre_estado = :Estado WHERE id_estado = :id"
        self.conn.query_update(consulta, (Estado,int(self.id_inter[0])))

        # Limpia LineBox
        self.ui.line_estado.setText("")

        self.conn.close()
        self.refreshTable()

    def closeEvent(self, event):
        self.closed.emit()
        event.accept()

    def print_table(self, f, c, States):
        for i in range(f):
            for j in range(c):
                self.ui.table_estado.setItem(i, j, QTableWidgetItem(str(States[i][j])))
                #print(States[i][j])
