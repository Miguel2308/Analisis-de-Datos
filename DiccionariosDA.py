# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 20:56:55 2020

@author: Admin
"""

# podemos crear una lista con tupla y transformarlas en un diccionario 

diccionary = [(1,'uno'),(2,'dos'),(3,'tres'),(4,'cuatro'),(5,'cinco')]
mi_diccionario = dict(diccionary)

print(mi_diccionario,'Diccionario creado a partir de una lista con tuplas','\n')



cipher = {'p':'9', 'y':'6', 't':'5', 'h':'2', 'o':'1', 'n':'4'}
# con esta funcion obtengo los valores de las claves
def encrypt(word):
    encrypted = []
    for i in word:
        encrypted += cipher[i]
    return encrypted


palabra = 'python'

enc = encrypt(palabra)
#............
#cipher = enc
#...........:

print(enc,'\n')
#print(cipher)

# si queremos buscar una clave la cual no sabeos si se encuentra en el diccionario pero queremos intentar
# debemos llamar al metodo get()

print(cipher.get('t'),'.....es el valor para get("t")','\n')
print(cipher.get(1),'.....es lo que devuelve si la clave no esta en el diccionario get(1)','\n')
print(cipher.get(1,'t'),'.....si uno no esta en el diccionario devolvera el valor predeterminado que hemos indicado get(1,"t")','\n')

# Para asignar un nuevo valor a una clave existente.
cipher['p'] = 'g'

print(cipher,'Se ha modificado el valor para "p"','\n')

# tambien se puede agregar clave valor que no existan en el diccionario, con la misma sintaxis 
# con la que hemos actualizado una clave.

cipher['m'] = 'i'
print(cipher,'Se agrego una nueva clave valor al diccionario','\n')


enc2  = encrypt(palabra)
print(enc2)


print('\n')
print('\n')
print('\n')



#  DICCIONARY KEYS: 
    # CHECKING KEYS.

print('checking keys','\n')


# para averiguar si una clave se encuentra en un diccionario usamos in
print('m' in cipher) # para 'm devolvera true, en tal caso ya podemos mandar a imprimir su valor.

mapping = {1:100,2:120,3:240,4:520,5:89}

keys = [1,2,3,4,5,6] # 6 no se encuentra en el diccionario

# mapeamos las claves e imprimimos su valor correspondiente en el diccionario.
for key in keys:
    if key in mapping:
        print(key,mapping[key])
    else:
        print('{} no esta como clave en el diccionario mapping'.format(key))
        

# IMPORTTANTE:   EN PYTHON LAS CLAVES DEBEN SER DEL MISMO TIPO PARA EVITAR QUE ELINTERPRETE 
# MALINTERPRETE LO QUE QUEREMOS HACER CUANDO QUEREMOS AGREGAR UN NUEVO MAPEO O ACTUALIZAR UNO EXISTENTE.





#..............................

# HANDLING DICTIONARY ERRORS

print('\n')
print('\n')
print('\n','HANDLING DICTIONARY ERRORS')


# En los diccionarios las claves deben de ser inmutables, si las claves son mutables, 
# python no sabra como hacer el hash.

# por ejemplo si la claves esta compuestas por nombre y apellido, debemos de colocarla dentro de 
# parentesis curvo para representar una tula y no entre corchetes como una lista, 
# ya que las tuplas son inmutables y las listas mutables.

# una funcion que devuelva el valor de una clave si se encuentra enel diccionario,
# si no es asi que devuelva un valor por default.
# el valor -1 es un quivalente a False, seria intuitivo si se lo asignamos como valor por defecto
# expresando que la clave no se encuentra en el diccionario.

def lookup(my_dict,my_key,default_value = None):
    if my_key in my_dict:
        return my_dict[my_key]
    else:
        return default_value


simple_dict = {'joe':1, 'scott':2, 'jhon':3}
'''
print(lookup(simple_dict,'joe',-1))
print(lookup(simple_dict,'stephen',-1))
print(simple_dict)
'''

print(simple_dict.get('scott',-1))
print(simple_dict.get('stephen',-1))
print(simple_dict.get('stephen'))

# de ninguna de las dos maneras se agrega un nuevo mapeo.


