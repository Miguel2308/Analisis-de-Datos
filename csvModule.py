# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 03:06:48 2020

@author: Admin
"""
'''
 ESTA SERA LA MANERA CORRECTA DE ANALIZAR ARCHIVoS CSV POR DESORDENADOS QUE ESTEN,
 EL MODULO CSV LIMPIARA TODO POR NOSOTROS, Y DEVOLVERA DATOS TABULARES AGRADABLES Y 
 MAS SENCILLOS DE OBSERVAR.

 PRIMERO CREAMOS UNA FUNCION QUE LEA EL ARCHIVO E ITERE SOBRE LAS FILAS,
 PARA LUEGO ALMACENARLAS EN UNA LISTA PREVIAMENTE INICIALIZADA.

 LO SEGUNDO SERIA UNA FUNCION PARA DAR FORMATO A LA LISTA DE LISTAS Y
 OBTENER DATOS TABULARES LISTOS, LIMPIOS, AGRADABLES Y BIEN PROCESADOS PARA 
 NUESTRA COMODIDAD.  
'''
# de nevo se analizaran los datos como una lista de listas.

"""
Using the csv module.
"""

import csv

def parse(csvfilename):
    """
    Reads CSV file named csvfilename, parses
    it's content and returns the data within
    the file as a list of lists.
    """
    table = []
    with open(csvfilename, "r") as csvfile:
        csvreader = csv.reader(csvfile,
                               skipinitialspace=True)
        for row in csvreader:
            table.append(row)
    return table




def print_table(table):
    """
    Print out table, which must be a list
    of lists, in a nicely formatted way.
    """
    for row in table:
        # encabezado justificado a la izquierda.
        print("{:<19}".format(row[0]), end='')
        # columnas restantes justificadas a la derecha.
        for col in row[1:]:
            print("{:>4}".format(col), end='')
        print("", end='\n')


table = parse("hightemp.csv")
print_table(table)

print("")
print("")


table2 = parse("hightemp2.csv")
print_table(table2)

