a = 2
b = 3
c = a + b

print(c)

nombre = "nacho"

print(nombre)

# concatenar con +
bienvenida = "Hola " + nombre +  " ¿Como estas?"

# "del bienvenida" aca borramos la variable

print(bienvenida)

# otra formade hacerlo, lo que hace esto 
# es agarar el dato que le den y lo pasa a texto
# entonces es mas comodo usar esta forma

#concatenar con f-string
bienvenida2 = f"Hola {nombre} ¿Como estas?"
print(bienvenida2)


#operadores de pertenencia, siempre nos dan True  o False
print("nacho" in bienvenida2) # si estaa "in"
print("pepe" not in bienvenida2) # no esta "not in"