import os.path
import subprocess
import cx_Oracle
from Oracle.Connection_Oracle import Connection_Oracle

def generate_report(name_file, conn):
    jasper_starter_path = "./Program Files (x86)/JasperStarter"
    jrxml_file = open(f'./{name_file}.jrxml', 'w')
    jrxml_file.close()
    jasper_file = open(f'./{name_file}.jasper', 'w')
    jasper_file.close()
    output_file = open(f'./{name_file}.pdf', 'w')
    output_file.close()



    db_params = {
        "host": "localhost",
        "port": "1521",
        "database": "xepdb1",
        "user": conn.user,
        "password": conn.password
    }

    compile_comand = [
        jasper_starter_path,
        "compile",
        jrxml_file,
        "-o",
        jasper_file
    ]

    generate_command = [
        jasper_starter_path,
        "printraw",
        jasper_file,
        "-f",
        "PDF",
        "-o",
        output_file,
        "-t",
        "oracle",
        "-u",
        db_params["user"],
        "-p",
        db_params["password"],
        "-H",
        db_params["host"],
        "-n",
        db_params["port"],
        "-n",
        db_params["database"]
    ]

    subprocess.run(compile_comand)

    subprocess.run(generate_command)

#conn = Connection_Oracle()
#conn.user = "Developer"
#conn.password = "PassDev"
#name_file = "reporte"
#generate_report(name_file, conn)

def generar_reporte(ruta_jrxml):
    cx_Oracle.init_oracle_client(lib_dir = 'ojdbc8.jar')
    connection = cx_Oracle.connect(
                user='developer',
                password='PassDev',
                dsn='localhost:1521/XEPDB1',
                encoding='UTF-8')

    cursor = connection.cursor()
    query = '''SELECT NOMBRE_HABITAT, COUNT(NOMBRE_ANIMAL) AS ANIMALES
               FROM ANIMAL
               JOIN HABITAT USING(ID_HABITAT)
               GROUP BY NOMBRE_HABITAT
               ORDER BY ANIMALES'''

    query = '''SELECT * FROM EMPLEADO'''
    cursor.execute(str(query))

    with open("datos.csv", "w") as archivo_csv:
        for row in cursor:
            archivo_csv.write(','.join([str(x) for x in row]) + '\n')

    comando = f"jasperstarter pr {ruta_jrxml} -f csv -t oracle -u developer -p PassDev -H localhost --db-sid XEPDB1 -o reporte.pdf"
    subprocess.call(comando, shell=True)
    cursor.close()
    connection.close()

    print("Reporte generado con éxito.")


    # jrxml_file = open(f'./Files/QuerryAcuario.jrxml', 'w')
    # jrxml_file.close()
    ruta_jrxml = "Files/QuerryAcuario.jrxml"
    generar_reporte(ruta_jrxml)
