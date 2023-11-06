from PyQt5.QtCore import pyqtSignal
from GUI.Mainmenu.Pantallas.Species.Ui_EspecieScreen import Ui_EspecieScreen
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import pyqtSignal
from Oracle.Connection_Oracle import Connection_Oracle
from PyQt5.QtWidgets import *
from GUI.PopUpWindow.PopUpWindow import ok_information_window
import sys

class Species(QMainWindow):
    closed = pyqtSignal()

    def __init__(self, conn):
        super().__init__()
        self.ui = Ui_EspecieScreen()
        self.ui.setupUi(self)
        self.id_inter = None
        self.conn = conn

        # Evento click en la tabla
        self.ui.table_especie.cellClicked.connect(self.cell_to_line)

        # Agregar Especie
        self.ui.btn_agregar.clicked.connect(self.addSpecie)

        # Editar Especie
        self.ui.btn_editar.clicked.connect(self.editSpecie)

        # Borrar Especie
        self.ui.btn_borrar.clicked.connect(self.deleteSpecie)

    def showEvent(self, event):
        super().showEvent(event)
        # Mostrar tabla
        self.refreshTable()
        #self.refreshCombos()

    def reset(self):
        self.ui.line_nombre.setText("")
        self.ui.line_descripcion.setText("")
        self.ui.line_nombreCientifico.setText("")

    def closeEvent(self, event):
        self.closed.emit()
        event.accept()

    def addSpecie(self):
        self.conn.q_open()

        Nombre = str(self.ui.line_nombre.text())
        NombreCientifico = str(self.ui.line_nombreCientifico.text())
        Descripcion = str(self.ui.line_descripcion.text())

        consulta = "INSERT INTO especie (id_especie, nombre_comun, nombre_cientifico, descripcion) values ((select max(id_especie) from especie)+1, :Nombre, :NombreCie, :Descripcion)"
        self.conn.query_update(consulta, (Nombre, NombreCientifico, Descripcion))
        self.conn.close()
        self.refreshTable()
        self.reset()

    def editSpecie(self):
        self.conn.q_open()
        Nombre = str(self.ui.line_nombre.text())
        NombreCientifico = str(self.ui.line_nombreCientifico.text())
        Descripcion = str(self.ui.line_descripcion.text())

        consulta = "UPDATE especie SET nombre_comun = :NombreEspecie, nombre_cientifico = :NombreCient, descripcion = :Descrip WHERE id_especie = :id"
        self.conn.query_update(consulta, (Nombre, NombreCientifico, Descripcion, self.id_inter[0]))

        self.refreshTable()
        self.reset()
        self.conn.close()

    def deleteSpecie(self):
        self.conn.q_open()

        consulta = f"DELETE FROM especie WHERE id_especie = {int(self.id_inter[0])}"
        self.conn.query_insert(consulta)
        self.conn.close()
        self.refreshTable()
        self.reset()

    def refreshTable(self):
        self.conn.q_open()

        consulta = str("SELECT * FROM especie")
        Speciess = self.conn.query_execution(consulta)

        f = len(Speciess)  # No. filas
        c = len(Speciess[0])  # No. columnas

        self.ui.table_especie.setRowCount(f)
        self.ui.table_especie.setColumnCount(c)
        self.ui.table_especie.setHorizontalHeaderLabels(['Numero', 'Nombre Comun', 'Nombre Cientifico', 'Descripcion'])
        self.ui.table_especie.verticalHeader().setVisible(False)

        for i in range(f):
            for j in range(c):
                self.ui.table_especie.setItem(i, j, QTableWidgetItem(str(Speciess[i][j])))
                #print(Animals[i][j])

        self.ui.table_especie.show()
        self.conn.close()

    def cell_to_line(self, row, column):
        self.conn.q_open()

        #print(row, column)
        listcell = []
        for i in range(4):
            listcell.append(self.ui.table_especie.item(row,i).text())

        self.id_inter = listcell
        self.ui.line_nombre.setText(listcell[1])
        self.ui.line_nombreCientifico.setText(listcell[2])
        self.ui.line_descripcion.setText(listcell[3])

        self.conn.close()

