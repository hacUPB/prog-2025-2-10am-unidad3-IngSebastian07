### Pseudocódigo.

```
INICIO 

# Parámetros (Constantes) y Validación Inicial.

TOL <- 0.5  # Tolerancia en psi
Repetir:
    Escribir "Ingrese la cantidad de llantas de la aeronave (entero positivo):"
    Leer NLL
Hasta que NLL > 0

Repetir:
    Escribir "Ingrese la presión estándar (PE) en psi (valor > 0):"
    Leer PE
Hasta que PE > 0

# Inicializar Contadores.

Cuenta_OK = 0
Cuenta_Agregar = 0
Cuenta_Retirar = 0
```