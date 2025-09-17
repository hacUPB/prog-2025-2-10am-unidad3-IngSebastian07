# Opcion 1

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

def OP1():
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

'''
if __name__ == "__main__":
    main()
'''    
# Opcion 2


def CALC_CG (MT, PMT):
    CG = MT / PMT
    return CG

def OP2 ():
    MDL = input("Ingrese el modelo de la aeronave: ")
    MTCL = input("Ingrese la matrícula de la aeronave: ")
    NSRE = input("Ingrese el número de serie de la aeronave: ")
    BDMN = float(input("Ingrese la distancia desde el DATUM hasta el punto de apoyo del tren de nariz (ft): "))
    BDMP = float(input("Ingrese la distancia desde el DATUM hasta el punto de apoyo del tren principal: "))
    RPCG = float(input("Ingrese el Rango Permitido del Centro de Gravedad (en distancia desde el datum): "))
    RPCGmin = RPCG - 1
    RPCGmax = RPCG + 1
    while True:
        PMTN = float(input("Ingrese el peso registrado en el Tren de nariz (lb): "))
        PMTPI = float(input("Ingrese el peso registrado en el Tren principal (izquierda)): "))
        PMTPD = float(input("Ingrese el peso registrado en el Tren principal (derecha): "))
        PMTP = PMTPI + PMTPD    
        PMT = PMTP + PMTN
        MPN = PMTN * BDMN
        MPP = PMTP * BDMP
        MT = MPN + MPP
        CG = CALC_CG (MT, PMT)
        if RPCGmin < CG < RPCGmax:
            break
        elif CG < RPCGmin: 
            print ("Añada más peso atras o reduzca adelante e introduzca los nuevos datos")
        elif CG > RPCGmax:
            print ("Añada más peso adelante o reduzca atras e introduzca los nuevos datos")
    print (f"El avión {MDL} con matrícula {MTCL} y numero de serie {NSRE}, cuenta con un CG a {CG} metros del Datum, Dato valido para permitir su salida.")

# Opcion 3

def calcular_combustible_base(distancia, consumo_por_mi):
    combustible_base = distancia * consumo_por_mi
    return combustible_base

def calcular_combustible_escalas(escalas, combustible_por_escala):
    if escalas > 0:
        combustible_escalas = escalas * combustible_por_escala
    else:
        combustible_escalas = 0
    return combustible_escalas

def ajuste_por_peso(peso_carga, limite_peso, combustible_extra_por_peso, distancia):
    if peso_carga > limite_peso:
        combustible_peso = combustible_extra_por_peso * distancia
    else:
        combustible_peso = 0
    return combustible_peso

def reserva_seguridad(combustible_base):
    reserva_seguridad_fija = combustible_base * 0.3
    return reserva_seguridad_fija

def combustible_total_vuelo(combustible_base, combustible_escalas, combustible_peso, reserva_seguridad_fija):
    total_vuelo =  combustible_base + combustible_escalas + combustible_peso + reserva_seguridad_fija
    return total_vuelo

def calcular_precio_total(total_vuelo, precio_por_galon):
    precio_total = total_vuelo * precio_por_galon
    return precio_total

def OP3():
    vuelos = int(input("Ingrese la cantidad de vuelos que realizará el día de hoy el avión: "))
    consumo_por_mi = float(input("Ingrese la cantidad de galones de combustible que consume el avión por milla: "))
    combustible_por_escala = float(input("Ingrese la cantidad de galones de combustible que consume el avión por escala: "))
    combustible_extra_por_peso = float(input("Ingrese la cantidad de galones de combustible que consume el avión por superar el límite de peso (por libra), cada milla: "))
    limite_peso = float(input("Ingrese el peso de la carga a partir del cual se consume combustible extra (lb): "))
    precio_por_galon = float(input("Ingrese el coste del combustible por galón (Dólares): "))
    total_dia = 0
    precio_total_dia = 0

    for i in range (1, vuelos+1, 1):
        print (f"\nvuelo número {i}\n")
        distancia = float(input("Ingrese la distancia del vuelo (mi): "))
        escalas = int(input("ingrese las escalas del vuelo: "))
        peso_carga = float(input("Ingrese el peso de la carga del avión (lb): "))
        combustible_base = calcular_combustible_base(distancia, consumo_por_mi)
        combustible_escalas = calcular_combustible_escalas(escalas, combustible_por_escala)
        combustible_peso = ajuste_por_peso(peso_carga, limite_peso, combustible_extra_por_peso, distancia)
        reserva_seguridad_fija = reserva_seguridad(combustible_base)
        total_vuelo = combustible_total_vuelo(combustible_base, combustible_escalas, combustible_peso, reserva_seguridad_fija)
        precio_total = calcular_precio_total(total_vuelo, precio_por_galon)
        print (f"\nEl combustible necesario para el vuelo es: {total_vuelo}Gal . \nEl costo para este vuelo es: ${precio_total}")
        total_dia += total_vuelo
        precio_total_dia += precio_total

    print (f"\n\nEl combustible que esta aeronave gastará en el día es: {total_dia}Gal . \nEl costo de combustible para todas las operaciones es: ${precio_total_dia}")    