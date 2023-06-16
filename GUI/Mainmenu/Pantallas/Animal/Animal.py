from GUI.Mainmenu.Pantallas.Animal.Ui_AnimalScreen import Ui_AnimalScreen
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import pyqtSignal
from Oracle.Connection_Oracle import Connection_Oracle
from PyQt5.QtWidgets import *
from GUI.PopUpWindow.PopUpWindow import ok_information_window
import sys


class Animal(QMainWindow):
    closed = pyqtSignal()

    def __init__(self, conn):
        super().__init__()
        self.ui = Ui_AnimalScreen()
        self.ui.setupUi(self)
        self.conn = conn
        # BotonAgregar
        # self.ui.btn_agregar.clicked.connect(self.addAnimal)

        # Evento Click en la tabla
        self.ui.table_animal.cellClicked.connect(self.cell_to_line)

    def showEvent(self,event):
        super().showEvent(event)
        #Mostrar tabla
        self.refreshTable()
        self.refreshCombos()

    def closeEvent(self, event):
        self.closed.emit()
        event.accept()

    def refreshTable(self):
        self.conn.q_open()

        consulta = str("SELECT * FROM animal")
        Animals = self.conn.query_execution(consulta)

        f = len(Animals)  # No. filas
        c = len(Animals[0])  # No. columnas

        self.ui.table_animal.setRowCount(f)
        self.ui.table_animal.setColumnCount(c)
        self.ui.table_animal.setHorizontalHeaderLabels(['ID', 'Nombre Animal', 'Cantidad de Alimento', 'Condicion Especial', 'ID Alimentacion', 'ID PELIGRO', 'ID HABITAT', 'ID ESPECIE', 'ID SUCURSAL'])
        self.ui.table_animal.verticalHeader().setVisible(False)

        for i in range(f):
            for j in range(c):
                self.ui.table_animal.setItem(i, j, QTableWidgetItem(str(Animals[i][j])))
                #print(Animals[i][j])

        self.ui.table_animal.show()
        self.conn.close()
    
    def addAnimal(self):
        self.conn.q_open()

        Nombre_Animal = str(self.ui.line_nombre.text())
        Cantidad_Alimento = int(self.ui.line_cantAli.text())
        Condicion_Especial = str(self.ui.line_condicion.text())
        ID_ALIMENTACION = str(self.ui.comboBox_tipoalimentacion.currentText())
        ID_PELIGRO = str(self.ui.comboBox_peligro.currentText())
        ID_HABITAT = str(self.ui.comboBox_habitat.currentText())
        ID_ESPECIE = str(self.ui.comboBox_especie.currentText())
        ID_SUCURSAL = str(self.ui.comboBox_sucursal.currentText())

        if len(Nombre_Animal) == 0 and len(Cantidad_Alimento) == 0 and len(Condicion_Especial) == 0 and len(ID_ALIMENTACION) and len(ID_PELIGRO) and len(ID_HABITAT) and len(ID_ESPECIE) and len(ID_SUCURSAL) == 0 == 0:
            ok_information_window("Ingresa todos registros!!", "ayuda")
            return

        # TODO Consulta nombre => ID para las IDS
        consulta = "INSERT INTO animal (id_animal, nombre_animal, cantidad_de_alimento, condicion_especial, id_alimentacion, id_peligro, id_habitat, id_especie, id_sucursal) values ((select max(id_animal) from animal)+1, :Nombre_Animal, :Cantidad_alimento, :Condicion_Especial, :ID_alimentacion, :ID_peligro, :ID_habitat, :ID_especie, :ID_sucursal)"

        self.conn.query_update(consulta,(Nombre_Animal,Cantidad_Alimento,Condicion_Especial,ID_ALIMENTACION,ID_PELIGRO,ID_HABITAT,ID_ESPECIE,ID_SUCURSAL))
        self.conn.close()

        self.refreshTable()

    def refreshCombos(self):
        self.conn.q_open()

        sucursal = "SELECT NOMBRE_SUCURSAL FROM SUCURSAL"
        sucursal = self.conn.query_execution(sucursal)
        sucursal = get_values(sucursal)

        especie = "SELECT nombre_comun from especie"
        especie = self.conn.query_execution(especie)
        especie = get_values(especie)

        alimentacion = "SELECT alimentacion FROM alimentacion"
        alimentacion = self.conn.query_execution(alimentacion)
        alimentacion = get_values(alimentacion)

        peligro = "SELECT peligro from peligro"
        peligro = self.conn.query_execution(peligro)
        peligro = get_values(peligro)

        habitat = "SELECT nombre_habitat from habitat"
        habitat = self.conn.query_execution(habitat)
        habitat = get_values(habitat)



        self.ui.comboBox_sucursal.addItems(sucursal)
        self.ui.comboBox_especie.addItems(especie)
        self.ui.comboBox_tipoalimentacion.addItems(alimentacion)
        self.ui.comboBox_peligro.addItems(peligro)
        self.ui.comboBox_habitat.addItems(habitat)

        self.ui.comboBox_sucursal.show()
        self.ui.comboBox_especie.show()
        self.ui.comboBox_tipoalimentacion.show()
        self.ui.comboBox_peligro.show()
        self.ui.comboBox_habitat.show()

        self.conn.close()

    def cell_to_line(self, row, column):
        self.conn.q_open()

        print(row, column)
        listcell = []
        for i in range(9):
            listcell.append(self.ui.table_animal.item(row,i).text())

        print(listcell)
        self.ui.line_nombre.setText(listcell[1])
        self.ui.line_cantAli.setText(listcell[2])
        self.ui.line_condicion.setText(listcell[3])

        # extrayendo compos para que coincidan 
        #self.ui.comboBox_tipoalimentacion.setCurrentIndex(listcell[4])
        #self.ui.comboBox_peligro.setCurrentIndex(listcell[5])
        #self.ui.comboBox_habitat.setCurrentIndex(listcell[6])
        #self.ui.comboBox_especie.setCurrentIndex(listcell[7])
        #self.ui.comboBox_sucursal.setCurrentIndex((listcell[8]))

        self.conn.close()

def get_values(data):
    values = [item[0] for item in data]
    return values

print("Jalando")
app = QApplication(sys.argv)
conn = Connection_Oracle()
conn.open('Developer', 'PassDev')
log_in = Animal(conn)
log_in.show()
sys.exit(app.exec_())
