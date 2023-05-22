import cx_Oracle
class User:

    def Connection(usuario, contraseña):
        try:
            connection = cx_Oracle.connect(
                user = usuario,
                password = contraseña,
                dsn = 'localhost:1521/XEPDB1',
                encoding = 'UTF-8'
            )
            print("CONECTADO!")

        except Exception as ex:
            print(ex)