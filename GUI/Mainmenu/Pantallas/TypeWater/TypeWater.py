from GUI.Mainmenu.Pantallas.TypeWater.Ui_TipoAguaScreen import Ui_TipoAguaScreen
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from PyQt5.QtCore import pyqtSignal
from GUI.PopUpWindow.PopUpWindow import ok_information_window


class TypeofWater(QMainWindow):
    closed = pyqtSignal()

    # Acciones que pueden ser activadas por el usuario
    def __init__(self, conn):
        super().__init__()

        self.ui = Ui_TipoAguaScreen()
        self.ui.setupUi(self)
        self.conn = conn

        # Agregar registro "Tipo de agua"
        self.ui.btn_agregar.clicked.connect(self.agregarTypeWater)

        # Eliminar registro
        self.ui.btn_borrar.clicked.connect(self.eliminarTypeWater)

        # Boton editar tabla
        self.ui.table_tipoagua.cellChanged.connect(self.edit_table)

    # Eventos
    def showEvent(self, event):
        super().showEvent(event)
        # Mostrar tabla Tipo de agua en la tabla
        # self.ui.btn_borrar.clicked.connect(self.show_table)
        self.refreshtable()
        # self.ui.table_tipoagua.cellClicked(self.edit_table)

    def agregarTypeWater(self):
        self.conn.open("developer", "PassDev")

        regist = str(self.ui.line_tipoagua.text())
        consulta = f"""insert into tipo_agua (tipo_agua.id_tipo_de_agua, tipo_agua.tipo_de_agua) values ((select max(tipo_agua.id_tipo_de_agua)from tipo_agua)+1,'{regist}')"""
        self.conn.query_insert(consulta)
        self.conn.close()

    def eliminarTypeWater(self):
        self.conn.open("developer", "PassDev")

        regist = str(self.ui.line_tipoagua.text())

        if len(regist) == 0:
            ok_information_window("Ingresa el estado!!", "ayuda")
            return

        buscar = str(f"""select id_tipo_de_agua from tipo_agua where tipo_de_agua = '{regist}'""")
        print(buscar)
        IDreg = (self.conn.query_execution(buscar))
        ID = IDreg[0][0]
        print(ID)
        consulta = str(f"""delete from tipo_agua where id_tipo_de_Agua = {ID}""")
        print(consulta)
        self.conn.query_insert(consulta)
        self.conn.close()

    def refreshtable(self):
        self.conn.open("developer", "PassDev")

        consulta = str("SELECT * FROM TIPO_AGUA")

        typeWatertext = self.conn.query_execution(consulta)

        f = len(typeWatertext)  # No. filas
        c = len(typeWatertext[0])  # No. columnas

        self.ui.table_tipoagua.setRowCount(f)
        self.ui.table_tipoagua.setColumnCount(c)
        self.ui.table_tipoagua.setHorizontalHeaderLabels(['ID', 'Tipo de agua'])
        self.ui.table_tipoagua.verticalHeader().setVisible(False)

        for i in range(f):
            for j in range(c):
                self.ui.table_tipoagua.setItem(i, j, QTableWidgetItem(str(typeWatertext[i][j])))
                # print(typeWatertext[i][j])
        self.ui.table_tipoagua.show()
        self.conn.close()

    def closeEvent(self, event):
        self.closed.emit()
        event.accept()

    def edit_table(self, row, column):

        try:
            # obtener tabla original
            self.conn.open("developer", "PassDev")
            consulta = str("SELECT * FROM TIPO_AGUA")
            typeWatertext = self.conn.query_execution(consulta)

            print("Celda cambiada:", row, column)
            item = self.ui.table_tipoagua.item(row, column)
            if item is None:
                return

            text = str(item.text())
            print("nuevo: ", text)

            registOld = str(typeWatertext[row][column])
            print("viejo: ", registOld)

            # Condicion cuando no hay cambios
            if text == registOld:
                self.ui.line_tipoagua.setText("")
                return

            # buscar ID
            buscar = str(f"""select id_tipo_de_agua from tipo_agua where tipo_de_agua = '{registOld}'""")
            print(buscar)
            IDreg = (self.conn.query_execution(buscar))
            ID = IDreg[0][0]
            print(ID)

            # hacer update f"""delete from tipo_agua where id_tipo_de_Agua = {ID}"""
            consulta = str(f"""UPDATE tipo_agua SET tipo_de_agua = 'ANODEPRRO' WHERE tipo_de_agua = 'Dulce'""")
            print(consulta)
            print(type(consulta))
            self.conn.query_insert(consulta)

            self.ui.line_tipoagua.setText("")
        except:
            print("Ni pedo No se pudo")
        finally:
            self.conn.close()
