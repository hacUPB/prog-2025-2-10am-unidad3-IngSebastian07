'''
Ejercicio 8: Verificador de Números Primos

Dificultad: Intermedio

Implementa un programa que determine si un número es primo y, en caso de no serlo, muestre sus factores. El programa debe:

1. Solicitar al usuario un número entero positivo mayor que 1
2. Determinar si el número es primo
3. Si no es primo, mostrar todos sus factores
4. Permitir al usuario verificar múltiples números

Entrada: Un número entero positivo
Salida: Mensaje indicando si el número es primo o no, y sus factores si corresponde
'''
'''
VARIABLES DE ENTRADA
Numero              int

VARIABLE DE SALIDA 
Divisores
'''

Numero = int(input("Ingrese un número mayor que 1 para saber si es primo o no: "))
contador = 0
for i in range (1, Numero +1):
    if Numero % i == 0:
        contador = contador + 1

if contador == 2:
    print (f"El número {Numero} es primo.")
else:
    print (f"{Numero} no es primo. Los divisores de {Numero} son:")
    for i in range (1, Numero +1):
        if Numero % i == 0:
            print (i)

