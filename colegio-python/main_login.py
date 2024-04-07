import sys
import conexion 
import time 
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication 
from GUI import *
import main
from conexionBD import*

class MiApp2(QMainWindow):
	def __init__(self):
		super(MiApp2, self).__init__()
		uic.loadUi('frmLogin.ui',self)
	
		self.bt_ingresar.clicked.connect(self.iniciar_sesion)

		self.datos = conexion.Registro_datos2()

	def iniciar_sesion(self):
		self.contrasena_incorrecta.setText('')
		self.usuario_incorrecto.setText('')
		users_entry = self.users.text()
		password_entry = self.password.text()

		users_entry = str("'" + users_entry + "'")
		password_entry = str("'" + password_entry + "'")

		dato1 = self.datos.busca_users(users_entry)
		dato2 = self.datos.busca_password(password_entry)

		fila1 = dato1
		fila2 = dato2

		if fila1 == fila2:	
			if dato1 == [] and dato2 ==[]:
				self.contrasena_incorrecta.setText('Contraseña incorrecta')
				self.usuario_incorrecto.setText('Usuario incorrecto')
			else:

				if dato1 ==[]:
					self.usuario_incorrecto.setText('Usuario incorrecto')
				else:
					dato1 = dato1[0][1]

				if dato2 ==[]:
					self.contrasena_incorrecta.setText('Contraseña incorrecta')
				else:
					dato2 = dato2[0][2]

				if dato1 != [] and dato2 != []:
					for i in range(0,99):
						time.sleep(0.02)
						self.progressBar.setValue(i)
						self.cargando.setText('Cargando...')

					self.hide()
					self.ventana = main.MiApp()
					self.ventana.show()
		else:
			self.contrasena_incorrecta.setText(' Error ')
			self.usuario_incorrecto.setText(' Error ')
			

if __name__ == "__main__":
     app = QApplication(sys.argv)
     mi_app = MiApp2()
     mi_app.show()
     sys.exit(app.exec_())	