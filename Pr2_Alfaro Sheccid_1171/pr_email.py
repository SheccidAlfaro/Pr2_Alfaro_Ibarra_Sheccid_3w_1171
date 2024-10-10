print("")
print("Alfaro Ibarra Sheccid, 3w, 1171, Prueba de registrar gmail.")
#Definir funcion y argumento (despliegue por el caso de poenr en pantalla)
def gmail(despliegue):
    #Utilizar if para que la secuencia actue con las dos opciones que llegan a cumplir
    if "@" in despliegue:
         print("Tu correo es: " +despliegue)
    else:
        print("Necesita ingresar el @.")
    return
#Preguntar al usuario el dato especifico
despliegue=str(input("Ingresa tu correo electronico:"))
#Llamar funcion
gmail(despliegue)