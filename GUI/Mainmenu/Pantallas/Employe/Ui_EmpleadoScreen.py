# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Empleado.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import GUI.Mainmenu.Pantallas.recursos_rc

class Ui_EmpleadoScreen(object):
    def setupUi(self, EmpleadoScreen):
        EmpleadoScreen.setObjectName("EmpleadoScreen")
        EmpleadoScreen.resize(568, 600)
        EmpleadoScreen.setMinimumSize(QtCore.QSize(568, 600))
        EmpleadoScreen.setMaximumSize(QtCore.QSize(568, 600))
        EmpleadoScreen.setStyleSheet("border: 2px solid #3498db;\n"
"border-radius: 10px;\n"
"\n"
"background-color: #eaf2ff;")
        self.centralwidget = QtWidgets.QWidget(EmpleadoScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setMinimumSize(QtCore.QSize(550, 251))
        self.groupBox.setMaximumSize(QtCore.QSize(551, 251))
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
        self.line_nombre = QtWidgets.QLineEdit(self.groupBox)
        self.line_nombre.setGeometry(QtCore.QRect(150, 40, 121, 20))
        self.line_nombre.setObjectName("line_nombre")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 131, 21))
        self.label_2.setStyleSheet("background-color: #eaf2ff;\n"
"border: 2px solid #3498db;\n"
"border-radius: 8px;\n"
"color: #333333;\n"
"font-size: 10px;\n"
"font-weight: bold;\n"
"text-align: center;")
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setObjectName("label_2")
        self.line_apellidopaterno = QtWidgets.QLineEdit(self.groupBox)
        self.line_apellidopaterno.setGeometry(QtCore.QRect(150, 70, 121, 20))
        self.line_apellidopaterno.setObjectName("line_apellidopaterno")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 131, 21))
        self.label_3.setStyleSheet("background-color: #eaf2ff;\n"
"border: 2px solid #3498db;\n"
"border-radius: 8px;\n"
"color: #333333;\n"
"font-size: 10px;\n"
"font-weight: bold;\n"
"text-align: center;")
        self.label_3.setObjectName("label_3")
        self.line_apellidomaterno = QtWidgets.QLineEdit(self.groupBox)
        self.line_apellidomaterno.setGeometry(QtCore.QRect(150, 100, 121, 20))
        self.line_apellidomaterno.setObjectName("line_apellidomaterno")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 130, 131, 21))
        self.label_4.setStyleSheet("background-color: #eaf2ff;\n"
"border: 2px solid #3498db;\n"
"border-radius: 8px;\n"
"color: #333333;\n"
"font-size: 10px;\n"
"font-weight: bold;\n"
"text-align: center;")
        self.label_4.setObjectName("label_4")
        self.line_descripcion = QtWidgets.QLineEdit(self.groupBox)
        self.line_descripcion.setGeometry(QtCore.QRect(150, 130, 121, 20))
        self.line_descripcion.setObjectName("line_descripcion")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(290, 40, 81, 21))
        self.label_7.setStyleSheet("background-color: #eaf2ff;\n"
"border: 2px solid #3498db;\n"
"border-radius: 8px;\n"
"color: #333333;\n"
"font-size: 11px;\n"
"font-weight: bold;\n"
"text-align: center;")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(290, 70, 81, 21))
        self.label_8.setStyleSheet("background-color: #eaf2ff;\n"
"border: 2px solid #3498db;\n"
"border-radius: 8px;\n"
"color: #333333;\n"
"font-size: 11px;\n"
"font-weight: bold;\n"
"text-align: center;")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(290, 100, 81, 21))
        self.label_9.setStyleSheet("background-color: #eaf2ff;\n"
"border: 2px solid #3498db;\n"
"border-radius: 8px;\n"
"color: #333333;\n"
"font-size: 11px;\n"
"font-weight: bold;\n"
"text-align: center;")
        self.label_9.setObjectName("label_9")
        self.line_sucursal = QtWidgets.QComboBox(self.groupBox)
        self.line_sucursal.setGeometry(QtCore.QRect(390, 40, 121, 20))
        self.line_sucursal.setObjectName("line_sucursal")
        self.line_direccion = QtWidgets.QLineEdit(self.groupBox)
        self.line_direccion.setGeometry(QtCore.QRect(390, 70, 121, 20))
        self.line_direccion.setObjectName("line_direccion")
        self.line_correo = QtWidgets.QLineEdit(self.groupBox)
        self.line_correo.setGeometry(QtCore.QRect(390, 100, 121, 20))
        self.line_correo.setObjectName("line_correo")
        self.btn_editar = QtWidgets.QPushButton(self.groupBox)
        self.btn_editar.setGeometry(QtCore.QRect(380, 170, 60, 60))
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Images/Botones_Interfaz/editar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_editar.setIcon(icon)
        self.btn_editar.setIconSize(QtCore.QSize(50, 50))
        self.btn_editar.setObjectName("btn_editar")
        self.btn_agregar = QtWidgets.QPushButton(self.groupBox)
        self.btn_agregar.setGeometry(QtCore.QRect(310, 170, 60, 60))
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Images/Botones_Interfaz/agregar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_agregar.setIcon(icon1)
        self.btn_agregar.setIconSize(QtCore.QSize(50, 50))
        self.btn_agregar.setObjectName("btn_agregar")
        self.btn_borrar = QtWidgets.QPushButton(self.groupBox)
        self.btn_borrar.setGeometry(QtCore.QRect(450, 170, 60, 60))
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Images/Botones_Interfaz/borrar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_borrar.setIcon(icon2)
        self.btn_borrar.setIconSize(QtCore.QSize(50, 50))
        self.btn_borrar.setObjectName("btn_borrar")
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("background-color: #eaf2ff;\n"
"padding: 12px;\n"
"")
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setContentsMargins(-1, 20, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.table_empleado = QtWidgets.QTableWidget(self.groupBox_2)
        self.table_empleado.setObjectName("table_empleado")
        self.table_empleado.setColumnCount(0)
        self.table_empleado.setRowCount(0)
        self.horizontalLayout.addWidget(self.table_empleado)
        self.verticalLayout.addWidget(self.groupBox_2)
        EmpleadoScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(EmpleadoScreen)
        QtCore.QMetaObject.connectSlotsByName(EmpleadoScreen)

    def retranslateUi(self, EmpleadoScreen):
        _translate = QtCore.QCoreApplication.translate
        EmpleadoScreen.setWindowTitle(_translate("EmpleadoScreen", "Empleado"))
        self.groupBox.setTitle(_translate("EmpleadoScreen", "Empleado"))
        self.label.setText(_translate("EmpleadoScreen", "Nombre"))
        self.label_2.setText(_translate("EmpleadoScreen", "Apellido Materno"))
        self.label_3.setText(_translate("EmpleadoScreen", "Apellido Paterno"))
        self.label_4.setText(_translate("EmpleadoScreen", "Tipo de Empleado"))
        self.label_7.setText(_translate("EmpleadoScreen", "Sucursal"))
        self.label_8.setText(_translate("EmpleadoScreen", "Direccion"))
        self.label_9.setText(_translate("EmpleadoScreen", "Correo"))
        self.groupBox_2.setTitle(_translate("EmpleadoScreen", "Mostrar"))

