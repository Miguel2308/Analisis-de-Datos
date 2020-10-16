# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 03:41:44 2020

@author: Admin
"""

# PANDAS INTRODUCCION:

# utilizado para manipulacion y analisis de datos
# a diferencia de numpy, pandas permite dar nombre a las filas y columnas,
# con el fin de facilitar el analisis y la manipulacion de los datos 
# una serie en pandas, es una matriz 1D en numpy
# un DataFrame en pandas, es una matriz 2D en numpy
# un Panel en pandas, es una matriz 3D

# COMO EN MACHINE LEARNING SE UTILIZAN MATRICES 2D, SE ESTUDIARAN LOS 'DATAFRAME'
import pandas as pd
import numpy as np




#..................................................................................




df = pd.DataFrame(np.array([[1,2,3],[4,5,6],[7,8,9]]))
print('DataFrame con matriz numpy')
print(df, '\n')

# una serie
serie = pd.Series({'Uruguay':'Montevideo',
                   'Brasil':'Brasilia',
                   'Francia':'Paris',
                   'Argentina':'Buenos Aires'})
print('SERIES:')
print(serie,'\n')

# PARA EXPLORAR EL DATAFRAME:

print('exploramos el DataFrame con las funciones de pandas\n')

matriz = pd.DataFrame(np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))

print(matriz,'\n')

print(matriz.shape,' ES SU FORMA\n')

# podemos ver su altura o cantidad de filas con .index en combinacion con len
print(len(matriz.index),' ES SU ALTURA\n')

# Podemos ver sus estadisticas 
print(matriz.describe(),' SON LAS ESTADISTICAS\n')  

# Tambien podemos conocer la medida de todas las columnas utilizando mean()
print(matriz.mean(),' SON LAS MEDIDAS DE LAS COLUMNAS\n')

# Correlacion entre columnas 
print(matriz.corr(),' ES LA CORRELACION ENTRE LOS VALORES\n')

# Conteo de datos del DataFrame
print(matriz.count(),' CANTIDAD DE VALORES NO NULOS POR FILA\n')

# max(), min() Y mediana de cada columna 
print(matriz.max(),' VALOR MAXIMO DE CADA COLUMNA\n')
print(matriz.min(),' VALOR MINIMO DE CADA COLUMNA\n')
print(matriz.median(),' REPRESENTA LA MEDIANA DE CADA COLUMNA')
# tAMBIEN SE PUEDE SABER CUAL ES LA DESVIACION ESTANDAR DE CADA COLUMNA 
print(matriz.std(),' DESVIACION ESTANDARD DE CADA COLUMNA\n')

# PARA SELECCIONAR UNA COLUMNA DEL DATAFRAME SOLO DEBE INDICAR EL INDICE DE LA MISMA
print(matriz[0],' ESTA ES LA COLUMNA 0\n')
# PARA SELECCIONAR DOS COLUMNAS O MAS DEL DATAFRAME SOLO DE SE LAS DEBE INDICAR DENTRO DE LOS DOBLE CORCHETES
print(matriz[[0,3]],' ESTO ES LA COLUMNA 0 Y LA 3\n')
# TAMBIEN SE LE PUEDE INDICAR SU POSICION, FILA COLUMNA
print(matriz.iloc[0][3],' ESTO ES LA POSICION [0] [3]\n')
print(matriz.loc[0],' CON .loc[n] PARA SSELECCIONAR TODOS LOS VALORES DE A PRIMERA FILA\n')
# EQUIVALENTE A matriz.iloc[0,:]





# PARA IMPORTAR UN ARCHIVO, ESTE EJEMPLO ES UN ARCHIVO CSV LLAMADO TRAIN LOCALIZADO EN NUESTRO EQUIPO
#--- df = pd.read_csv('train.csv')

# para guardar los cambios hechos sobre el archivo
#--- pd.to_tipoarchivo(nombreArchivo)

# PARA VERIFICAR SI HAY DATOS NULOS EN EL DATAFRAME
print(matriz.isnull(),' LOS DATOS NULOS APARECERAN EN True\n')
print(matriz.isnull().sum(),' DEVUELVE LA SUMA DE LOS DATOS NULOS\n')

# Para deshacernos de los datos perdidos pd.dropna elimina las filas que contengan datos perdidos
print(matriz.dropna(),' DEBERIA BORRAR LOS VALORES NULOS, EN ESTE CASO NO LOS HAY\n')
# y matriz.dropna(axis = 1) elimina las columnas en las que hayan datos nulos

# EN CASO DE NO QUERER PODEMOS REEMPLAZARLOS CON X O COMO EN EL EJEMPLO CON LA MEDIA DE LOS DATOS
print(matriz.fillna('x'),' REEMPLAZA TODOS LOS VALORES NULO CON X\n')
print(matriz.fillna(matriz.mean()), ' REEMPLAZA LOS VALORES NULOS CON LA MEDIA DE LOS VALORES DEL DATAFRAME')


 







