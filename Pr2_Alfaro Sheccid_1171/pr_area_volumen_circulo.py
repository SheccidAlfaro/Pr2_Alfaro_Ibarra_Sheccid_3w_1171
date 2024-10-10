print("")
print("ALfaro Ibarra Sheccid, 3w, 1171, Area, volumen de una esfera")
#Definir la funcion y argumento(en este caso solo r)
def volumen (r):
    #Definir una contante y las variables que den los resultados que se especifican
    pi=3.1416
    totalvolumen= (4/3)*pi*(r*r*r)
    totalarea=4*pi*(r*r)
    #Finalizar y devolver el valor
    return totalvolumen, totalarea
#Definir y preguntar al usuario
r=float(input("Poner el radio de la esfera:"))
#Funcion
totalvolumen, totalarea= volumen(r)
#Mostrar en pantalla
print("Volumen de la esfera:", totalvolumen)
print("Area de la esfera:", totalarea)

