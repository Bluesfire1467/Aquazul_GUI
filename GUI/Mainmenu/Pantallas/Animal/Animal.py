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
        self.id_inter = None

        # Boton Agregar
        self.ui.btn_agregar.clicked.connect(self.addAnimal)

        # Boton Eliminar
        self.ui.btn_borrar.clicked.connect(self.deleteAnimal)

        # Boton Editar
        self.ui.btn_editar.clicked.connect(self.editAnimal)

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
        self.ui.table_animal.setHorizontalHeaderLabels(['Numero', 'Nombre Animal', 'Cantidad de Alimento', 'Condicion Especial', 'ID Alimentacion', 'ID PELIGRO', 'ID HABITAT', 'ID ESPECIE', 'ID SUCURSAL'])
        self.ui.table_animal.verticalHeader().setVisible(False)

        for i in range(f):
            for j in range(c):
                self.ui.table_animal.setItem(i, j, QTableWidgetItem(str(Animals[i][j])))
                #print(Animals[i][j])

        self.ui.table_animal.show()
        self.conn.close()

    def restablecer(self):
        self.ui.line_nombre.setText("")
        self.ui.line_condicion.setText("")
        self.ui.line_cantAli.setText("")
        self.ui.comboBox_sucursal.setCurrentIndex(1)
        self.ui.comboBox_especie.setCurrentIndex(1)
        self.ui.comboBox_peligro.setCurrentIndex(1)
        self.ui.comboBox_habitat.setCurrentIndex(1)
        self.ui.comboBox_tipoalimentacion.setCurrentIndex(1)

    def addAnimal(self):
        self.conn.q_open()

        Nombre_Animal = str(self.ui.line_nombre.text())
        Cantidad_Alimento = int(self.ui.line_cantAli.text())
        Condicion_Especial = str(self.ui.line_condicion.text())

        # Te dan texto al que pertenece el ID
        ID_ALIMENTACION = str(self.ui.comboBox_tipoalimentacion.currentText())
        ID_PELIGRO = str(self.ui.comboBox_peligro.currentText())
        ID_HABITAT = str(self.ui.comboBox_habitat.currentText())
        ID_ESPECIE = str(self.ui.comboBox_especie.currentText())
        ID_SUCURSAL = str(self.ui.comboBox_sucursal.currentText())
        print(ID_ALIMENTACION,ID_SUCURSAL,ID_ESPECIE,ID_HABITAT)

        buscar = str(f"""SELECT id_alimentacion FROM alimentacion WHERE alimentacion = '{ID_ALIMENTACION}'""")
        ID_ALIMENTACION = (self.conn.query_execution(buscar))
        ID_ALIMENTACION = ID_ALIMENTACION[0][0]

        buscar = str(f"""SELECT id_peligro FROM peligro WHERE peligro = '{ID_PELIGRO}'""")
        ID_PELIGRO = (self.conn.query_execution(buscar))
        ID_PELIGRO = ID_PELIGRO[0][0]

        buscar = str(f"""SELECT id_habitat FROM habitat WHERE nombre_habitat = '{ID_HABITAT}'""")
        ID_HABITAT = (self.conn.query_execution(buscar))
        ID_HABITAT = ID_HABITAT[0][0]

        buscar = str(f"""SELECT id_especie FROM especie WHERE nombre_comun = '{ID_ESPECIE}'""")
        ID_ESPECIE = (self.conn.query_execution(buscar))
        ID_ESPECIE = ID_ESPECIE[0][0]

        buscar = str(f"""SELECT id_sucursal FROM sucursal WHERE nombre_sucursal = '{ID_SUCURSAL}'""")
        ID_SUCURSAL = (self.conn.query_execution(buscar))
        ID_SUCURSAL = ID_SUCURSAL[0][0]

        if len(Nombre_Animal) == 0 and len(Cantidad_Alimento) == 0 and len(Condicion_Especial) == 0 and len(ID_ALIMENTACION) and len(ID_PELIGRO) and len(ID_HABITAT) and len(ID_ESPECIE) and len(ID_SUCURSAL) == 0 == 0:
            ok_information_window("Ingresa todos registros!!", "ayuda")
            return

        consulta = "INSERT INTO animal (id_animal, nombre_animal, cantidad_de_alimento, condicion_especial, id_alimentacion, id_peligro, id_habitat, id_especie, id_sucursal) values ((select max(id_animal) from animal)+1, :Nombre_Animal, :Cantidad_alimento, :Condicion_Especial, :ID_alimentacion, :ID_peligro, :ID_habitat, :ID_especie, :ID_sucursal)"

        self.conn.query_update(consulta,(Nombre_Animal,Cantidad_Alimento,Condicion_Especial,ID_ALIMENTACION,ID_PELIGRO,ID_HABITAT,ID_ESPECIE,ID_SUCURSAL))
        self.conn.close()
        self.restablecer()
        self.refreshTable()

    def deleteAnimal(self):
        self.conn.q_open()

        consulta = f"DELETE FROM animal WHERE id_animal = {int(self.id_inter[0])}"
        self.conn.query_insert(consulta)
        self.conn.close()

        self.refreshTable()
        self.restablecer()

    def editAnimal(self):
        self.conn.q_open()
        Nombre_Animal = str(self.ui.line_nombre.text())
        Cantidad_Alimento = int(self.ui.line_cantAli.text())
        Condicion_Especial = str(self.ui.line_condicion.text())

        # Te dan texto al que pertenece el ID
        ID_ALIMENTACION = str(self.ui.comboBox_tipoalimentacion.currentText())
        ID_PELIGRO = str(self.ui.comboBox_peligro.currentText())
        ID_HABITAT = str(self.ui.comboBox_habitat.currentText())
        ID_ESPECIE = str(self.ui.comboBox_especie.currentText())
        ID_SUCURSAL = str(self.ui.comboBox_sucursal.currentText())
        print(ID_ALIMENTACION, ID_SUCURSAL, ID_ESPECIE, ID_HABITAT)

        buscar = str(f"""SELECT id_alimentacion FROM alimentacion WHERE alimentacion = '{ID_ALIMENTACION}'""")
        ID_ALIMENTACION = (self.conn.query_execution(buscar))
        ID_ALIMENTACION = ID_ALIMENTACION[0][0]

        buscar = str(f"""SELECT id_peligro FROM peligro WHERE peligro = '{ID_PELIGRO}'""")
        ID_PELIGRO = (self.conn.query_execution(buscar))
        ID_PELIGRO = ID_PELIGRO[0][0]

        buscar = str(f"""SELECT id_habitat FROM habitat WHERE nombre_habitat = '{ID_HABITAT}'""")
        ID_HABITAT = (self.conn.query_execution(buscar))
        ID_HABITAT = ID_HABITAT[0][0]

        buscar = str(f"""SELECT id_especie FROM especie WHERE nombre_comun = '{ID_ESPECIE}'""")
        ID_ESPECIE = (self.conn.query_execution(buscar))
        ID_ESPECIE = ID_ESPECIE[0][0]

        buscar = str(f"""SELECT id_sucursal FROM sucursal WHERE nombre_sucursal = '{ID_SUCURSAL}'""")
        ID_SUCURSAL = (self.conn.query_execution(buscar))
        ID_SUCURSAL = ID_SUCURSAL[0][0]

        consulta = "UPDATE animal SET nombre_animal = :NombreAnimal, cantidad_de_alimento = :Cantidad_Alimento, condicion_especial = :Condicion_especial, id_alimentacion = :id_ali, id_peligro = :peligro, id_habitat = :habi, id_especie = :especie, id_sucursal = :suc WHERE id_animal = :id"

        self.conn.query_update(consulta, (Nombre_Animal, Cantidad_Alimento, Condicion_Especial, ID_ALIMENTACION, ID_PELIGRO, ID_HABITAT, ID_ESPECIE,ID_SUCURSAL,self.id_inter[0]))

        self.refreshTable()
        self.conn.close()
        self.restablecer()

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

        self.id_inter = listcell

        self.ui.line_nombre.setText(listcell[1])
        self.ui.line_cantAli.setText(listcell[2])
        self.ui.line_condicion.setText(listcell[3])

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

def get_values(data):
    values = [item[0] for item in data]
    return values
