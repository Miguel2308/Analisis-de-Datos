# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 19:02:45 2020

@author: Admin
"""



"""
Example code to read and parse a CSV file.
"""

def parse(csvfilename):
    """
    Reads CSV file named csvfilename, parses
    it's content and returns the data within
    the file as a list of lists.
    """
    # rstrip() es para deshacerse del espacio en blanco final
    # y luego se obtienen todas las columnas llamando al metdo split(',')
    table = []
    with open(csvfilename, "r") as csvfile:
        for line in csvfile:
            line = line.rstrip()
            columns = line.split(',')
            table.append(columns)
    return table

# es la temperatura media mensual alta para una variedad de ciudades.
#print(parse('hightemp.csv'))



# luego ya se puede dar formato y hacer que que los datos  se representen de una 
# forma mas agradable.

# se analizaran como una lista de listas:.

def print_table(table):
    """
    Print out table, which must be a list
    of lists, in a nicely formatted way.
    """
    for row in table:
        # Header column left justified
        print("{:<19}".format(row[0]), end='')
        # Remaining columns right justified
        for col in row[1:]:
            print("{:>4}".format(col), end='')
        print("", end='\n')

table = parse("hightemp.csv")
print_table(table)

print("")
print("")

#table2 = parse("hightemp2.csv")
#print_table(table2)


# LA VARIABLE table2 ALMACENA UN CSV QUE NO SE FORMATEA DE MANERA AGRADABLE,
# ES POR ESO QUE EN EL SIGUIENTE ARCHIVO SE TRATARA EL MODULO csv.
# ...Quitar # para ver como reacciona ante nuestro intento de dar formato...