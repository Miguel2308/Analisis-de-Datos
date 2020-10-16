# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 17:45:35 2020

@author: Codigo dado por la Universidad de Michigan,
en su curso sobre analisis de datos con python, en Coursera.
"""

# Diccionario con algunas Capitales.
capitals = {'USA': 'Washington, D.C.',
            'China': 'Beijing',
            'France': 'Paris',
            'England': 'London',
            'Italy': 'Rome',
            'Russia': 'Moscow',
            'Australia': 'Canberra',
            'Peru': 'Lima',
            'Japan': 'Tokyo'}


# vale decir que aunque el diccionaro se llama capitals, las claves son los paises y no las ciudades

print("Direct Iteration")
print("================")

for country in capitals:
    print("{}, {}".format(capitals[country], country))

print("")

#  tambien puedo iterar directamente sobre los valores del diccionario


print("Iteration over Values")
print("=====================")

for city in capitals.values():
    print("Capital city: {}".format(city))

print("")



# o sobre las claves:.

print("Iteration over Keys")
print("===================")

for country in capitals.keys():
    print("{}, {}".format(capitals[country], country))

print("")


# con .keys() y values() tenemos las herramientas para indagar claves o valores.

# con .items() podemos iterar directamente sobre los dos elementos clave, valor.
print("Iteration over Items")
print("===================")

for country, city in capitals.items():
    print("{}, {}".format(city, country))

print("")


# comprobar si una clave o valor se encuenrta en el diccionario como clave o como valor segun se especifique.
#  Esto evitara que el interprete devuelva error en caso de que se intente obtener el valor de una clave que no se
# encuentre en el diccionario con el que esta trabajando.

print("Checking Membership")
print("===================")

# de esta manera solo preguntamos por las claves.
print('England' in capitals)
print('Lima' in capitals)

# estas son las maneras correctas:.
print('Moscow' in capitals.keys())
print('Italy' in capitals.keys())

print('Houston' in capitals.values())
print('Beijing' in capitals.values())


