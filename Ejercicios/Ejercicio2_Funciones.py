'''
Crear una función llamada menu()
Parámetros de entrada: ninguno
Lo que realiza: muestra un menú y pide al usuario que seleccione una opción.
Valor de retorno: la opción seleccioanda.
'''

# Definiendo la función.

def menu():
    print ("1. ENTRADAS\n2. PLATOS FUERTES\n3. BEBIDAS\n4. POSTRES\n5. SALIR")
    opcion = int(input("Elija una opción:"))
    return opcion

def ENTRADAS():
    print ("1. Patacones\t\tCOP $5,000")
    print ("2. Empanadas\t\tCOP $3,500")
    print ("3. Pandebonos\t\tCOP $3,000")

def PLATOS_FUERTES():
    print ("1. Punta de Anca\t\tCOP $50,000")
    print ("2. Churrasco\t\tCOP $35,000")
    print ("3. Sopa Mexicana\t\tCOP $30,000")

def BEBIDAS():
    print ("3. Té Hatsu\t\tCOP $5,000")
    print ("1. Jugo Natural\t\tCOP $3,000")
    print ("2. Guandolo\t\tCOP $3,000")

def POSTRES():
    print ("2. Pie de Manzana\t\tCOP $9,000")
    print ("1. Postre de Maracuyá\t\tCOP $7,000")
    print ("3. Cupcake tradicional\t\tCOP $5,000")

def SALIR():
    print ("Saliendo del menú.")

# Función principal.

def main ():
    eleccion = menu()
    print (eleccion)

    match (eleccion):
        case 1: 
            ENTRADAS ()
        case 2: 
            PLATOS_FUERTES ()
        case 3: 
            BEBIDAS ()
        case 4:
            POSTRES ()
        case 5: 
            SALIR ()
        case _:
            print ("Opción no válida.")

# Aquí se llama a la función principal.
if __name__ == "__main__":
    main ()