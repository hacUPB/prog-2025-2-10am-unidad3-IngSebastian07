### Pseudocódigo.

```
INICIO 

# Parámetros (Constantes) y Validación Inicial.

TOL = 0.5  # Tolerancia en psi.
Mientras True:
    Escribir "Ingrese la cantidad de llantas de la aeronave (entero positivo):"
    Leer NLL
    Si NLL <= 0:
        Escribir "Error: la cantidad de llantas debe ser mayor a cero. Ingrese nuevamente."
    Si no:
        break
    Fin Si

Mientras True:
    Escribir "Ingrese la presión estándar (PE) en psi (valor > 0):"
    Leer PE
    Si PE <= 0:
        Escribir "Error: la presión debe ser mayor a cero. Ingrese nuevamente."
    Si no:
        break
    Fin Si

# Inicializar Contadores.

Cuenta_OK = 0
Cuenta_Agregar = 0
Cuenta_Retirar = 0

# Proceso llanta por llanta

Para i = 1 hasta i = NLL:
    # Leer y confirmar la presión para la llanta i
    Mientras True:
        Escribir "Ingrese la presión actual (psi) de la llanta #", i, ":"
        Leer Presion_actual
        Si Presion_actual < 0:
            Escribir "Error: la presión no puede ser negativa. Ingrese nuevamente."
        Si no:
            break
        Fin Si
    Mientras True:
        Escribir "Confirmar: la presión ingresada para la llanta #", i, " es: ", Presion_actual, " psi."
        Escribir "Seleccione 1 si es correcta, 0 si desea reingresar:"
        Leer VC_temp
        Si Vc_temp = 1
            break
        Fin Si

# Calcular cuánto nitrógeno agregar o retirar.

NIT = PE - Presion_actual

# Decisión según tolerancia.

Si NIT > TOL:
    Escribir "Llanta #", i, ": agregar ", Redondear(NIT,1), " psi de N₂"
        Cuenta_Agregar = Cuenta_Agregar + 1
    
    # Permitir simular ajuste inmediato y re-evaluar.

    Escribir "¿Desea reingresar nueva presión para esta llanta ahora para verificar ajuste? (S/N):"
    Leer respAjuste
    Si convertir_a_mayusculas(respAjuste) = "S":
        Mientras True:
             True:
            Escribir "Ingrese la nueva presión (psi) para la llanta #", i, " (o la misma si no la cambió):"
            Leer Presion_actual
            Si Presion_actual < 0 Entonces
                Escribir "Error: valor negativo. Intente de nuevo."
            Si no:
                break
            Fin Si
            NIT = PE - Presion_actual
            Si Abs(NIT) = TOL:
                Escribir "Llanta #", i, " ahora está dentro de la tolerancia. ✅"
                # Corregir Contadores.
                Cuenta_OK = Cuenta_OK + 1
                Cuenta_Agregar = Cuenta_Agregar - 1
            Si no:
                Escribir "Aún se requiere ajuste de ", Redondear(NIT,1), " psi."
                Escribir "¿Intentar otra vez con esta llanta? (S/N):"
                Leer seguir
                Si convertir_a_mayusculas(seguir) = "S":
                Escribir "Ingrese la nueva presión (psi) para la llanta #", i, " (o la misma si no la cambió):"
                Leer Presion_actual
                Si Presion_actual < 0:
                    Escribir "Error: valor negativo. Intente de nuevo."
                Si no:
                    break
                Fin Si
            Fin Si

    Fin Si


```