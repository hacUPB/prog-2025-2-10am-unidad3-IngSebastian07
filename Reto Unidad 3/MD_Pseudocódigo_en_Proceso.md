### Pseudocódigo.

```
INICIO

# Parámetros y validación inicial.
TOL = 0.5   # Tolerancia en psi.

Mientras True:
    Escribir "Ingrese la cantidad de llantas de la aeronave (entero positivo):"
    Leer NLL
    Si NLL > 0:
        break
    Sino:
        Escribir "Error: ingrese un entero positivo."
Fin Mientras

Mientras True:
    Escribir "Ingrese la presión estándar (PE) en psi (valor > 0):"
    Leer PE
    Si PE > 0:
        break
    Sino:
        Escribir "Error: ingrese un número mayor que 0."
Fin Mientras

# Inicializar contadores.
Cuenta_OK = 0
Cuenta_Agregar = 0
Cuenta_Retirar = 0

# Proceso llanta por llanta.
Para i = 1 Hasta i = NLL Hacer:
    # Leer y confirmar la presión para la llanta i.
    Mientras True:
        Escribir "Ingrese la presión actual (psi) de la llanta #", i, ":"
        Leer PA
        Si PA >= 0:
            # Confirmación
            Escribir "Confirmar: la presión ingresada para la llanta #", i, " es ", PA:0.2f, "psi."
            Escribir "Seleccione 1 si es correcta, 0 si desea reingresar:"
            Leer VCT
            Si VCT = 1:
                break
            Sino:
                Escribir "Reingrese la presión para la llanta #", i, "."
        Sino:
            Escribir "Error: la presión no puede ser negativa. Ingrese nuevamente."
    Fin Mientras

    # Calcular cuánto nitrógeno agregar o retirar.
    NIT = PE - PA

    # Decisión según tolerancia.
    Si NIT > TOL:
        Escribir "Llanta #", i, ": agregar ", NIT:0.2f, "psi de N₂"
        Cuenta_Agregar = Cuenta_Agregar + 1

        # Permitir simular ajuste inmediato y re-evaluar.
        Escribir "¿Desea reingresar nueva presión para esta llanta ahora para verificar ajuste? (S/N):"
        Leer RA
        Si (convertir_a_mayusculas(RA) = "S"):
            Mientras True:
                Escribir "Ingrese la nueva presión (psi) para la llanta #", i, " (o la misma si no la cambió):"
                Leer PA
                Si PA < 0:
                    Escribir "Error: valor negativo. Intente de nuevo."
                    Continuar
                Fin Si
                NIT = PE - PA
                Si Abs(NIT) <= TOL:
                    Escribir "Llanta #", i, " ahora está dentro de la tolerancia. ✅"
                    Cuenta_OK = Cuenta_OK + 1
                    Cuenta_Agregar = Cuenta_Agregar - 1
                    break
                Sino:
                    Escribir "Aún se requiere ajuste de ", NIT:0.2f, "psi."
                    Escribir "¿Intentar otra vez con esta llanta? (S/N):"
                    Leer Seguir
                    Si (convertir_a_mayusculas(Seguir) <> "S"):
                        break
                    Fin Si
                Fin Si
            Fin Mientras
        Fin Si

    Sino Si NIT < -TOL:
        Escribir "Llanta #", i, ": retirar ", Abs(NIT):0.2f, "psi de N₂"
        Cuenta_Retirar = Cuenta_Retirar + 1

        Escribir "¿Desea reingresar nueva presión para esta llanta ahora para verificar ajuste? (S/N):"
        Leer RA2
        Si (convertir_a_mayusculas(RA2) = "S"):
            Mientras True:
                Escribir "Ingrese la nueva presión (psi) para la llanta #", i, ":"
                Leer PA
                Si PA < 0:
                    Escribir "Error: valor negativo. Intente de nuevo."
                    Continuar
                Fin Si
                NIT = PE - PA
                Si Abs(NIT) <= TOL:
                    Escribir "Llanta #", i, " ahora está dentro de la tolerancia. ✅"
                    Cuenta_OK = Cuenta_OK + 1
                    Cuenta_Retirar = Cuenta_Retirar - 1
                    break
                sino:
                    Escribir "Aún se requiere ajuste de ", NIT:0.2f, "psi."
                    Escribir "¿Intentar otra vez con esta llanta? (S/N):"
                    Leer Seguir2
                    Si (convertir_a_mayusculas(Seguir2) <> "S"):
                        break
                    Fin Si
                Fin Si
            Fin Mientras
        Fin Si

    Sino:
        # Dentro de la tolerancia
        Escribir "Llanta #", i, ": presión adecuada ✅"
        Cuenta_OK = Cuenta_OK + 1
    Fin Si

Fin Para

# Resumen final.
Escribir ""
Escribir "RESUMEN FINAL:"
Escribir "  Llantas con presión adecuada: ", Cuenta_OK
Escribir "  Llantas que requieren inflado: ", Cuenta_Agregar
Escribir "  Llantas que requieren desinflado: ", Cuenta_Retirar
Escribir ""

# Preguntar si repetir todo el proceso
Escribir "¿Desea repetir todo el proceso para volver a ingresar las presiones de todas las llantas? (S/N):"
Leer RT
Si (convertir_a_mayusculas(RT) = "S"):
    Escribir "Nota: para repetir, ejecute de nuevo."
Sino:
    Escribir "Fin del proceso."
Fin Si

FIN
```