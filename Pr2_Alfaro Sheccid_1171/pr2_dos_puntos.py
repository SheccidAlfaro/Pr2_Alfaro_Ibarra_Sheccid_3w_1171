print("")
print("Alfaro Ibarra Sheccid, 3w,1171, Distancia de dos puntos.")
#Utilizar librertia para operaciones matematicas
import math
#DEfinir funcion y argumentos(punto1 y punto 2)
def distancia_dirigida(punto1, punto2):
    # Descomponer los puntos en coordenadas
    x1, y1 = punto1
    x2, y2 = punto2
    
    # Calcular las diferencias
    delta_x = x2 - x1
    delta_y = y2 - y1
    
    # Calcular la distancia
    distancia = math.sqrt(delta_x**2 + delta_y**2)
    
    return (delta_x, delta_y), distancia

#Utilizar a base del plano cartesiano, formula de la distancia para obtener el resultado
punto1 = (7, 13)
punto2 = (9, 18)
vector, distancia = distancia_dirigida(punto1, punto2)
#Mostrar en pantalla 
print("Vector de desplazamiento:", vector)
print("Distancia dirigida:", distancia)
