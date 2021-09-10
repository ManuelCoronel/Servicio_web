import pymysql

class Database:
    def __init__(self):
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            db="personas")

        self.cursor = self.connection.cursor()
        print("Conexion establecidad exitosamente!")

    def select_user(self, id):
        print(id)
        sql = "SELECT cedula, nombre, edad, pais FROM persona WHERE cedula = {dato}".format(dato=id)
        try:
            self.cursor.execute(sql)
            persona = self.cursor.fetchone()
            print(persona)
        except Exception as e:
            raise
        return persona

    def select_all_user(self):
        sql = "SELECT cedula, nombre, edad, pais FROM persona"
  #      print(sql)
        try:
            self.cursor.execute(sql)
            personas = self.cursor.fetchall()
        except Exception as e:
            raise
        return personas

    def insert_user(self,cedula, nombre, edad, pais):
        sql = 'INSERT INTO persona values ({cedula},"{nombre}",{edad},"{pais}")'.format(cedula=cedula,nombre=nombre,edad=edad,pais=pais)
        print(sql)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise

    def delete_user(self,cedula):
        sql = 'DELETE FROM persona WHERE cedula = {cedula}'.format(cedula=cedula)
        print(sql)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise


    def update_user(self, cedula, nombre, edad, pais):
        sql = 'UPDATE persona SET nombre = "{nombre}", edad = {edad}, pais = "{pais}" WHERE persona.cedula= {cedula}'.format(cedula=cedula, nombre=nombre, edad=edad, pais=pais)
        print(sql)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise









#database = Database()
#database.select_all_user()