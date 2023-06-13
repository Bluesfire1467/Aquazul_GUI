from GUI.Mainmenu.Pantallas.TypeWater.Ui_TipoAguaScreen import Ui_TipoAguaScreen
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import pyqtSignal
import sys
from Oracle import Connection_Oracle as conn
from GUI.PopUpWindow.PopUpWindow import ok_information_window


class TypeofWater(QMainWindow):
    closed = pyqtSignal()

    #Acciones que pueden ser activadas por el usuario
    def __init__(self):
        super().__init__()
        self.ui = Ui_TipoAguaScreen()
        self.ui.setupUi(self)

        # Agregar registro "Tipo de agua"
        self.ui.btn_agregar.clicked.connect(self.agregarTypeWater)


        #Boton regrescar tabla
        self.ui.pushButton.clicked.connect(self.refreshtable)

    def closeEvent(self, event):
        self.closed.emit()
        event.accept()

    #Eventos
    def showEvent(self,event):
        super().showEvent(event)
        # Mostrar tabla Tipo de agua en la tabla
        #self.ui.btn_borrar.clicked.connect(self.show_table)
        coneccionTemp = conn.Connection_Oracle()
        coneccionTemp.open("developer", "PassDev")

        consulta = str("SELECT * FROM tipo_agua")

        typeWatertext = coneccionTemp.query_execution(consulta)

        f = len(typeWatertext)  # No. filas
        c = len(typeWatertext[0])  # No. columnas

        print(typeWatertext)

        self.ui.table_tipoagua.setRowCount(f)
        self.ui.table_tipoagua.setColumnCount(c)
        self.ui.table_tipoagua.setHorizontalHeaderLabels(['ID', 'Tipo de agua'])
        self.ui.table_tipoagua.verticalHeader().setVisible(False)

        for i in range(f):
            for j in range(c):
                self.ui.table_tipoagua.setItem(i, j, QTableWidgetItem(str(typeWatertext[i][j])))
                print(typeWatertext[i][j])
        self.ui.table_tipoagua.show()
        coneccionTemp.close()

    def agregarTypeWater(self):
        coneccionTemp = conn.Connection_Oracle()
        coneccionTemp.open("developer","PassDev")

        regist = self.ui.line_tipoagua.text()
        consulta = f"""insert into tipo_agua (tipo_agua.id_tipo_de_agua, tipo_agua.tipo_de_agua) values ((select max(tipo_agua.id_tipo_de_agua)from tipo_agua)+1,'{regist}')"""
        print(consulta)
        coneccionTemp.query_insert(consulta)
        coneccionTemp.close()

    def eliminarTypeWater(self):
        coneccionTemp = conn.Connection_Oracle()
        coneccionTemp.open("developer", "PassDev")

        regist = str(self.ui.line_tipoagua.text())

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

    def refreshtable(self):
        coneccionTemp = conn.Connection_Oracle()
        coneccionTemp.open("developer", "PassDev")

        consulta = str("SELECT * FROM TIPO_AGUA")

        typeWatertext = coneccionTemp.query_execution(consulta)

        f = len(typeWatertext)  # No. filas
        c = len(typeWatertext[0])  # No. columnas

        print(typeWatertext)

        self.ui.table_tipoagua.setRowCount(f)
        self.ui.table_tipoagua.setColumnCount(c)
        self.ui.table_tipoagua.setHorizontalHeaderLabels(['ID', 'Tipo de agua'])
        self.ui.table_tipoagua.verticalHeader().setVisible(False)

        for i in range(f):
            for j in range(c):
                self.ui.table_tipoagua.setItem(i, j, QTableWidgetItem(str(typeWatertext[i][j])))
                print(typeWatertext[i][j])
        self.ui.table_tipoagua.show()
        coneccionTemp.close()

    def closeEvent(self, event):
        self.closed.emit()
        event.accept()
