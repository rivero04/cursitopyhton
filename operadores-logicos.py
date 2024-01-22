#AND
# devuelve true si ambas se cumplen

Resultado = True & True #Devolver True
Resultado2 = False & True #Devolver Falso
Resultado3 = True & False #Devolver Falso
Resultado4 = False & False #Devolver Falso

#OR
# devuelve falso solamente si las dos condiciones no se cumplen
# es decir cuando ambas son falsas

Resultado5 = True | True #Devolver True
Resultado6 = False | True #Devolver True
Resultado7 = True | False #Devolver True
Resultado8 = False | False #Devolver Falso

#NOT
# si no es verdadero es falso  y si es verdadero no es falso

Resultado9 = not True #Devolver Falso
Resultado10 = not False #Devolver True

print(Resultado9)
