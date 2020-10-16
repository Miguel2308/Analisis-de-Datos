# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 20:24:16 2020

"""

# EN ESTE DOCUMENTO SE VERA MATPLOTLIB BASICO
#--------------------------------------------

# LIBRERIA DE TRAZADO UTILIZADA PARA GRAFICOS 2D

import matplotlib.pyplot as plt

# Con este codigo se genera una grafica lineal azul.
'''
x = [1,2,3,4]
y = [11,15,33,30]

# Si en lugar de una grafica lineal, deseamos que se muestren solo los puntos dados
# utilizar: scatter()
plt.plot(x, y, color='blue', lineWidth=3, label='line')
plt.legend()
plt.show()
'''
#--- IMPORTANTE: los datos para machine learning, deberan estar estructurados con numpy.

# grafic 1
x1 = [0,2,4,6,8]
y1 = [0,10,14,22,17.5]

#grafic 2
x2 = [0,2,4,6,8]
y2 = [10,6,7,12,5]

# En el siguiente codigo hay dos graficas sobre un grid. (liberar codigo para ver.)
'''
plt.plot(x1,y1,label = 'Venta', linewidth = 4, color = 'blue')
plt.plot(x2,y2,label = 'Inversion', linewidth = 4, color = 'red')


plt.title('Ventas e Inversiones bimestrales')
plt.xlabel('eje x')
plt.ylabel('eje y')

plt.legend()
plt.grid()
plt.show()
'''

# En el siguiente codigo hay una grafica de barras.
# igual al codigo anterior, pero se debe cambiar de la funcion plot() a bar()
'''
plt.bar(x1,y1,label = 'Venta', linewidth = 4, color = 'blue')
plt.bar(x2,y2,label = 'Inversion', linewidth = 4, color = 'red')


plt.title('Ventas e Inversiones bimestrales')
plt.xlabel('eje x')
plt.ylabel('eje y')

plt.legend()
plt.grid()
plt.show()
'''


# TAMBIEN SE PUEDEN GRAFICAR HISTOGRAMAS: se usan para mostrar distribucion

# Definir los dattos
'''
a = [22,34,54,23,76,25,98,74,22,43,54,65,72,23,41,60,48,59,23,45,
     44,56,23,44,12,13,43,21,53,44]
bins = [0,10,20,30,40,50,60,70,80,90,100]

# definir las carcteristicas del grafico
plt.hist(a,bins, histtype = 'bar', rwidth = 0.8, color = 'lightgreen')

# titulo y nombre de ejes
plt.title('Histograma')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')

# Mostrar figura
plt.show()
'''

# GRAFICOS DE DISPERSION: se utilizan para compara variables.
'''
plt.scatter(x1,y1,label = 'Var1', linewidth = 4, color = 'blue')
plt.scatter(x2,y2,label = 'Var2', linewidth = 4, color = 'green')


plt.title('Grafica de Dispersion')
plt.xlabel('eje x')
plt.ylabel('eje y')

plt.legend()
plt.grid()
plt.show()
'''


# GRAFICAS CIRCULARES

# despues de analizar me doy cuenta de que en divisiones se estan asignando los valores a la grafica sacados de los arrays.
# vale explicar que en este caso cada valor correspondiente a cada lugar de indice en la variable
# corresponde a las horas por dia, para el valor de indice [0], corresponde a divisiones = [1,7,8,2,6]
comer = [1.0,2,4,0.5,1.1]
dormir = [7,5,3,7.5,6]
trabajar = [8,10,15,6,0]
recreacion = [2,1.5,1,2,0]
otros = [6,4.5,1,8,16.5]

divisiones = [1,7,8,2,6]
actividades = ['comer','dormir','trabajar','recreacion','otros']
colores = ['red','purple','blue','orange','green']

plt.pie(divisiones,labels=actividades, colors=colores, startangle=90, shadow=True, explode=(0.1,0,0,0,0), autopct='%1.1f%%')
plt.title('Grafica Circular')
plt.show() 
       

