from GUI.Mainmenu.Pantallas.Habitat.Ui_HabitatScreen import Ui_HabitatScreen
from PyQt5.QtWidgets import QMainWindow
from Oracle.Connection_Oracle import Connection_Oracle
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import *
import sys

class Habitat(QMainWindow):
    closed = pyqtSignal()

    def __init__(self, conn):
        super().__init__()
        self.ui = Ui_HabitatScreen()
        self.ui.setupUi(self)
        self.id_inter = None
        self.conn = conn

        #Evento click tabla
        self.ui.table_habitat.cellClicked.connect(self.cell_to_line)

        #Evento Agregar tabla
        self.ui.btn_agregar.clicked.connect(self.addHabitat)

        #Evento Borrar Habi
        self.ui.btn_borrar.clicked.connect(self.deleteHabitat)

    def showEvent(self, event):
        super().showEvent(event)
        # Mostrar tabla
        self.refreshTable()
        self.refreshCombos()

    def closeEvent(self, event):
        self.closed.emit()
        event.accept()

    def refreshTable(self):
        self.conn.q_open()

        consulta = str("SELECT * FROM habitat")
        Habi = self.conn.query_execution(consulta)

        f = len(Habi)  # No. filas
        c = len(Habi[0])  # No. columnas

        self.ui.table_habitat.setRowCount(f)
        self.ui.table_habitat.setColumnCount(c)
        self.ui.table_habitat.setHorizontalHeaderLabels(['Numero', 'Nombre Habitat', 'Ancho', 'Largo', 'Alto', 'Descripcion', 'Temperatura', 'PH Agua', 'Tipo Agua', 'Id Material'])
        self.ui.table_habitat.verticalHeader().setVisible(False)

        for i in range(f):
            for j in range(c):
                self.ui.table_habitat.setItem(i, j, QTableWidgetItem(str(Habi[i][j])))
                #print(Animals[i][j])

        self.ui.table_habitat.show()
        self.conn.close()

    def deleteHabitat(self):
        self.conn.q_open()
        consulta = f"DELETE FROM habitat WHERE id_habitat = {int(self.id_inter[0])}"
        self.conn.query_insert(consulta)
        self.conn.close()

        self.refreshTable()
        self.restablecer()

    def addHabitat(self):
        self.conn.q_open()

        Nombre_Habi = str(self.ui.line_nombrehabi.text())
        Ancho = int(self.ui.line_ancho.text())
        Largo = int(self.ui.line_largo.text())
        Alto = int(self.ui.line_alto.text())
        print("llegue")
        descripcion = str(self.ui.line_descripcion.text())
        temperatura = float(self.ui.line_temperatura.text())
        print("llegue")
        Ph = float(self.ui.line_ph.text())
        print("Ph", Ph)

        # Te dan texto al que pertenece el ID
        Id_Tipo_Agua = str(self.ui.comboBox_TipoAgua.currentText())
        Id_Material = str(self.ui.comboBox_Material.currentText())

        print(Id_Tipo_Agua, Id_Material)

        buscar = str(f"""SELECT id_tipo_de_agua FROM tipo_agua WHERE tipo_de_agua = '{Id_Tipo_Agua}'""")
        Id_Tipo_Agua = (self.conn.query_execution(buscar))
        Id_Tipo_Agua = Id_Tipo_Agua[0][0]
        print(Id_Tipo_Agua)

        buscar = str(f"""SELECT id_material FROM material WHERE nombre_material = '{Id_Material}'""")
        Id_Material = (self.conn.query_execution(buscar))
        Id_Material = Id_Material[0][0]
        print(Id_Material)

        consulta = "INSERT INTO habitat (id_habitat, nombre_habitat, ancho, largo, alto, descripcion, temperaturatura, ph_agua, id_tipo_de_agua, id_material) values ((select max(id_habitat) from habitat)+1, :Nombre, :ancho, :largo, :alto, :descr, :Temp, :ph, :id_tipo, :material)"
        self.conn.query_update(consulta,(Nombre_Habi,Ancho,Largo,Alto,descripcion,temperatura,Ph,Id_Tipo_Agua,Id_Material))

        self.conn.close()
        self.restablecer()
        #self.refreshTable()


    def refreshCombos(self):
        self.conn.q_open()

        tipoMaterial = "SELECT nombre_material FROM material"
        tipoMaterial = self.conn.query_execution(tipoMaterial)
        tipoMaterial = get_values(tipoMaterial)

        tipoAgua = "SELECT tipo_de_agua from tipo_agua"
        tipoAgua = self.conn.query_execution(tipoAgua)
        tipoAgua = get_values(tipoAgua)

        self.ui.comboBox_Material.addItems(tipoMaterial)
        self.ui.comboBox_TipoAgua.addItems(tipoAgua)

        self.ui.comboBox_Material.show()
        self.ui.comboBox_TipoAgua.show()

        self.conn.close()

    def cell_to_line(self, row, column):
        self.conn.q_open()

        #print(row, column)
        listcell = []
        for i in range(10):
            listcell.append(self.ui.table_habitat.item(row,i).text())

        print(listcell)
        self.id_inter = listcell

        self.ui.line_nombrehabi.setText(listcell[1])
        self.ui.line_ancho.setText(listcell[2])
        self.ui.line_largo.setText(listcell[3])
        self.ui.line_alto.setText(listcell[4])
        self.ui.line_descripcion.setText(listcell[5])
        self.ui.line_temperatura.setText(listcell[6])
        self.ui.line_ph.setText(listcell[7])
        Id_tipoAgua = int(listcell[8])
        Id_Material = int(listcell[9])

        buscar = str(f"""SELECT tipo_de_agua FROM tipo_agua WHERE id_tipo_de_Agua = '{Id_tipoAgua}'""")
        Id_tipoAgua = (self.conn.query_execution(buscar))
        Id_tipoAgua = Id_tipoAgua[0][0]

        buscar = str(f"""SELECT nombre_material FROM material WHERE id_material = '{Id_Material}'""")
        Id_Material = (self.conn.query_execution(buscar))
        Id_Material = Id_Material[0][0]

        self.ui.comboBox_Material.setCurrentText(Id_Material)
        self.ui.comboBox_TipoAgua.setCurrentText(Id_tipoAgua)

        self.conn.close()

    def restablecer(self):
        self.ui.line_alto.setText("")
        self.ui.line_ancho.setText("")
        self.ui.line_largo.setText("")
        self.ui.line_nombrehabi.setText("")
        self.ui.line_descripcion.setText("")
        self.ui.line_temperatura.setText("")
        self.ui.line_ph.setText("")
        self.ui.comboBox_Material.currentIndex(1)
        self.ui.comboBox_TipoAgua.currentText(1)
def get_values(data):
    values = [item[0] for item in data]
    return values

