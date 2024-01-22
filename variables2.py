
#creando los datos
datos_en_tupla = ("Nacho","Rivero",1000000)
datos_en_lista = ["Nacho","Rivero",1000000]

#desempaquetado
nombre,apellido,plata = datos_en_lista

#mostrando resultado
print(plata)

#TUPLAS (cuando solo vamos a leer datos nos sirven las tuplas)

#creando tuplas con tuple()
tupla = tuple(["dato1","dato2"])

#creando una tupla sin parentesis de multiples datos
tupla = "dato1","dato2"

#creando una tupla sin parentesis de un solo dato
tupla = "dato",

print(tupla)


#CONJUNTOS

#creando un conjunto con set()
conjunto = set(["Dato 1"])

#metiendo un conjunto dentro de otro conjunto con frozenset
conjunto1 = frozenset(["dato 1", "dato 2"])
conjunto2 = {conjunto1,"dato 3"}
print(conjunto2)

#Teoria de conjuntos

conjunto1 = {1,3,5,7}
conjunto2 = {2,4,7,8}

#verificando si es un subconjunto
resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1

#verificando si es un superconjunto
resultado = conjunto2.issuperset(conjunto1)
resultado = conjunto2 > conjunto1

#verificar si hay algùn nùmero en comun
resultado = conjunto2.isdisjoint(conjunto1)

print(resultado)

#DICCIONARIOS

#creando diccionarios con dict()
diccionario = dict(nombre="nacho",apellido="rivero")

#las listas no pueden ser claves y usamos frozenset para meter conjuntos
diccionario = {frozenset(["rivero","rancio" ]):"jajas"}

#creando diccionarios con fromkeys() valor por defecto: none
diccionario = dict.fromkeys(["nombre","apellido"])

#creando diccionarios con fromkeys() cambiando el valor por defecto a "no se"
diccionario = dict.fromkeys(["nombre","apellido"],"No se")

print(diccionario["nombre"])
