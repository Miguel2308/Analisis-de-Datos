# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 01:07:59 2020

"""
'''
 Este archivo marca un comienzo para trabajar y comenzar a dar formato 
a nuestro datos con listas de listas y el metodo .format().
'''

# Programming language popularity, from www.tiobe.com/tiobe-index
popularity = [["Language", 2017, 2012, 2007, 2002, 1997, 1992, 1987],
              ["Java", 1, 2, 1, 1, 15, 0, 0],
              ["C", 2, 1, 2, 2, 1, 1, 1],
              ["C++", 3, 3, 3, 3, 2, 2, 5],
              ["C#", 4, 4, 7, 13, 0, 0, 0],
              ["Python", 5, 7, 6, 11, 27, 0, 0],
              ["Visual Basic .NET", 6, 17, 0, 0, 0, 0, 0],
              ["PHP", 7, 6, 4, 5, 0, 0, 0],
              ["JavaScript", 8, 9, 8, 7, 23, 0, 0],
              ["Perl", 9, 8, 5, 4, 4, 10, 0]]


''' los valores dentro de {} son por cuestiones de visualizacion.
{:<} esta alineando a la derecha los encabezados y {:>} esta alineando los enteros a la derecha.
'''
format_string = "{:<18}  {:>4}  {:>4}  {:>4}  {:>4}  {:>4}  {:>4}  {:>4}"


# Display langauges table
headers = popularity[0]
header_row = format_string.format(*headers) # * es para asignar a cada valor de la cadena de formato 
# un valor que se encuentra en el encabezado, pasandolo al .format(*headers), para que cubra todos los argumentos esperados.

print(header_row)

# aca imprimimos una linea punteada del largo de header_row
print("-" * len(header_row))

# se itera a partir del row 1 por logicas razones ya que en la posicion de indice [0]
# estaran los encabezados (headers).
# se le vuelve a pasar el format al iterador con * para asignar a cada argumento lo que le corresponda
for language in popularity[1:]:
    print(format_string.format(*language))

print("")


# Finding/selecting items

# What was Python's popularity in 1997? row 5 column 5
print("Python's popularity in 1997:", popularity[5][5],)


''' Esto es algo muy basico en el que le pasamos a una funcion la tabla y la columna,
 Y a la otra funcion la tabla y la fila, se los podria colocar como metodos
 de una funcion que reciba tabla, col, row: para dejar todo en una unica funcion.
'''

def find_col(table, col):
    
    return table[0].index(col)
   


def find_row(table, row):
    
    for idx in range(len(table)):
        if table[idx][0] == row:
            return idx
    return -1
    


idx1997 = find_col(popularity, 2017)
idxpython = find_row(popularity, 'Python')
print("Python's popularity in 2017:", popularity[idxpython][idx1997])



