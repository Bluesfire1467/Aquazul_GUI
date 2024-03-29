# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Estado.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import GUI.Mainmenu.Pantallas.recursos_rc

class Ui_EstadoScreen(object):
    def setupUi(self, EstadoScreen):
        EstadoScreen.setObjectName("EstadoScreen")
        EstadoScreen.resize(600, 450)
        EstadoScreen.setMinimumSize(QtCore.QSize(600, 450))
        EstadoScreen.setMaximumSize(QtCore.QSize(600, 450))
        EstadoScreen.setStyleSheet("border: 2px solid #3498db;\n"
"border-radius: 10px;\n"
"\n"
"background-color: #eaf2ff;")
        self.centralwidget = QtWidgets.QWidget(EstadoScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setMinimumSize(QtCore.QSize(580, 100))
        self.groupBox.setMaximumSize(QtCore.QSize(551, 100))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("background-color:#eaf2ff;")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 40, 131, 21))
        self.label.setStyleSheet("background-color: #eaf2ff;\n"
"border: 2px solid #3498db;\n"
"border-radius: 8px;\n"
"color: #333333;\n"
"font-size: 11px;\n"
"font-weight: bold;\n"
"text-align: center;")
        self.label.setObjectName("label")
        self.line_estado = QtWidgets.QLineEdit(self.groupBox)
        self.line_estado.setGeometry(QtCore.QRect(150, 40, 121, 20))
        self.line_estado.setObjectName("line_estado")
        self.btn_agregar = QtWidgets.QPushButton(self.groupBox)
        self.btn_agregar.setGeometry(QtCore.QRect(330, 20, 60, 60))
        self.btn_agregar.setMinimumSize(QtCore.QSize(55, 55))
        self.btn_agregar.setMaximumSize(QtCore.QSize(60, 60))
        self.btn_agregar.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.btn_agregar.setStyleSheet("QPushButton{\n"
"background-color: #eaf2ff;\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: white;\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.btn_agregar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Images/Botones_Interfaz/agregar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_agregar.setIcon(icon)
        self.btn_agregar.setIconSize(QtCore.QSize(50, 50))
        self.btn_agregar.setObjectName("btn_agregar")
        self.btn_borrar = QtWidgets.QPushButton(self.groupBox)
        self.btn_borrar.setGeometry(QtCore.QRect(490, 20, 60, 60))
        self.btn_borrar.setMinimumSize(QtCore.QSize(55, 55))
        self.btn_borrar.setMaximumSize(QtCore.QSize(60, 60))
        self.btn_borrar.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.btn_borrar.setStyleSheet("QPushButton{\n"
"background-color: #eaf2ff;\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: white;\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.btn_borrar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Images/Botones_Interfaz/borrar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_borrar.setIcon(icon1)
        self.btn_borrar.setIconSize(QtCore.QSize(50, 50))
        self.btn_borrar.setObjectName("btn_borrar")
        self.btn_editar = QtWidgets.QPushButton(self.groupBox)
        self.btn_editar.setGeometry(QtCore.QRect(410, 20, 60, 60))
        self.btn_editar.setMinimumSize(QtCore.QSize(55, 55))
        self.btn_editar.setMaximumSize(QtCore.QSize(60, 60))
        self.btn_editar.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.btn_editar.setStyleSheet("QPushButton{\n"
"background-color: #eaf2ff;\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: white;\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.btn_editar.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Images/Botones_Interfaz/editar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_editar.setIcon(icon2)
        self.btn_editar.setIconSize(QtCore.QSize(50, 50))
        self.btn_editar.setObjectName("btn_editar")
        self.verticalLayout.addWidget(self.groupBox)
        self.table_estado = QtWidgets.QTableWidget(self.centralwidget)
        self.table_estado.setMinimumSize(QtCore.QSize(580, 0))
        self.table_estado.setMaximumSize(QtCore.QSize(580, 16777215))
        self.table_estado.setObjectName("table_estado")
        self.table_estado.setColumnCount(0)
        self.table_estado.setRowCount(0)
        self.verticalLayout.addWidget(self.table_estado)
        EstadoScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(EstadoScreen)
        QtCore.QMetaObject.connectSlotsByName(EstadoScreen)

    def retranslateUi(self, EstadoScreen):
        _translate = QtCore.QCoreApplication.translate
        EstadoScreen.setWindowTitle(_translate("EstadoScreen", "Estado"))
        self.groupBox.setTitle(_translate("EstadoScreen", "Estado"))
        self.label.setText(_translate("EstadoScreen", "Estado"))

