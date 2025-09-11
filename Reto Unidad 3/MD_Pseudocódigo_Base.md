```
INICIO

// --- Parámetros y validación inicial ---
TOL <- 0.5               // tolerancia en psi (puedes cambiarla)
Repetir:
    Escribir "Ingrese la cantidad de llantas de la aeronave (entero positivo):"
    Leer NLL
Hasta que NLL > 0

Repetir:
    Escribir "Ingrese la presión estándar (PE) en psi (valor > 0):"
    Leer PE
Hasta que PE > 0

// Inicializar contadores
cuenta_ok <- 0
cuenta_agregar <- 0
cuenta_retirar <- 0

// --- Proceso llanta por llanta ---
Para i <- 1 Hasta NLL Hacer
    // Leer y confirmar la presión para la llanta i
    Repetir:
        Escribir "Ingrese la presión actual (psi) de la llanta #", i, ":"
        Leer Presion_actual
        Si Presion_actual < 0 Entonces
            Escribir "Error: la presión no puede ser negativa. Ingrese nuevamente."
            Continuar Repetir
        Fin Si

        Escribir "Confirmar: la presión ingresada para la llanta #", i, " es ", Presion_actual, " psi."
        Escribir "Seleccione 1 si es correcta, 0 si desea reingresar:"
        Leer VC_temp
    Hasta que VC_temp = 1

    // Calcular cuánto nitrógeno agregar o retirar
    NIT <- PE - Presion_actual

    // Decisión según tolerancia
    Si NIT > TOL Entonces
        Escribir "Llanta #", i, ": agregar ", Redondear(NIT,1), " psi de N₂"
        cuenta_agregar <- cuenta_agregar + 1

        // Opcional: permitir simular ajuste inmediato y re-evaluar
        Escribir "¿Desea reingresar nueva presión para esta llanta ahora para verificar ajuste? (S/N):"
        Leer respAjuste
        Si convertir_a_mayusculas(respAjuste) = "S" Entonces
            Repetir:
                Escribir "Ingrese la nueva presión (psi) para la llanta #", i, " (o la misma si no la cambió):"
                Leer Presion_actual
                Si Presion_actual < 0 Entonces
                    Escribir "Error: valor negativo. Intente de nuevo."
                    Continuar Repetir
                Fin Si
                NIT <- PE - Presion_actual
                Si Abs(NIT) <= TOL Entonces
                    Escribir "Llanta #", i, " ahora está dentro de la tolerancia. ✅"
                    cuenta_ok <- cuenta_ok + 1
                    cuenta_agregar <- cuenta_agregar - 1   // corregir contadores
                    Romper
                Sino
                    Escribir "Aún se requiere ajuste de ", Redondear(NIT,1), " psi."
                    Escribir "¿Intentar otra vez con esta llanta? (S/N):"
                    Leer seguir
                    Si convertir_a_mayusculas(seguir) <> "S" Entonces
                        // mantener el estado previo (requiere inflado)
                        Romper
                    Fin Si
                Fin Si
            Hasta que false
        Fin Si

    Sino Si NIT < -TOL Entonces
        Escribir "Llanta #", i, ": retirar ", Redondear(Abs(NIT),1), " psi de N₂"
        cuenta_retirar <- cuenta_retirar + 1

        // Opcional: permitir re-evaluación como en inflado (misma lógica)
        Escribir "¿Desea reingresar nueva presión para esta llanta ahora para verificar ajuste? (S/N):"
        Leer respAjuste2
        Si convertir_a_mayusculas(respAjuste2) = "S" Entonces
            Repetir:
                Escribir "Ingrese la nueva presión (psi) para la llanta #", i, ":"
                Leer Presion_actual
                Si Presion_actual < 0 Entonces
                    Escribir "Error: valor negativo. Intente de nuevo."
                    Continuar Repetir
                Fin Si
                NIT <- PE - Presion_actual
                Si Abs(NIT) <= TOL Entonces
                    Escribir "Llanta #", i, " ahora está dentro de la tolerancia. ✅"
                    cuenta_ok <- cuenta_ok + 1
                    cuenta_retirar <- cuenta_retirar - 1
                    Romper
                Sino
                    Escribir "Aún se requiere ajuste de ", Redondear(NIT,1), " psi."
                    Escribir "¿Intentar otra vez con esta llanta? (S/N):"
                    Leer seguir2
                    Si convertir_a_mayusculas(seguir2) <> "S" Entonces
                        Romper
                    Fin Si
                Fin Si
            Hasta que false
        Fin Si

    Sino
        // Dentro de la tolerancia
        Escribir "Llanta #", i, ": presión adecuada ✅"
        cuenta_ok <- cuenta_ok + 1
    Fin Si

Fin Para

// --- Resumen final ---
Escribir ""
Escribir "RESUMEN FINAL:"
Escribir "  Llantas con presión adecuada: ", cuenta_ok
Escribir "  Llantas que requieren inflado: ", cuenta_agregar
Escribir "  Llantas que requieren desinflado: ", cuenta_retirar
Escribir ""

Escribir "¿Desea repetir todo el proceso para volver a ingresar las presiones de todas las llantas? (S/N):"
Leer repetirTodo
Si convertir_a_mayusculas(repetirTodo) = "S" Entonces
    // Reiniciar contadores y volver a comenzar (puedes implementar con GOTO o envolver todo en un bucle externo)
    // Aquí se asume que el pseudocódigo se coloca dentro de un bucle que repite desde la parte de lectura de presiones.
Fin Si

FIN
```