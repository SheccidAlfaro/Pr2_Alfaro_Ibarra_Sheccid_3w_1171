print("")
print("Alfaro Ibarra Sheccid, 3w, 1171. Fatura con y sin IVA")
#Definir la funcion y los argumentos (importe, unidad, iva)
def factura(Importe,unidad, iva=21):
    #Definir variable que de el resultado sin IVA
    ttalsiva=Importe*unidad
    #Definir variable que de el resultado de cuanto es el IVA
    ttalciva=ttalsiva*(iva/100)
    #Definir la variable que de el resultado total de todo
    total=ttalsiva + ttalciva
    #fINALIZA Y DEVUELVE LOS RESULTADOS
    return ttalsiva, ttalciva, total
    #Definir variables y preguntar al usuario
importe = float(input("Introduce el importe sin IVA: "))
unidad = int(input("Introduce la cantidad de unidades: "))
#Llamar funcion 
ttalsiva, ttalciva, total = factura(importe, unidad)
#Poner en pantalla los resultados dados
print(f"Total sin IVA: {ttalsiva:}")
print(f"IVA: {ttalciva:}")
print(f"Total con IVA: {total:}")
