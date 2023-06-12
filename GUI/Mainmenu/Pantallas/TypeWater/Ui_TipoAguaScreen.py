# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TipoAgua.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TipoAguaScreen(object):
    def setupUi(self, TipoAguaScreen):
        TipoAguaScreen.setObjectName("TipoAguaScreen")
        TipoAguaScreen.resize(568, 400)
        TipoAguaScreen.setMinimumSize(QtCore.QSize(568, 400))
        TipoAguaScreen.setMaximumSize(QtCore.QSize(568, 400))
        TipoAguaScreen.setStyleSheet("border: 2px solid #3498db;\n"
"border-radius: 10px;\n"
"\n"
"background-color: #eaf2ff;")
        self.centralwidget = QtWidgets.QWidget(TipoAguaScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setMinimumSize(QtCore.QSize(550, 100))
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
        self.line_tipoagua = QtWidgets.QLineEdit(self.groupBox)
        self.line_tipoagua.setGeometry(QtCore.QRect(150, 40, 121, 20))
        self.line_tipoagua.setObjectName("line_tipoagua")
        self.btn_agregar = QtWidgets.QPushButton(self.groupBox)
        self.btn_agregar.setGeometry(QtCore.QRect(310, 10, 60, 60))
        self.btn_agregar.setMinimumSize(QtCore.QSize(55, 55))
        self.btn_agregar.setMaximumSize(QtCore.QSize(60, 60))
        self.btn_agregar.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.btn_agregar.setStyleSheet("QPushButton{\n"
"background-color: white;\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: black;\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.btn_agregar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../Images/Botones Interfaz/agregar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_agregar.setIcon(icon)
        self.btn_agregar.setIconSize(QtCore.QSize(50, 50))
        self.btn_agregar.setObjectName("btn_agregar")
        self.btn_editar = QtWidgets.QPushButton(self.groupBox)
        self.btn_editar.setGeometry(QtCore.QRect(380, 10, 60, 60))
        self.btn_editar.setMinimumSize(QtCore.QSize(55, 55))
        self.btn_editar.setMaximumSize(QtCore.QSize(60, 60))
        self.btn_editar.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.btn_editar.setStyleSheet("QPushButton{\n"
"background-color: white;\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: black;\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.btn_editar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../Images/Botones Interfaz/editar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_editar.setIcon(icon1)
        self.btn_editar.setIconSize(QtCore.QSize(50, 50))
        self.btn_editar.setObjectName("btn_editar")
        self.btn_borrar = QtWidgets.QPushButton(self.groupBox)
        self.btn_borrar.setGeometry(QtCore.QRect(450, 10, 60, 60))
        self.btn_borrar.setMinimumSize(QtCore.QSize(55, 55))
        self.btn_borrar.setMaximumSize(QtCore.QSize(60, 60))
        self.btn_borrar.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.btn_borrar.setStyleSheet("QPushButton{\n"
"background-color: white;\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: black;\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.btn_borrar.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../../Images/Botones Interfaz/borrar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.table_tipoagua = QtWidgets.QTableWidget(self.groupBox_2)
        self.table_tipoagua.setObjectName("table_tipoagua")
        self.table_tipoagua.setColumnCount(0)
        self.table_tipoagua.setRowCount(0)
        self.horizontalLayout.addWidget(self.table_tipoagua)
        self.verticalLayout.addWidget(self.groupBox_2)
        TipoAguaScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(TipoAguaScreen)
        QtCore.QMetaObject.connectSlotsByName(TipoAguaScreen)

    def retranslateUi(self, TipoAguaScreen):
        _translate = QtCore.QCoreApplication.translate
        TipoAguaScreen.setWindowTitle(_translate("TipoAguaScreen", "Tipo de Agua"))
        self.groupBox.setTitle(_translate("TipoAguaScreen", "Tipo de Agua"))
        self.label.setText(_translate("TipoAguaScreen", "Tipo de agua"))
        self.groupBox_2.setTitle(_translate("TipoAguaScreen", "Mostrar"))
