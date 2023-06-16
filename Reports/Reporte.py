import csv
import os
import cx_Oracle
from agatereports.basic_report import BasicReport
import webbrowser
import logging

logger = logging.getLogger(__name__)


def create_connection():
    connection = cx_Oracle.connect(
        user='developer',
        password='PassDev',
        dsn='localhost:1521/XEPDB1',
        encoding='UTF-8'
    )
    return connection


def reporte_habitad(habitad):
    connection = create_connection()
    cursor = connection.cursor()

    query = str(f'''SELECT NOMBRE_ANIMAL, 
                    NOMBRE_COMUN, 
                    NOMBRE_CIENTIFICO 
                    FROM DEVELOPER.ANIMAL
                    JOIN DEVELOPER.ESPECIE USING(ID_ESPECIE)
                    JOIN DEVELOPER.HABITAT USING(ID_HABITAT)
                    WHERE NOMBRE_HABITAT LIKE \'{habitad}\'''')

    cursor.execute(query)
    resultados = cursor.fetchall()
    print(resultados)
    archivo_csv = 'temp.csv'
    with open(archivo_csv, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['NOMBRE_ANIMAL', 'NOMBRE_COMUN', 'NOMBRE_CIENTIFICO'])
        for row in resultados:
            writer.writerow(row)

    cursor.close()
    connection.close()
    jrxml = './jrxml/QuerryAcuario.jrxml'
    outpt = './output/1.pdf'
    data = './temp.csv'
    datareport_csv(jrxml_filename=jrxml, output_filename=outpt, data_csv=data)
    ruta_pdf = os.path.abspath('./output/1.pdf')
    abrir_pdf_en_navegador(ruta_pdf)


def reporte_peligro_extincion(estado_extincion):
    connection = create_connection()
    cursor = connection.cursor()

    query = str(f'''SELECT NOMBRE_CIENTIFICO AS ESPECIE_AMENAZADA
                    FROM DEVELOPER.ANIMAL
                    JOIN DEVELOPER.PELIGRO USING(ID_PELIGRO)
                    JOIN DEVELOPER.ESPECIE USING(ID_ESPECIE)
                    WHERE PELIGRO LIKE \'{estado_extincion}\'
                    GROUP BY NOMBRE_CIENTIFICO''')

    cursor.execute(query)
    resultados = cursor.fetchall()
    archivo_csv = 'temp.csv'
    with open(archivo_csv, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['NOMBRE_CIENTIFICO'])
        for row in resultados:
            writer.writerow(row)

    cursor.close()
    connection.close()
    jrxml = './jrxml/2.jrxml'
    outpt = './output/2.pdf'
    data = './temp.csv'
    datareport_csv(jrxml_filename=jrxml, output_filename=outpt, data_csv=data)
    ruta_pdf = os.path.abspath('./output/2.pdf')
    abrir_pdf_en_navegador(ruta_pdf)


def reporte_cantidad_animales():
    connection = create_connection()
    cursor = connection.cursor()

    query = str(f'''SELECT NOMBRE_HABITAT, COUNT(NOMBRE_ANIMAL) AS ANIMALES
                    FROM DEVELOPER.ANIMAL
                    JOIN DEVELOPER.HABITAT USING(ID_HABITAT)
                    GROUP BY NOMBRE_HABITAT
                    ORDER BY ANIMALES''')

    cursor.execute(query)
    resultados = cursor.fetchall()
    archivo_csv = 'temp.csv'
    with open(archivo_csv, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['NOMBRE_HABITAD', 'ANIMALES'])
        for row in resultados:
            writer.writerow(row)

    cursor.close()
    connection.close()
    jrxml = './jrxml/4.jrxml'
    outpt = './output/4.pdf'
    data = './temp.csv'
    datareport_csv(jrxml_filename=jrxml, output_filename=outpt, data_csv=data)
    ruta_pdf = os.path.abspath('./output/4.pdf')
    abrir_pdf_en_navegador(ruta_pdf)


def datareport_csv(jrxml_filename, output_filename, data_csv):

    logger.info('running datasource csv sample')

    # CSV datasource configuration
    data_config = {'adapter': 'csv', 'filename': data_csv}

    pdf_page = BasicReport(jrxml_filename=jrxml_filename, output_filename=output_filename, data_config=data_config)
    pdf_page.generate_report()


def abrir_pdf_en_navegador(ruta_pdf):
    url = ruta_pdf
    webbrowser.open_new_tab(url)


# reporte_habitad("Reptiles")
# reporte_peligro_extincion("Amenzada")
# reporte_cantidad_animales()
