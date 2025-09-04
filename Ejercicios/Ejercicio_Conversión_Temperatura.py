# Ejercicio 1: Conversor de Temperatura

# Dificultad: Principiante

# Crea un programa que convierta temperaturas entre Celsius y Fahrenheit. El programa debe:

# 1. Preguntar al usuario si desea convertir de Celsius a Fahrenheit (ingresando 'C') o de Fahrenheit a Celsius (ingresando 'F')
# 2. Aceptar un valor de temperatura como entrada
# 3. Realizar la conversión usando la fórmula apropiada
# 4. Continuar pidiendo conversiones hasta que el usuario ingrese 'Q' para salir

# Entrada: Un carácter ('C', 'F', o 'Q') y un valor numérico de temperatura
# Salida: El valor de temperatura convertido con las unidades correspondientes

# VARIABLES DE ENTRADA
# NOMBRE               TIPO
# opcion               str
# temperatura          float

#VARIABLES DE SALIDA
# NOMBRE               TIPO
# conversion           Float

# VARIABLES DE CONTROL
# NOMBRE               TIPO
# opcion 

opcion = 'Z'    # Asigno un valor diferente de Q, sirve para que se cumpla la condición para ingresar al while
while opcion != 'Q': # != Significa diferente
    opcion = input("F. Fahrenheit a Celsius\nC. Celcius a Fahnrenheit\nQ. Salir\n") # Esto define las opciones del menú.
    opcion = opcion.upper() # Sirve para convertir la opción que ingrese e usuario a MAYÚSCULA
    if opcion != 'Q':
        temperatura = float(input("Ingrese la temperatura a convertir: "))
        match opcion: # match sirve para plantear qué pasa en cada opción
            case 'F':
                conversion = (temperatura - 32) * (5/9)
                print (f"{temperatura} °F = {conversion:0.2f} °C") # :0.2f muestra solo dos decimales en el resultado.
            case 'C':
                conversion = (temperatura * 9 / 5) + (32)
                print (f"{temperatura} °C = {conversion:0.2f} °F") # :0.2f muestra solo dos decimales en el resultado.
            case _: # case_: sirve para cuando se ingresa una opción que no está presente en el menú.
                print ("Opción no válida")
    else:
        print ("Saliendo del programa...")
        