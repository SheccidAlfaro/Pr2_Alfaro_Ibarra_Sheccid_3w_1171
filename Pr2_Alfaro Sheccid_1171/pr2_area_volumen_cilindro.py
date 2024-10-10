print("")
print("Alfaro Ibarra Sheccid, 3w, 1171, Area y volumen de un cilindro")
#Definir la funcion y argumentos(en este caso son r y h)
def aryvol(r, h):
    #Definir constante (pi) y variables con las operaciones para tener a cabo lo solicitado
    pi=3.1416
    totalvolumen=pi*(r*r)*h
    totalarea=2*pi*r*h
    #Finaliza y devuelve
    return totalvolumen, totalarea
#Preguntar al usuario
r=float(input("Coloca el radio del cilindro:"))
h=float(input("Coloca la altura del cilindro:"))
#llamar funcion
totalvolumen, totalarea= aryvol(r, h)
#Mostrar en pantalla 
print("Volumen del cilindro:", totalvolumen)
print("Area del cilindro:", totalarea)