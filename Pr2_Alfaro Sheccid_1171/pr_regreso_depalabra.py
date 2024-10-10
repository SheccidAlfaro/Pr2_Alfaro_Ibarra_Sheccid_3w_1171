print("")
print("Alfaro Ibarra Sheccid, 3w, 1171, Longitud de la ultima palabra de una oracion...")
#Definir funcion con argumento(palabra)
def regreso(palabra):
    # Eliminar espacios al principio y al final, y luego dividir la cadena por espacios
    palabra = palabra.strip().split()
    if palabra:
        # Retornar la longitud de la última palabra
        return len(palabra[-1])
    else:
        return 0  # Si no hay palabras, regresar 0
#Definir y preguntar al usuario
palabra=(input("ingrese una oracion:"))
#Mostrar en pantalla
print("Longitud de la ultima palbra es:", regreso(palabra))