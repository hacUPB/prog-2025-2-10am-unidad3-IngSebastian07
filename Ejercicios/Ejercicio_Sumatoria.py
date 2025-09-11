# Sumatoria de Números.
# El número debde ser natural.
# El usuario no puede continuar si no ingresa un número válido.

N = int(input("Ingrese un número positivo: "))
while N < 0:
    print ("Por favor ingrese un número válido.")
    N = int(input("Ingrese un número positivo: "))
acumulador = 0
for SS in range (1,N+1):
    if SS % 2 == 0:
        acumulador += SS
print (f"La suma de todos los números pares desde 1 hasta {N} es: {acumulador}")