print("")
print("Alfaro Ibarra Sheccid, 3w, 1171, Suma de numeros en lista")
#Definir la funcion con su argumento (numero)
def multlist(nu):
    #Multiplicarlos numeros que den
   resultado = 1
   # iterar sobre elementos
   for numero in nu:
        resultado *= numero
   return resultado
#Mostrar en pantalla la lista y el resultado
print("numeros:2, 2, 4, 3")  
listnum=[2, 2, 4, 3]
resultado= multlist(listnum)
print("EL resultado de la multiplicacion es:", resultado)