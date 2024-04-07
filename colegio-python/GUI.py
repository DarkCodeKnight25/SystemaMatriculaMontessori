from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(681, 400)
        Form.setMinimumSize(QtCore.QSize(681, 400))
        Form.setStyleSheet("background-color: rgb(0, 0, 255);")
        self.pantalla = QtWidgets.QTabWidget(Form)
        self.pantalla.setGeometry(QtCore.QRect(0, 0, 681, 400))
        self.pantalla.setMinimumSize(QtCore.QSize(681, 400))
        self.pantalla.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.pantalla.setObjectName("pantalla")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.bt_refrescar = QtWidgets.QPushButton(self.tab_5)
        self.bt_refrescar.setGeometry(QtCore.QRect(550, 320, 75, 23))
        self.bt_refrescar.setStyleSheet("background-color: rgb(85, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.bt_refrescar.setObjectName("bt_refrescar")
        self.tabla_productos = QtWidgets.QTableWidget(self.tab_5)
        self.tabla_productos.setGeometry(QtCore.QRect(30, 60, 511, 281))
        self.tabla_productos.setRowCount(0)
        self.tabla_productos.setColumnCount(5)
        self.tabla_productos.setObjectName("tabla_productos")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 0, 191))
        self.tabla_productos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(85, 255, 127))
        self.tabla_productos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 248, 53))
        self.tabla_productos.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(0, 170, 127))
        self.tabla_productos.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 170, 0))
        self.tabla_productos.setHorizontalHeaderItem(4, item)
        self.pantalla.addTab(self.tab_5, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.bt_buscar = QtWidgets.QPushButton(self.tab)
        self.bt_buscar.setGeometry(QtCore.QRect(550, 330, 75, 23))
        self.bt_buscar.setStyleSheet("background-color: rgb(85, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.bt_buscar.setObjectName("bt_buscar")
        self.codigoB = QtWidgets.QLineEdit(self.tab)
        self.codigoB.setGeometry(QtCore.QRect(72, 51, 101, 20))
        self.codigoB.setText("")
        self.codigoB.setObjectName("codigoB")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(21, 51, 45, 16))
        self.label.setObjectName("label")
        self.tabla_buscar = QtWidgets.QTableWidget(self.tab)
        self.tabla_buscar.setGeometry(QtCore.QRect(30, 90, 511, 261))
        self.tabla_buscar.setRowCount(0)
        self.tabla_buscar.setColumnCount(5)
        self.tabla_buscar.setObjectName("tabla_buscar")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 0, 191))
        self.tabla_buscar.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(85, 255, 127))
        self.tabla_buscar.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 248, 53))
        self.tabla_buscar.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(0, 170, 127))
        self.tabla_buscar.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 170, 0))
        self.tabla_buscar.setHorizontalHeaderItem(4, item)
        self.pantalla.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.bt_agregar = QtWidgets.QPushButton(self.tab_2)
        self.bt_agregar.setGeometry(QtCore.QRect(420, 260, 75, 23))
        self.bt_agregar.setStyleSheet("background-color: rgb(85, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.bt_agregar.setObjectName("bt_agregar")
        self.layoutWidget = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget.setGeometry(QtCore.QRect(170, 70, 231, 211))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.codigoA = QtWidgets.QLineEdit(self.layoutWidget)
        self.codigoA.setObjectName("codigoA")
        self.verticalLayout.addWidget(self.codigoA)
        self.nombreA = QtWidgets.QLineEdit(self.layoutWidget)
        self.nombreA.setObjectName("nombreA")
        self.verticalLayout.addWidget(self.nombreA)
        self.modeloA = QtWidgets.QLineEdit(self.layoutWidget)
        self.modeloA.setObjectName("modeloA")
        self.verticalLayout.addWidget(self.modeloA)
        self.precioA = QtWidgets.QLineEdit(self.layoutWidget)
        self.precioA.setObjectName("precioA")
        self.verticalLayout.addWidget(self.precioA)
        self.cantidadA = QtWidgets.QLineEdit(self.layoutWidget)
        self.cantidadA.setObjectName("cantidadA")
        self.verticalLayout.addWidget(self.cantidadA)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.pantalla.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.bt_actualizar = QtWidgets.QPushButton(self.tab_3)
        self.bt_actualizar.setGeometry(QtCore.QRect(530, 280, 91, 21))
        self.bt_actualizar.setStyleSheet("background-color: rgb(85, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.bt_actualizar.setObjectName("bt_actualizar")
        self.layoutWidget1 = QtWidgets.QWidget(self.tab_3)
        self.layoutWidget1.setGeometry(QtCore.QRect(270, 80, 251, 221))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_4.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_4.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_4.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_4.addWidget(self.label_11)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.codigo_actualizar = QtWidgets.QLineEdit(self.layoutWidget1)
        self.codigo_actualizar.setObjectName("codigo_actualizar")
        self.verticalLayout_3.addWidget(self.codigo_actualizar)
        self.nombre_actualizar = QtWidgets.QLineEdit(self.layoutWidget1)
        self.nombre_actualizar.setObjectName("nombre_actualizar")
        self.verticalLayout_3.addWidget(self.nombre_actualizar)
        self.modelo_actualizar = QtWidgets.QLineEdit(self.layoutWidget1)
        self.modelo_actualizar.setObjectName("modelo_actualizar")
        self.verticalLayout_3.addWidget(self.modelo_actualizar)
        self.precio_actualizar = QtWidgets.QLineEdit(self.layoutWidget1)
        self.precio_actualizar.setObjectName("precio_actualizar")
        self.verticalLayout_3.addWidget(self.precio_actualizar)
        self.cantidad_actualizar = QtWidgets.QLineEdit(self.layoutWidget1)
        self.cantidad_actualizar.setObjectName("cantidad_actualizar")
        self.verticalLayout_3.addWidget(self.cantidad_actualizar)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.id_producto = QtWidgets.QLineEdit(self.tab_3)
        self.id_producto.setGeometry(QtCore.QRect(30, 120, 180, 20))
        self.id_producto.setObjectName("id_producto")
        self.label_13 = QtWidgets.QLabel(self.tab_3)
        self.label_13.setGeometry(QtCore.QRect(40, 80, 191, 39))
        self.label_13.setObjectName("label_13")
        self.id_buscar = QtWidgets.QPushButton(self.tab_3)
        self.id_buscar.setGeometry(QtCore.QRect(70, 150, 75, 23))
        self.id_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.id_buscar.setObjectName("id_buscar")
        self.pantalla.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.codigo_borrar = QtWidgets.QLineEdit(self.tab_4)
        self.codigo_borrar.setGeometry(QtCore.QRect(91, 50, 101, 20))
        self.codigo_borrar.setText("")
        self.codigo_borrar.setObjectName("codigo_borrar")
        self.label_12 = QtWidgets.QLabel(self.tab_4)
        self.label_12.setGeometry(QtCore.QRect(40, 50, 45, 16))
        self.label_12.setObjectName("label_12")
        self.borrar_ok = QtWidgets.QPushButton(self.tab_4)
        self.borrar_ok.setGeometry(QtCore.QRect(200, 50, 91, 23))
        self.borrar_ok.setStyleSheet("background-color: rgb(255, 0, 127);")
        self.borrar_ok.setObjectName("borrar_ok")
        self.bt_borrar = QtWidgets.QPushButton(self.tab_4)
        self.bt_borrar.setGeometry(QtCore.QRect(560, 290, 75, 23))
        self.bt_borrar.setStyleSheet("background-color: rgb(85, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.bt_borrar.setObjectName("bt_borrar")
        self.tabla_borrar = QtWidgets.QTableWidget(self.tab_4)
        self.tabla_borrar.setGeometry(QtCore.QRect(30, 80, 511, 231))
        self.tabla_borrar.setRowCount(0)
        self.tabla_borrar.setColumnCount(5)
        self.tabla_borrar.setObjectName("tabla_borrar")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 0, 191))
        self.tabla_borrar.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(85, 255, 127))
        self.tabla_borrar.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 248, 53))
        self.tabla_borrar.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(0, 170, 127))
        self.tabla_borrar.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 170, 0))
        self.tabla_borrar.setHorizontalHeaderItem(4, item)
        self.pantalla.addTab(self.tab_4, "")

        self.retranslateUi(Form)
        self.pantalla.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "REGISTRO DE ESTUDIANTES"))
        self.bt_refrescar.setText(_translate("Form", "REFRESCAR"))
        item = self.tabla_productos.horizontalHeaderItem(0)
        item.setText(_translate("Form", "DNI"))
        item = self.tabla_productos.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Nombre"))
        item = self.tabla_productos.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Apellidos"))
        item = self.tabla_productos.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Sexo"))
        item = self.tabla_productos.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Fecha de nacimiento"))
        self.pantalla.setTabText(self.pantalla.indexOf(self.tab_5), _translate("Form", "ESTUDIANTES"))
        self.bt_buscar.setText(_translate("Form", "BUSCAR"))
        self.label.setText(_translate("Form", "CODIGO:"))
        item = self.tabla_buscar.horizontalHeaderItem(0)
        item.setText(_translate("Form", "DNI"))
        item = self.tabla_buscar.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Nombres"))
        item = self.tabla_buscar.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Apellidos"))
        item = self.tabla_buscar.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Sexo"))
        item = self.tabla_buscar.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Fecha de nacimiento"))
        self.pantalla.setTabText(self.pantalla.indexOf(self.tab), _translate("Form", "BUSCAR  ESTUDIANTE"))
        self.bt_agregar.setText(_translate("Form", "AGREGAR"))
        self.label_2.setText(_translate("Form", "DNI:"))
        self.label_3.setText(_translate("Form", "Nombres:"))
        self.label_4.setText(_translate("Form", "Apellidos:"))
        self.label_5.setText(_translate("Form", "Sexo: "))
        self.label_6.setText(_translate("Form", "Fecha de nacimiento: "))
        self.pantalla.setTabText(self.pantalla.indexOf(self.tab_2), _translate("Form", "NUEVO ESTUDIANTE"))
        self.bt_actualizar.setText(_translate("Form", "ACTUALIZAR"))
        self.label_7.setText(_translate("Form", "DNI:"))
        self.label_8.setText(_translate("Form", "Nombres:"))
        self.label_9.setText(_translate("Form", "Apellidos:"))
        self.label_10.setText(_translate("Form", "Sexo: "))
        self.label_11.setText(_translate("Form", "Fecha de nacimiento: "))
        self.label_13.setText(_translate("Form", "INGRESE EL DNI DEL ESTUDIANTE"))
        self.id_buscar.setText(_translate("Form", "BUSCAR"))
        self.pantalla.setTabText(self.pantalla.indexOf(self.tab_3), _translate("Form", "ACTUALIZAR ESTUDIANTE"))
        self.label_12.setText(_translate("Form", "DNI:"))
        self.borrar_ok.setText(_translate("Form", "OK"))
        self.bt_borrar.setText(_translate("Form", "BORRAR"))
        item = self.tabla_borrar.horizontalHeaderItem(0)
        item.setText(_translate("Form", "DNI"))
        item = self.tabla_borrar.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Nombres"))
        item = self.tabla_borrar.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Apellidos"))
        item = self.tabla_borrar.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Sexo"))
        item = self.tabla_borrar.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Fecha de nacimiento"))
        self.pantalla.setTabText(self.pantalla.indexOf(self.tab_4), _translate("Form", "ELIMINAR ESTUDIANTE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

