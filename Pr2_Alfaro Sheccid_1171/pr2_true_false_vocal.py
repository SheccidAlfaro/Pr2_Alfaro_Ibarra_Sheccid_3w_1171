print("")
print("Alfaro Ibarra Sheccid, 3w, 1171, Vocales")
#Definir la funcion con su argumento (v)
def vrdvocal(v):
    #Utilizar if para saber si esta cumpliendo o no con el pedido
    if v== "a" or v=="A":
        print("True.")
        return
    if v== "e" or v=="E":
        print("True.")
        return
    if v== "i" or v=="I":
        print("True.")
        return
    if v== "o" or v=="O":
        print("True.")
        return
    if v== "u" or v=="U":
        print("True.")
        return
    print("False")
#Preguntar al usuario y llamar funcion
v=(input("Ingresa caracter:"))
vocal= vrdvocal(v)
