# Serie de Fibonacci.

# Empezamos solicitando al usuario un número entero, que corresponde a la cantidad de valores a mostrar procedentes de dicha serie.
N = int(input("Ingrese un número entero para generar la serie:" ))

# Se verificará si el número ingresado es un número válido (necesariamente debe ser entero y a su vez natural).
if N <= 0:
    print ("Por favor, ingrese un número entero positivo.")
else:
    if N == 1:
        print ("Serie de Fibonacci: 0")
    else:
         # Inicializar los primeros dos términos de la serie.
         a = 0
         b = 1
         cont = 2 # Iniciar en 2 debido a los dos primeros términos ya impresos.

         # Calcular e imprimir los términos restantes.
         
         print("Serie de Fibonacci:", end=" ")
         while cont < N:
            print (a, end= ",")
            sig = a + b
            a = b
            b = sig
            cont += 1
         print ("Fin.")

