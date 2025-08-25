# Ejercicio 2
numero = int(input("Ingrese un número entero para saber si es par o impar: "))
residuo = numero % 2
# Si el residuo es cero, el número es par. Sino, es impar.
if residuo == 0:
    print (numero, "es un número par")
else:
    print (numero, "es un número impar")