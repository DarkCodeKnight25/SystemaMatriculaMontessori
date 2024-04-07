import sys
from GUI import *
from conexionBD import*
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication 

class MiApp(QMainWindow):
	def __init__(self):
		super(MiApp, self).__init__()
		uic.loadUi('frmColegio.ui',self) 
	
		self.datosTotal = Registro_datos()

		self.bt_refrescar.clicked.connect(self.m_productos)
		self.bt_agregar.clicked.connect(self.insert_productos)
		self.bt_buscar.clicked.connect(self.buscar_producto)
		self.bt_borrar.clicked.connect(self.eliminar_producto)
		self.bt_actualizar.clicked.connect(self.modificar_productos)

		self.tabla_productos.setColumnWidth(0,98)
		self.tabla_productos.setColumnWidth(1,100)
		self.tabla_productos.setColumnWidth(2,98)
		self.tabla_productos.setColumnWidth(3,98)
		self.tabla_productos.setColumnWidth(4,98)

		self.tabla_borrar.setColumnWidth(0,98)
		self.tabla_borrar.setColumnWidth(1,100)
		self.tabla_borrar.setColumnWidth(2,98)
		self.tabla_borrar.setColumnWidth(3,98)
		self.tabla_borrar.setColumnWidth(4,98)

		self.tabla_buscar.setColumnWidth(0,98)
		self.tabla_buscar.setColumnWidth(1,100)
		self.tabla_buscar.setColumnWidth(2,98)
		self.tabla_buscar.setColumnWidth(3,98)
		self.tabla_buscar.setColumnWidth(4,98)

	def m_productos(self):	
		datos = self.datosTotal.buscar_productos()
		i = len(datos)

		self.tabla_productos.setRowCount(i)
		tablerow = 0
		for row in datos:
			self.tabla_productos.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[1]))
			self.tabla_productos.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[2]))
			self.tabla_productos.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[3]))
			self.tabla_productos.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[4]))
			self.tabla_productos.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[5]))
			self.tabla_productos.setItem(tablerow,5,QtWidgets.QTableWidgetItem(row[6]))
			self.tabla_productos.setItem(tablerow,6,QtWidgets.QTableWidgetItem(row[7]))
			tablerow +=1


	def insert_productos(self):
		codigo = self.codigoA.text() 
		nombre = self.nombreA.text()
		apellido_parterno = self.modeloA.text()
		apellido_materno = self.precioA.text()
		sexo = self.cantidadA.text()
		fecha_nacimiento = self.lneFechaNacimiento.text()
		direccion = self.lneDireccion.text()

		self.datosTotal.inserta_producto(codigo, nombre, apellido_parterno, apellido_materno, sexo, fecha_nacimiento, direccion)
		self.codigoA.clear()
		self.nombreA.clear()
		self.modeloA.clear()
		self.precioA.clear()
		self.cantidadA.clear()
		self.lneFechaNacimiento.clear()
		self.lneDireccion.clear()

	def modificar_productos(self):
		id_producto = self.id_producto.text() 
		id_producto = str("'" + id_producto + "'")
		nombreXX = self.datosTotal.busca_producto(id_producto)

		if nombreXX != None:

			self.id_buscar.setText("ACTUALIZAR")

			codigoM = self.codigo_actualizar.text() 
			nombreM = self.nombre_actualizar.text()
			modeloM = self.modelo_actualizar.text()
			precioM = self.precio_actualizar.text()
			cantidadM = self.cantidad_actualizar.text()
			fechaUpdate = self.lneFechaNacimiento_Update.text()
			direccionUpdate = self.lneDireccion_Update.text()


			act = self.datosTotal.actualiza_productos(codigoM,nombreM , modeloM, precioM, cantidadM, fechaUpdate, direccionUpdate)
			if act == 1:
				self.id_buscar.setText("ACTUALIZADO")				
				self.codigo_actualizar.clear()
				self.nombre_actualizar.clear()
				self.modelo_actualizar.clear()
				self.precio_actualizar.clear()
				self.cantidad_actualizar.clear()
				self.lneFechaNacimiento_Update.clear()
				self.lneDireccion_Update.clear()
	
				self.id_producto.clear()

			elif act == 0:
				self.id_buscar.setText("ERROR")
			else:
				self.id_buscar.setText("INCORRECTO")
			
		else:
			self.id_buscar.setText("NO EXISTE")


	def buscar_producto(self):
		nombre_producto = self.codigoB.text()
		nombre_producto = str("'" + nombre_producto + "'")

		datosB = self.datosTotal.busca_producto(nombre_producto)
		i = len(datosB)

		self.tabla_buscar.setRowCount(i)
		tablerow = 0
		for row in datosB:
			self.tabla_buscar.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[1]))
			self.tabla_buscar.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[2]))
			self.tabla_buscar.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[3]))
			self.tabla_buscar.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[4]))
			self.tabla_buscar.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[5]))
			self.tabla_buscar.setItem(tablerow,5,QtWidgets.QTableWidgetItem(row[6]))
			self.tabla_buscar.setItem(tablerow,6,QtWidgets.QTableWidgetItem(row[7]))
			tablerow +=1

	def eliminar_producto(self):
		eliminar = self.codigo_borrar.text()
		eliminar = str("'"+ eliminar + "'")

		resp = (self.datosTotal.elimina_productos(eliminar))
		datos = self.datosTotal.buscar_productos()
		i = len(datos)

		self.tabla_borrar.setRowCount(i)
		tablerow = 0
		for row in datos:
			self.tabla_borrar.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[1]))
			self.tabla_borrar.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[2]))
			self.tabla_borrar.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[3]))
			self.tabla_borrar.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[4]))
			self.tabla_borrar.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[5]))
			self.tabla_borrar.setItem(tablerow,5,QtWidgets.QTableWidgetItem(row[6]))
			self.tabla_borrar.setItem(tablerow,6,QtWidgets.QTableWidgetItem(row[7]))
			tablerow +=1

		if resp == None:
			self.borrar_ok.setText("NO EXISTE")
		elif resp == 0:
			self.borrar_ok.setText("NO EXISTE")

		else:
			self.borrar_ok.setText("SE ELIMINO")


if __name__ == "__main__":
     app = QtWidgets.QApplication(sys.argv)
     mi_app = MiApp()
     mi_app.show()
     sys.exit(app.exec_())		