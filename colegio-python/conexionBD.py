import mysql.connector

class Registro_datos():

    def __init__(self):
        self.conexion = mysql.connector.connect( host='localhost',
                                            database ='python_colegio', 
                                            user = 'root',
                                            password ='123456')



    def inserta_producto(self,dni, nombre, apellido_parterno, apellido_materno, sexo, fecha_nacimiento, direccion):
        cur = self.conexion.cursor()
        sql='''INSERT INTO estudiante (dni, nombre, apellido_parterno, apellido_materno, sexo, fecha_nacimiento, direccion) 
        VALUES('{}', '{}','{}', '{}','{}','{}','{}')'''.format(dni, nombre, apellido_parterno, apellido_materno, sexo, fecha_nacimiento, direccion)
        cur.execute(sql)
        self.conexion.commit()    
        cur.close()


    def buscar_productos(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM estudiante" 
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro


    def busca_producto(self, nombre_producto):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM estudiante WHERE dni = {}".format(nombre_producto)
        cur.execute(sql)
        nombreX = cur.fetchall()
        cur.close()     
        return nombreX 


    def elimina_productos(self,nombre):
        cur = self.conexion.cursor()
        sql='''DELETE FROM estudiante WHERE dni = {}'''.format(nombre)
        cur.execute(sql)
        a = cur.rowcount
        self.conexion.commit()    
        cur.close()
        return a   


    def actualiza_productos(self, dni, nombre, apellido_parterno, apellido_materno, sexo, fecha_nacimiento, direccion):
        cur = self.conexion.cursor()
        sql ='''UPDATE estudiante SET nombre = '{}', apellido_parterno = '{}', apellido_materno = '{}', sexo = '{}', fecha_nacimiento = '{}', direccion = '{}'
        WHERE dni = '{}' '''.format(nombre, apellido_parterno, apellido_materno, sexo, fecha_nacimiento, direccion, dni)
        cur.execute(sql)
        a = cur.rowcount
        self.conexion.commit()    
        cur.close()
        return a   