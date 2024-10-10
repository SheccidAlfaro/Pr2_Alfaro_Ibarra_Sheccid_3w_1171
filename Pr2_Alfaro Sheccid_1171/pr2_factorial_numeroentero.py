print("")
print("Alfaro Ibarra Sheccid 3w, 1171. REsolver factorial de numero entero")
#Definir funcion y argumento (en este caso "n")
def factorial(n):
    #Utilizar if en caso de que el numero al que sacar factorial sean los siguientes
   if n==0 or n==1:
       resultado=1
   elif n>1:
    #Definir el resultado como poner la operacion para sacar el factorial
        resultado=n*factorial (n - 1)
   return resultado
   
fact7=factorial(7)
print(fact7)
#Definir y mostrar en pantalla el resultado
