import cx_Oracle


class Connection_Oracle:

    def __init__(self):
        self.user = None
        self.password = None
        self._connection = None
        self._dsn = 'localhost:1521/XEPDB1'
        self._encoding = 'UTF-8'

    def open(self, user, password) -> bool:
        self.user = user
        self.password = password
        # print(f"Usuario {self.user}, {self.password}")

        try:
            self._connection = cx_Oracle.connect(
                user=self.user,
                password=self.password,
                dsn=self._dsn,
                encoding=self._encoding)

            print('Successful Connection')
            return True
        except Exception as ex:
            error = ex
            print('Database connection error', error)
            return False

    def close(self):
        if self._connection:  # Si hay conexion, desconectar y volver a colocar None
            self._connection.close()
            print('Connection Finished')
            self._connection = None
        else:
            print('There is not connection')

    def query_execution(self, consulta):
        if self._connection:
            cursor = self._connection.cursor()
            cursor.execute(consulta)
            # Obtiene todos los registros resultantes
            result = cursor.fechall()
            self._connection.commit()
            cursor.close()

            return result
        else:
            print('There is not connection')
