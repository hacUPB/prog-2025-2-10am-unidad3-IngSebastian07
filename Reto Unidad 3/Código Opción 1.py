
def leer_entero_positivo(prompt):
    while True:
        s = input(prompt).strip()
        try:
            v = int(s)
            if v > 0:
                return v
            print("Error: ingrese un entero positivo.")
        except ValueError:
            print("Error: entrada no válida. Ingrese un número entero.")

def leer_flotante_mayor_cero(prompt):
    while True:
        s = input(prompt).strip()
        try:
            v = float(s)
            if v > 0:
                return v
            print("Error: el valor debe ser mayor que 0.")
        except ValueError:
            print("Error: entrada no válida. Ingrese un número.")

def leer_flotante_no_negativo(prompt):
    while True:
        s = input(prompt).strip()
        try:
            v = float(s)
            if v >= 0:
                return v
            print("Error: la presión no puede ser negativa.")
        except ValueError:
            print("Error: entrada no válida. Ingrese un número (ej. 32.5).")

def main():
    # Parámetros y validación inicial
    TOL = 0.5  # tolerancia en psi (puedes cambiarla)

    while True:  # bucle externo para permitir repetir todo el proceso si el usuario lo desea
        # Leer NLL
        NLL = leer_entero_positivo("Ingrese la cantidad de llantas de la aeronave (entero positivo): ")

        # Leer PE
        PE = leer_flotante_mayor_cero("Ingrese la presión estándar (PE) en psi (valor > 0): ")

        # Inicializar contadores
        Cuenta_OK = 0
        Cuenta_Agregar = 0
        Cuenta_Retirar = 0

        # Proceso llanta por llanta
        for i in range(1, NLL + 1):
            # Leer y confirmar la presión para la llanta i
            while True:
                PA = leer_flotante_no_negativo(f"Ingrese la presión actual (psi) de la llanta #{i}: ")
                # Confirmación
                print(f"Confirmar: la presión ingresada para la llanta #{i} es {PA:0.2f} psi.")
                VCT = input("Seleccione 1 si es correcta, 0 si desea reingresar: ").strip()
                if VCT == "1":
                    break
                elif VCT == "0":
                    print("Reingrese la presión para la llanta.")
                    continue
                else:
                    print("Entrada no válida. Se asumirá que desea reingresar la presión.")

            # Calcular cuánto nitrógeno agregar o retirar
            NIT = PE - PA

            # Decisión según tolerancia
            if NIT > TOL:
                print(f"Llanta #{i}: agregar {NIT:0.2f} psi de N₂")
                Cuenta_Agregar = Cuenta_Agregar + 1

                # Opcional: permitir simular ajuste inmediato y re-evaluar
                RA = input("¿Desea reingresar nueva presión para esta llanta ahora para verificar ajuste? (S/N): ").strip().upper()
                if RA == "S":
                    while True:
                        PA = leer_flotante_no_negativo(f"Ingrese la nueva presión (psi) para la llanta #{i} (o la misma si no la cambió): ")
                        NIT = PE - PA
                        if abs(NIT) <= TOL:
                            print(f"Llanta #{i} ahora está dentro de la tolerancia. ✅")
                            Cuenta_OK = Cuenta_OK + 1
                            Cuenta_Agregar = Cuenta_Agregar - 1
                            break
                        else:
                            print(f"Aún se requiere ajuste de {NIT:0.2f} psi.")
                            Seguir = input("¿Intentar otra vez con esta llanta? (S/N): ").strip().upper()
                            if Seguir != "S":
                                break

            elif NIT < -TOL:
                print(f"Llanta #{i}: retirar {abs(NIT):0.2f} psi de N₂")
                Cuenta_Retirar = Cuenta_Retirar + 1

                RA2 = input("¿Desea reingresar nueva presión para esta llanta ahora para verificar ajuste? (S/N): ").strip().upper()
                if RA2 == "S":
                    while True:
                        PA = leer_flotante_no_negativo(f"Ingrese la nueva presión (psi) para la llanta #{i}: ")
                        NIT = PE - PA
                        if abs(NIT) <= TOL:
                            print(f"Llanta #{i} ahora está dentro de la tolerancia. ✅")
                            Cuenta_OK = Cuenta_OK + 1
                            Cuenta_Retirar = Cuenta_Retirar - 1
                            break
                        else:
                            print(f"Aún se requiere ajuste de {NIT:0.2f} psi.")
                            Seguir2 = input("¿Intentar otra vez con esta llanta? (S/N): ").strip().upper()
                            if Seguir2 != "S":
                                break

            else:
                # Dentro de la tolerancia
                print(f"Llanta #{i}: presión adecuada ✅")
                Cuenta_OK = Cuenta_OK + 1

            print("")  # línea en blanco para separar llantas

        # Resumen final
        print("")
        print("RESUMEN FINAL:")
        print(f"  Llantas con presión adecuada: {Cuenta_OK}")
        print(f"  Llantas que requieren inflado: {Cuenta_Agregar}")
        print(f"  Llantas que requieren desinflado: {Cuenta_Retirar}")
        print("")

        # Preguntar si repetir todo el proceso
        RT = input("¿Desea repetir todo el proceso para volver a ingresar las presiones de todas las llantas? (S/N): ").strip().upper()
        if RT == "S":
            print("Se reiniciará el proceso para todas las llantas.\n")
            continue  # reinicia el bucle externo
        else:
            print("Fin del proceso.")
            break  # sale del bucle externo y termina el programa

if __name__ == "__main__":
    main()
