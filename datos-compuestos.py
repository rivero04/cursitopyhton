#LISTAS
# se pueden modificar

lista = ["Nacho Rivero","Bien de Baboso",True,1.81]

print(lista)

# si quiero printear el primer elemento
print(lista[0])
# si quiero printear el segundo elemento
print(lista[1])
# si quiero printear el tercero elemento
print(lista[2])
# si quiero printear el cuarto elemento
print(lista[3])

#TUPLA
# sabemos que vamos a tener unos datos
# que nunca se van a modificar mientras que en las listas los podes cambiar, sacar, etc
#NOSEMODIFICA
tupla = ("Nacho Rivero","Bien de Baboso",True,1.81)

#esto es valido
lista[3] = "maquinola"

#esto no es valido
# tupla[3] = "maquinola"

#CONJUNTO

# creando un conjunto (set)
# se puede redifinir pero no modificar los elementos
# tampoco puede haber datos duplicados , 
# en caso de que halla se imprime uno solo.
# tampoco podemos acceder a los elementos con un indice
# son datos desordenados 
conjunto= {"Nacho Rivero","Bien de Baboso",True,1.81}

#DICT

#creando un diccionario (dict)
# la estructura es key : value y separamos con comas

diccionario = {
    "nombre" : "nacho rivero",
    "esta feliz" : True,
    "altura" : 1.81,
    "dato_duplicado" : "nacho rivero"
}

print(diccionario["nombre"])