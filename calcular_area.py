""" 
Calculo del area de un rectangulo
El fin de esta práctica es entender el uso 
de una función
Esta práctica se trata de pedir por pantalla
dos datos que son los lados de un rectángulo 
como valor entero en centímetros
y da como resultado el área de dicho rectángulo
en cm2
"""
def area_rectangulo(lado1,lado2):
    area = lado1 * lado2
    return area
print(f"Esta funcion calcula el area de un rectangulo")
print("pidiendo por pantalla la longitud de cada uno de sus lados")

lado1 = int(input("introduce en cm el valor del lado 1 1: "))
lado2 = int(input("introduce en cm el valor del lado 2: "))        

print(f"El area del rectangulo es: {area_rectangulo(lado1,lado2)} cm2")




