# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Especie.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import GUI.Mainmenu.Pantallas.recursos_rc


class Ui_EspecieScreen(object):
    def setupUi(self, EspecieScreen):
        EspecieScreen.setObjectName("EspecieScreen")
        EspecieScreen.resize(568, 600)
        EspecieScreen.setMinimumSize(QtCore.QSize(568, 600))
        EspecieScreen.setMaximumSize(QtCore.QSize(568, 600))
        EspecieScreen.setStyleSheet("border: 2px solid #3498db;\n"
"border-radius: 10px;\n"
"\n"
"background-color: #eaf2ff;")
        self.centralwidget = QtWidgets.QWidget(EspecieScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setMinimumSize(QtCore.QSize(550, 180))
        self.groupBox.setMaximumSize(QtCore.QSize(551, 180))
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
        self.label_2.setGeometry(QtCore.QRect(10, 70, 131, 21))
        self.label_2.setStyleSheet("background-color: #eaf2ff;\n"
"border: 2px solid #3498db;\n"
"border-radius: 8px;\n"
"color: #333333;\n"
"font-size: 10px;\n"
"font-weight: bold;\n"
"text-align: center;")
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setObjectName("label_2")
        self.line_nombreCientifico = QtWidgets.QLineEdit(self.groupBox)
        self.line_nombreCientifico.setGeometry(QtCore.QRect(150, 70, 121, 20))
        self.line_nombreCientifico.setObjectName("line_nombreCientifico")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 131, 21))
        self.label_3.setStyleSheet("background-color: #eaf2ff;\n"
"border: 2px solid #3498db;\n"
"border-radius: 8px;\n"
"color: #333333;\n"
"font-size: 10px;\n"
"font-weight: bold;\n"
"text-align: center;")
        self.label_3.setObjectName("label_3")
        self.line_descripcion = QtWidgets.QLineEdit(self.groupBox)
        self.line_descripcion.setGeometry(QtCore.QRect(150, 100, 121, 20))
        self.line_descripcion.setObjectName("line_descripcion")
        self.btn_agregar = QtWidgets.QPushButton(self.groupBox)
        self.btn_agregar.setGeometry(QtCore.QRect(310, 50, 60, 60))
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
        self.btn_editar = QtWidgets.QPushButton(self.groupBox)
        self.btn_editar.setGeometry(QtCore.QRect(380, 50, 60, 60))
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Images/Botones_Interfaz/editar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_editar.setIcon(icon1)
        self.btn_editar.setIconSize(QtCore.QSize(50, 50))
        self.btn_editar.setObjectName("btn_editar")
        self.btn_borrar = QtWidgets.QPushButton(self.groupBox)
        self.btn_borrar.setGeometry(QtCore.QRect(450, 50, 60, 60))
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
        self.table_especie = QtWidgets.QTableWidget(self.centralwidget)
        self.table_especie.setObjectName("table_especie")
        self.table_especie.setColumnCount(0)
        self.table_especie.setRowCount(0)
        self.verticalLayout.addWidget(self.table_especie)
        EspecieScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(EspecieScreen)
        QtCore.QMetaObject.connectSlotsByName(EspecieScreen)

    def retranslateUi(self, EspecieScreen):
        _translate = QtCore.QCoreApplication.translate
        EspecieScreen.setWindowTitle(_translate("EspecieScreen", "Especie"))
        self.groupBox.setTitle(_translate("EspecieScreen", "Especie"))
        self.label.setText(_translate("EspecieScreen", "Nombre:"))
        self.label_2.setText(_translate("EspecieScreen", "Nombre cientifico"))
        self.label_3.setText(_translate("EspecieScreen", "Descripcion"))
