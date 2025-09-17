from Modulos.Funciones import *

def main():
    while True:
        print ("Bienvenido, este menú le permitirá realizar las siguientes tareas:")
        opcion = int(input("(1) Ajuste de presión en los neumáticos\n(2) Peso, balance y centro de gravedad\n(3) Calculo de combustible\n(4) Salir\nIngrese la opción: "))
        match (opcion):
            case 1:
                print ("Opción seleccionada: Ajuste de presión en los neumáticos.")
                OP1()
            case 2:
                print ("Opción seleccionada: Peso, balance y centro de gravedad.")
                OP2()
            case 3:
                print ("Opción seleccionada: Calculo de combustible.")                
                OP3()
            case 4:
                print ("Saliendo...")
                break
            case _:  
                print ("Opción no válida.")              

if __name__ == "__main__":
    main()