#IF ELSE

contraseña_almacenada = "NachitoCrack"
contraseña_escrita = '''NachitoCrack'''

if contraseña_almacenada == contraseña_escrita:
    print("INICIANDO SESIÒN...")
else: 
    print("CONTRASEÑA EQUIVOCADA, INTENTE DE NUEVO")    
    
    
#ELSE IF en pyhton se escribe "elif"

ingreso_mensual = 81000
gasto_mensual = 80000

#if anidados y else if (elif)

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0: 
        print("estas en deficit")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("bien pa, estas bien")
    else:
        print("y pa, estas gastando una banda, hay que ver si te alcanza")
    
elif ingreso_mensual > 1000:
    print("estas bien en latinoamèrica")
    
elif ingreso_mensual > 500:
    print("estas bien en argentina")
    
elif ingreso_mensual > 200:
    print("estas bien en venezuela")
    
else: 
    print("sos pobre")