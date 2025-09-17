# Tabla de Multiplicar.

N = int(input("Ingrese un número entero para conocer su tabla de multiplicar: "))
if N <= 0:
    print ("Por favor, ingrese un número válido: positivo mayor que cero.")
else:
    contador = 0
    while contador <= 15:
        M = N * contador
        print (f"{N} x {contador} = {M}")
        contador += 1 


