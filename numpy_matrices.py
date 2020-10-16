#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import numpy as np

'''a = np.array([1,2,3])
print('1D array: ')
print(a)

b = np.array([(1,2,3),(4,5,6)])
print('2D array: ')
print(b) '''

# numpy ocupa mucha menos memoria que las lista de python:
'''s = range(1000)
print('resultado lista python: ')
print(sys.getsizeof(5) * len(s))
print()

d = np.arange(1000)
print('Resultado numpy array: ')
print(d.size * d.itemsize) '''

# DEFINIMOS UNA MATRIZ CON TIPO DE DATOS ENTERO DE 64 BITS

array = np.array([[1,2,3,4],[5,6,7,8]], dtype=np.int64)
print(array)


# TAMBIEN PODEMOS CREAR MATRICEZ VACIAS LAS CUALES LUEGO PODRAN SER APROVECHADAS:

# creara una matriz de unos con 3 filas y 4 columnas:
print('matriz de unos')
unos = np.ones((3,4))
print(unos)
# una matriz con ceros, con la instruccion .zeros(())
print('Matriz con ceros')
ceros = np.zeros((3,4))
print(ceros)

# si lo que queremos es una matriz con numeros aleatorios:
print('Matriz random')
aleatorio = np.random.random((2,2))
print(aleatorio)

# matriz vacia:
print('matriz vacia: ')
vacio = np.empty((3,4))
print(vacio)

# si queremos que la matiz contenga un solo valor en todas sus posiciones:
print('Matriz con un solo valor:')
unValor = np.full((3,4),8)
print(unValor)

print()
# matriz con valores espaciados uniformemente
# el tercer parametro de arange es el intervalo entre el param1 y el param2.
print('matriz espaciada uniformemente')
espacio1 = np.arange(0,30,5)
print(espacio1)

print()
# el tercer parametro de linspace es la cantidad de valores que queremos generar 
# entre para1 y param2.
espacio2 = np.linspace(0,2,5)
print(espacio2)

# crear matriz identidad
print()
print('Matriz identidad con .eye(par1,par2)')
identidad1 = np.eye(4,4)
print(identidad1)

print('matriz identidad con .identity(par)')
identidad2 = np.identity(4)
print(identidad2)


#--------------------------
# DE AQUI EN ADELANTE SE INSPECCIONARAN MATRICES...
#..................................................

# la funcion .ndim devuelve la dimension de la matriz
print()
print()
print('EN ADELANTE SE INSPECCIONARAN MATRICES')
a = np.array([(1,2,3,4),(5,6,7,8)])
print(a)
print(a.ndim,' DIMENSIONES')

# O SU TIPO DE DATO DE LOS ELEMENTOS ALMACENADOS EN LA MATRIZ
print(a.dtype,' TIPO DE DATO')

# TAMBIEN EL TAMAÑO Y LA FORMA
print(a.size, ' ES EL TAMAÑO') 
print(a.shape,' ES SU FORMA, EN FILAS Y COLUMNAS')

# TAMBIEN SE PUEDE CAMBIAR SU FORMA 
print()
print('forma anterior')
print(a)
print()
print('nueva forma con .reshape()')
print(a.reshape(4,2))

# PARA SELECCIONAR UN ELEMENTO, ESPECIFICAMOS SUS COORDENADAS (FILAS,COLUMNAS)
print()
print('otro array')
b = np.array([(1,2,3,4),(5,6,7,8)])
print(b)
print('necesito el elemento en pos[1,3]')
print(b[1,2])
print('si deseo todos los valores desde la fila 0, en la columna 2 ')
print(b[0:,2])

print()

# Tambien se puede obtener el valor minimo maximo y la suma de la matriz
print(b.min(),' Es el valor mas chico\n')
print(b.max(),' ES EL VALOR MAYOR\n')
print(b.sum(),' ES LA SUMA DE LOS VALORES DE LA MATRIZ\n')
print(b.mean(),' Es la media de la suma de los valores del array dividido la cantidad de elementos')
# Tambien se puede obtener la raiz cuadrada y la desviacion estandar de la matriz
print(np.sqrt(b),' RAIZ CUADRADA DE CADA VALOR\n')
print(np.std(b),' ES LA DESVIACION ESTANDAR\n')


# TAMBIEN SE PUEDEN SUMAR RESTAR DIVIDIR Y MULTIPLICAR UNA MATRIZ CON OTRA



 

    
