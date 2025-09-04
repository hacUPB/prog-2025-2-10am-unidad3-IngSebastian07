#Calculadora

control = True #Variable Booleana

while True:
    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))
    print ("S. Sumar\nR. Restar\nM. Multiplicar\nD. Dividir\nP. Potenciar\nE. Salir")
    opcion = input("Elija una opción: ")
    match opcion:
        case "S":
            print ("Suma")
            resultado = numero1 + numero2
        case "R":
            print ("Resta")
            resultado = numero1 - numero2
        case "M":
            print ("Multiplicación")
            resultado = numero1 * numero2
        case "D":
            print ("División")
            if numero2 == 0:
                resultado = "División no definida."
            else:
                resultado = numero1/numero2
        case "P":
            print ("Potenciación.")
            resultado = numero1 ** numero2
        case "E":
            break
        case _:
            print ("Opción no válida.")
    print(f"Resultado = {resultado}")