#Condicional Simple
#Se le pide al usuario ingresar un número entero. Se mostrará un mensaje si el número es divisible por 3. 

numero = int(input("Ingrese un número entero para saber si es divisible por 3 (si no lo es, no se mostrará nada): "))
residuo = numero % 3

# Si el residuo es cero, el número es divisible por 3.

if residuo == 0:
    print (numero, "es divisible por 3.")
