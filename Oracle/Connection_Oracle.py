import cx_Oracle

class Connection_Oracle:

    def __init__(self):
        self.user = None
        self.password = None
        self.dsn = 'localhost:1521/XEPDB1'
        self.encoding = 'UTF-8'
        self.connection = None

    def open(self, user, password):
        self.user = user
        self.password = password

        try:
            self.connection = cx_Oracle.connect(self.user, self.password, self.dsn, self.encoding)
            print('Successful Connection')
        except cx_Oracle.DatabaseError as e:
            error = e.args
            print('Database connection error', error.message)
    
    def close (self):
        if (self.connection): # Si hay conexion, desconectar y volver a colocar None
            self.connection.close()
            print('Connection Finished')
            self.connection = None
        else:
            print('There is not connection')

    def query_execution (self, consulta):
        if (self.connection):
            cursor = self.connection.cursor()
            cursor.execute(consulta)
            # Obtiene todos los registros resultantes
            result = cursor.fechall()
            self.connection.commit()
            cursor.close()

            return result
        else:
            print('There is not connection')
