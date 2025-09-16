# Programación – 30893.
## Reto Unidad 3. 
## Menú Interactivo de Problemas Aeronáuticos.
### Estudiantes: 
+ David Piedrahita Valencia – 000577196
+ Sebastián Pulgarín Castrillón – 000577197
---
### Descripción General.
Como estudiantes de primer año de Ingeniería Aeronáutica, nuestro reto es diseñar un programa interactivo en Python que funcione completamente por consola y contenga un menú principal con cuatro opciones:
+ Opción 1: Problema propuesto.
+ Opción 2: Problema propuesto.
+ Opción 3: Problema propuesto.
+ Salir del programa.

Las primeras tres opciones serán problemas relacionados con conceptos aeronáuticos generales, fuerzas sobre el avión, conceptos de vuelo, etc.
El menú debe repetirse hasta que el usuario elija salir.

### Opción 1.
**Problema propuesto:** Control de presión en los neumáticos de una aeronave.
En el mantenimiento de aeronaves, uno de los parámetros críticos para garantizar la seguridad en el rodaje, despegue y aterrizaje es la presión de los neumáticos del tren de aterrizaje. Cada neumático debe estar inflado con nitrógeno (N₂) a una presión específica, medida en libras por pulgada cuadrada (psi), de acuerdo con los estándares establecidos por el fabricante.
El objetivo de este problema es desarrollar un programa en Python que, conociendo inicialmente:
1.	El número total de llantas de una aeronave (tren principal y tren de nariz).
2.	La presión estándar que cada neumático debe alcanzar para estar en condiciones de vuelo.
3.	La presión actual de cada neumático ingresada por el usuario.
El prograba será capaz de determinar:
+	Cuánto nitrógeno debe agregarse o retirarse en cada llanta para alcanzar el estándar.
+	Una alerta si la presión de un neumático aún no cumple con el valor requerido.
+	Un reporte final indicando qué llantas cumplen con la presión adecuada y cuáles requieren ajuste.
Para la implementación se usarán:
+	Bucles (while o for) para recorrer todas las llantas y verificar su presión actual.
+	Condicionales (if-elif-else) para determinar si se debe inflar, desinflar o si la presión es correcta.
+	Funciones que organicen el código, por ejemplo:
    +	Una función para solicitar y validar la entrada de datos del usuario.
    + Una función que calcule la diferencia entre la presión actual y la presión estándar.
    + Una función que genere el reporte final con los resultados.
+ Mensajes dinámicos que indiquen claramente, por ejemplo:
    + "Llanta #3: agregar 12 psi de N₂"
    + "Llanta #5: retirar 5 psi de N₂"
    + "Llanta #1: presión adecuada ✅"

De esta forma, el programa simulará una revisión técnica en línea de vuelo, en la cual el ingeniero aeronáutico puede verificar rápidamente la condición de los neumáticos antes de autorizar la aeronave para operaciones seguras.

### Tabla de Análisis.

| Variable       | Tipo (Entrada/Salida/Control) | Tipo de Variable en Python | Descripción |
|----------------|-------------------------------|----------------------------|-------------|
| TOL            | Control                       | float                      | Define la tolerancia permitida de diferencia entre la presión estándar y la actual de cada llanta. |
| NLL            | Entrada                       | int                        | Número total de llantas de la aeronave (incluye tren principal y tren de nariz). |
| PE             | Entrada/Control               | float                      | Presión estándar que debe alcanzar cada neumático (en psi). |
| PA             | Entrada                       | float                      | Presión actual de cada neumático ingresada por el usuario (en psi). |
| NIT            | Salida                        | float                      | Diferencia entre la presión estándar y la actual. Positivo = inflar, Negativo = desinflar. |
| Cuenta_OK      | Control/Salida                | int                        | Contador de llantas que cumplen con la presión adecuada. |
| Cuenta_Agregar | Control/Salida                | int                        | Contador de llantas que requieren inflado (agregar presión). |
| Cuenta_Retirar | Control/Salida                | int                        | Contador de llantas que requieren desinflado (retirar presión). |
| VCT            | Entrada/Control               | str                        | Variable de confirmación para validar si las presiones ingresadas son correctas (1 o 0). |
| RA             | Entrada/Control               | str                        | Respuesta del usuario para decidir si desea realizar un ajuste en las presiones. |
| RA2            | Entrada/Control               | str                        | Respuesta del usuario para decidir si mostrar o no el reporte final. |
| Seguir         | Control                       | bool                       | Controla si continuar pidiendo las presiones de cada llanta. |
| Seguir2        | Control                       | bool                       | Controla la repetición del bloque de ingreso y validación de datos. |
| RT             | Control                       | bool                       | Controla si repetir todo el proceso desde el inicio. |


### Variables que actúan como constantes

| Variable | Tipo | Descripción | 
|----------|------|-------------|
| TOL | Constante | Define la tolerancia permitida de diferencia entre la presión estándar y la actual de cada llanta. |
| NLL | Constante | Es el número de llantas de la aeronave. A partir de ellas se derivan acciones en el pseudocódigo, como por ejemplo, definir cuántas veces se pregunta por la presión en cada llanta. | 
| PE | Constante | Es la presión estándar que debe tener cada llanta. Es una variable de control porque a partir de ella se definen: cálculos, mensajes, reportes y procedimientos en el pseudocódigo. |



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

### Prueba de escritorio.

---

**Parámetros iniciales.**
- `TOL = 0.5` psi

---

**Entradas simuladas.**
1. **NLL**: primero `0` → error; luego `4` → aceptado (`NLL = 4`)
2. **PE**: primero `-10` → error; luego `200` → aceptado (`PE = 200.00` psi)

---

**Estado inicial de contadores.**
- `Cuenta_OK = 0`
- `Cuenta_Agregar = 0`
- `Cuenta_Retirar = 0`

---

**Ejecución llanta por llanta.**

| Llanta (i) | Entradas del usuario (confirmaciones incluidas) | PA final (psi) | NIT = PE - PA | Decisión inicial | Reingreso | Resultado final | Cambios en contadores |
|------------|--------------------------------------------------|----------------|---------------|------------------|-----------|-----------------|-----------------------|
| 1 | Ingresa `198.00`, confirma (VCT=1). | 198.00 | 2.00 | `NIT > TOL` → agregar 2.00 psi | RA = "N" | Requiere inflado | `Cuenta_Agregar = 1` |
| 2 | Ingresa `200.30`, confirma (VCT=1). | 200.30 | -0.30 | Dentro de tolerancia | — | Adecuada ✅ | `Cuenta_OK = 1` |
| 3 | Ingresa `203.00`, confirma (VCT=1). | 203.00 | -3.00 | `NIT < -TOL` → retirar 3.00 psi | RA2 = "S", reingresa `200.50` | Ajustada, ahora adecuada ✅ | `Cuenta_Retirar = 0`, `Cuenta_OK = 2` |
| 4 | Ingresa `-5.00` → error, luego `199.80`, confirma (VCT=1). | 199.80 | 0.20 | Dentro de tolerancia | — | Adecuada ✅ | `Cuenta_OK = 3` |

---

**Salida en consola (resumen).**
+ Llantas con presión adecuada: 3
+ Llantas que requieren inflado: 1
+ Llantas que requieren desinflado: 0


---

**Resultado final de variables.**
- `Cuenta_OK = 3`
- `Cuenta_Agregar = 1`
- `Cuenta_Retirar = 0`
- `NLL = 4`
- `PE = 200.00`

---

### Opción 2.
**Problema propuesto:** Pesaje y centro de gravedad de una aeronave.
En el marco de los procedimientos establecidos en la ATA 08 – Leveling & Weighing, el pesaje de una aeronave es una tarea fundamental para garantizar que su masa total y su centro de gravedad (CG) estén dentro de los límites operacionales certificados. Estos parámetros influyen directamente en la estabilidad, control y eficiencia del vuelo.
El objetivo de este problema es desarrollar un programa en Python que permita calcular el peso total y el centro de gravedad de una aeronave a partir de los datos ingresados por el usuario.
El programa debe recibir:
1.	La cantidad de puntos de apoyo o básculas (generalmente tren de nariz y tren principal izquierdo/derecho).
2.	El peso medido en cada punto de apoyo.
3.	La distancia (brazo de momento) de cada báscula respecto a un datum de referencia (una línea fija definida por el fabricante).
El programa debe calcular:
+	El peso total de la aeronave como la suma de todos los apoyos.
+	El momento total, multiplicando cada peso por su respectivo brazo.
+	La posición del centro de gravedad (CG), dividiendo el momento total entre el peso total.
+	Una verificación para determinar si el CG está dentro del rango permitido para la aeronave.
Para la implementación se recomienda:
+	Bucles (for) para recorrer todos los apoyos y acumular el peso total y el momento total.
+	Condicionales (if-else) para verificar si el CG calculado está dentro de los límites de seguridad definidos (que pueden pedirse como datos al usuario o predefinirse en el programa).
+	Funciones que dividan el problema en partes:
    +	Cálculo del peso total.
    + Cálculo del momento total.
    + Cálculo y verificación del CG.
+ Mensajes claros para el usuario, por ejemplo:
    + "Peso total de la aeronave: 52,300 lb"
    + "Centro de gravedad calculado: 492 in respecto al datum"
    + "Resultado: El CG está dentro del rango permitido ✅"
    + "Advertencia: El CG está fuera de límites ❌"
    
Este ejercicio permitirá simular un procedimiento de nivelación y pesaje real, tal como lo establece la ATA 08, y entender la importancia del cálculo del centro de gravedad en la seguridad y rendimiento aeronáutico.

### Tabla de análisis.

La siguiente tabla de análisis permite identificar las variables que se usarán tanto en el desarrollo del pseudocódigo como en el lenguaje de programación Phyton para dar solución al problema propuesto. 

| Variable | Tipo (Entrada/Salida/Control) | Tipo de variable en Phyton | Descripción |
| -------- | ----------------- | -------------- | ---------- |
| MDL | Entrada | str | Modelo de la aeronave. Sirve para el certificado de pesaje. |
| MTCL | Entrada | str | Matrícula. Sirve para el certificado de pesaje.|
| NSRE | Entrada | str | Número de serie. Sirve para el certificado de pesaje. |
| RPCG | Entrada, Control | float | RPCG son las iniciales de "Rango Permitido del Centro de Gravedad". Sirven para determinar si, después de hacer los cálculos respectivos, el CG de la aeronave es apto. | 
| CPA | Entrada | int | Esta variable hace referencia a la cantidad de puntos de apoyo o básculas que se usan en el pesaje y balance de la aeronave. |
| PMPA | Entrada | float | Esta variable se usa para conocer el peso medido en cada uno de los puntos de apoyo o básculas. Se usarán las unidades que sean más beneficiosas. |
| BDM | Entrada | float | BDM es un dato de entrada que el usuario debe ingresar al programa. Hace referencia a la distancia que hay desde el dátum (línea vertical de referencia) hasta cada una de las básculas o puntos de apoyo. Se usa para calular el momento y el centro de gravedad. |
| PTA | Control, Salida | float | Es el peso total de la aeronave. Se calcula como la suma de todos los pesos ingresados anteriormente. |
| MP | Control | float | MP hace referencia al momento particular que ejerce el peso en cada una de las básculas con respecto al dátum. Se calcula multiplicando el peso por la distancia. |
| MT | Control, Salida | float | Es el momento total. Se calcula como la suma de cada uno de los momentos particulares. |
| CG | Control, Salida | float | Hace referencia al centro de gravedad. Su dato se lee como la distancia que hay, en una unidad de medida previamente definida, entre el dátum y el centro de gravedad de la aeronave. | 

-----------------------------------------------------

### Constantes.
A continuación, se muestran particularmente las constantes incluidas en el problema.

| Variable | Tipo | Descripción | 
|----------|------|-------------|
| RPCG | Constante | Se considera una constante porque es el Rango Permitido del Centro de Gravedad. Este no cambia, pues está definido en el manual de la aeronave. |
| CPA | Constante | La cantidad de puntos de apoyo no cambia durante el proceso. | 
| BDM | Constante | El brazo de momento está previamente definido por el fabricante. Es una distancia constante desde dicha referecia a los trenes de aterrizaje de la aeronave (Nose Landing Gear and Main Landing Gear). 
-----------------------------------------------------

### Ecuaciones.

A continuación se define la ecuación principal que se usará para resolver el problema. Solo se menciona la fórmula para calular el CG de la aeronave, pues las demás operaciones son de aritmética básica. (El CG también se puede calcular de forma directa como el momento total dividido el peso total.)

_Fórmula:_

_CG = ( A - ( [N] x [B] / W )) + D_

+ CG: Centro de Gravedad.
+ A: Distancia entre el tren principal y el punto de gateo delantero.
+ N: Peso promedio tren de nariz.
+ B: Distancia entre el tren de nariz y el tren principal.
+ W: Peso total de la aeronave.
+ D: Distancia entre el dátum y el centro del punto de gateo.

### Pseudocódigo.

pseudocódigo de la opción 2:
 
### Pseudocódigo
 
```
Función CALC_CG(MT, PMT):
    CG = MT / PMT
    devolver CG
 
Inicio
    imprimir("Ingrese el modelo de la aeronave:")
    leer MDL
    imprimir("Ingrese la matrícula de la aeronave:")
    leer MTCL
    imprimir("Ingrese el número de serie de la aeronave:")
    leer NSRE
    imprimir("Ingrese la distancia desde el DATUM hasta el punto de apoyo del tren de nariz:")
    leer BDMN
    imprimir("Ingrese la distancia desde el DATUM hasta el punto de apoyo del tren principal:")
    leer BDMP
    imprimir("Ingrese el Rango Permitido del Centro de Gravedad (en distancia desde el datum):")
    leer RPCG
    RPCGmin = RPCG - 1
    RPCGmax = RPCG + 1
    CG_valido = falso
    mientras CG_valido = falso:
        imprimir("Ingrese el peso registrado en el Tren de nariz:")
        leer PMTN
        imprimir("Ingrese el peso registrado en el Tren principal (izquierda):")
        leer PMTPI
        imprimir("Ingrese el peso registrado en el Tren principal (derecha):")
        leer PMTPD
        PMTP = PMTPI + PMTPD
        PMT = PMTP + PMTN
        MPN = PMTN * BDMN
        MPP = PMTP * BDMP
        MT = MPN + MPP
        CG = CALC_CG(MT, PMT)
        si CG > RPCGmin y CG < RPCGmax entonces:
            CG_valido = verdadero
        sino si CG < RPCGmin entonces:
            imprimir("Añada más peso atrás o reduzca adelante e introduzca los nuevos datos")
        sino si CG > RPCGmax entonces:
            imprimir("Añada más peso adelante o reduzca atrás e introduzca los nuevos datos")
    imprimir("El avión ", MDL, " con matrícula ", MTCL, " y número de serie ", NSRE, ", cuenta con un CG a ", CG, " metros del Datum, dato válido para permitir su salida.")
Fin
```
 
 ---

 ### Opción 3: Cálculo de Combustible para Vuelos Diarios de una Aeronave

### 1. Explicación del Problema.

El objetivo es calcular la cantidad de combustible necesario para los vuelos diarios de una aeronave. Este cálculo debe considerar múltiples factores que afectan el consumo de combustible, tales como:

- Número de vuelos programados en el día.
- Distancia de cada vuelo.
- Número de escalas.
- Peso de carga transportada.
- Reservas obligatorias de seguridad.

Estos elementos permiten estimar con precisión el combustible requerido, optimizar costos y garantizar la seguridad operacional.

### 2. Tabla de Análisis de Variables.

| Nombre de la variable         | Tipo       | Tipo de dato | Descripción                                                  |
|------------------------------|------------|--------------|--------------------------------------------------------------|
| vuelos              | Entrada    | Entero       | Número total de vuelos programados en el día                |
|consumo_por_km|Entrada (luego será constante)|Flotante|Cantidad de combustible que gasta el avión por kilómetro recorrido|
|combustible_por_escala|Entrada (luego será constante)|Flotante|Cantidad de combustible que gasta el avión por entrar en escalas|
|combustible_extra_por_peso|Entrada (luego será constante)|Flotante|Cantidad de combustible que gasta el avión por kilogramo extra|
| distancia_vuelo              | Entrada    | Flotante     | Distancia en kilómetros de cada vuelo                        |
| escalas               | Entrada    | Entero       | Número de escalas en cada vuelo    
|combustible_escalas|Salida|Flotante|Combustible necesario para las esclas a realizar|                          |
| peso_carga                   | Entrada    | Flotante     | Peso de la carga en kilogramos. Esta cantidad se obtendrá del problema propuesto anterior                               |
| reserva_seguridad_fija            |Constante | Flotante     | Porcentaje adicional del combustible base por seguridad            |
|limite_peso|Entrada (Esta variable se tomrá del dato que devuelve el programa en el problema anterior "Pesaje y CG")|Flotante|Peso límite para un uso mínimo de combustible, si se supera, el consumo aumenta|
|combustible_peso|Salida|Flotante|Será el cunsumo de combustible por superar el límite de peso|
| combustible_base            | Salida     | Flotante     | Cantidad de combustible estimada para el vuelo               |
|total_vuelo|Salida|flotante|Cantidad de combustible necesario para un vuelo|
| total_dia            | Salida     | Flotante     | Combustible total requerido para todos los vuelos del dia           |
| precio_total           | Entrada    | Flotante     | Precio por litro de combustible en cada vuelo                              |
| precio_total_dia      | Salida     | Flotante     | Costo total del combustible necesario en el día                        |

### 3. Dividir el problema en funciones.

- calcular_combustible_base

- calcular_combustible_escalas

- ajuste_por_peso

- reserva_seguridad

- combustible_total_vuelo 

- calcular_precio_total

### 4. Ejemplos de Mensajes Claros para el Usuario.

- "Ingrese la cantidad de vuelos del día:"
- "Distancia del vuelo número X:"
- "Peso de carga para el vuelo número X:"
- "Número de escalas para el vuelo número X:"
- "Precio por litro de combustible:"

### Pseudocódigo.

pseudocodigo de la opcio 3:
 
### Pseudocódigo
 
```
Inicio
Función calcular_combustible_base(distancia, consumo_por_km):
    combustible_base = distancia * consumo_por_km
    Retornar combustible_base
 
Función calcular_combustible_escalas(escalas, combustible_por_escala):
    Si escalas > 0 Entonces:
        combustible_escalas = escalas * combustible_por_escala
    Sino:
        combustible_escalas = 0
    Retornar combustible_escalas
 
Función ajuste_por_peso(peso_carga, limite_peso, combustible_extra_por_peso, distancia):
    Si peso_carga > limite_peso Entonces:
        combustible_peso = combustible_extra_por_peso * distancia
    Sino:
        combustible_peso = 0
    Retornar combustible_peso
 
Función reserva_seguridad(combustible_base):
    reserva_seguridad_fija = combustible_base * 0.3
    Retornar reserva_seguridad_fija
 
Función combustible_total_vuelo(combustible_base, combustible_escalas, combustible_peso, reserva_seguridad_fija):
    total_vuelo = combustible_base + combustible_escalas + combustible_peso + reserva_seguridad_fija
    Retornar total_vuelo
 
Función calcular_precio_total(total_vuelo, precio_por_litro):
    precio_total = total_vuelo * precio_por_litro
    Retornar precio_total
 
Inicio
    imprimir("Ingrese la cantidad de vuelos que realizará el día de hoy el avión:")
    leer(vuelos)
    imprimir("Ingrese la cantidad de litros de combustible que consume el avión por kilómetro:")
    leer(consumo_por_km)
    imprimir("Ingrese la cantidad de litros de combustible que consume el avión por escala:")
    leer(combustible_por_escala)
    imprimir("Ingrese la cantidad de litros de combustible que consume el avión por superar el límite de peso, por kilometro:")
    leer(combustible_extra_por_peso)
    imprimir("Ingrese el peso máximo que puede cargar el avión:")
    leer(limite_peso)
    imprimir("Ingrese el coste del combustible por litro (Dólares):")
    leer(precio_por_litro)
    total_dia = 0
    precio_total_dia = 0
    para i = 1 hasta vuelos hacer:
        imprimir("Vuelo número " + i)
        imprimir("Ingrese la distancia del vuelo (Km):")
        leer(distancia)
        imprimir("Ingrese las escalas del vuelo:")
        leer(escalas)
        imprimir("Ingrese el peso de la carga del avión:")
        leer(peso_carga)
        combustible_base = calcular_combustible_base(distancia, consumo_por_km)
        combustible_escalas = calcular_combustible_escalas(escalas, combustible_por_escala)
        combustible_peso = ajuste_por_peso(peso_carga, limite_peso, combustible_extra_por_peso, distancia)
        reserva_seguridad_fija = reserva_seguridad(combustible_base)
        total_vuelo = combustible_total_vuelo(combustible_base, combustible_escalas, combustible_peso, reserva_seguridad_fija)
        precio_total = calcular_precio_total(total_vuelo, precio_por_litro)
        imprimir("El combustible necesario para el vuelo es: " + total_vuelo + "L")
        imprimir("El costo para este vuelo es: $" + precio_total)
        total_dia = total_dia + total_vuelo
        precio_total_dia = precio_total_dia + precio_total
    imprimir("El combustible que esta aeronave gastará en el día es: " + total_dia + "L")
    imprimir("El costo de combustible para todas las operaciones es: $" + precio_total_dia)
Fin
```    
 





