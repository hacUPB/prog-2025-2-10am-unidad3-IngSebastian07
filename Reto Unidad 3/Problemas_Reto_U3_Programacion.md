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

| Variable | Tipo (Entrada/Salida/Control) | Tipo de Variable en Phyton | Descripción |
|----------|----------|----------|----------|
| NLL | Entrada | int | Esta variable define el número de llantas que tiene en el avión, tanto en el _main landing gear_ como en el _nose landing gear._
| PE | Entrada, Control | float | Esta variable define la presión estándar que cada neumático debe tener (ingresada en psi).  
| PALL | Entrada | float | Esta variable define la presión actual de cada llanta. |
| NIT | Salida | float | Esta variable dará a conocer la cantidad de Nitrógeno (N₂) que se debe agregar (cantidad positiva) o retirar (cantidad negativa) a cada llanta para cumplir con la PE. |
| RF | Entrada | str | Esta variable define un reporte final indicando qué llantas cumplen con la presión adecuada y cuáles requieren ajuste.
| VC | Entrada | int | Esta variable permite definir condiciones falsas o verdaderas.

### Variables que actúan como constantes

| Variable | Tipo | Descripción | 
|----------|------|-------------|
| NLL | Constante | Es el número de llantas de la aeronave. A partir de ellas se derivan acciones en el pseudocódigo, como por ejemplo, definir cuántas veces se pregunta por la presión en cada llanta. | 
| PE | Constante | Es la presión estándar que debe tener cada llanta. Es una variable de control porque a partir de ella se definen: cálculos, mensajes, reportes y procedimientos en el pseudocódigo. |



### Pseudocódigo.

```
INICIO
Escribir "Ingrese la cantidad de llantas de la aeronave (incluya las del *main landing gear* y *nose landing gear*).
Leer NLL
Si NLL <= 0:
    Escribir "Por favor, ingrese un número válido."
Si no:
    Escribir "Ingrese la presión estándar (en psi) que debe tener cada llanta."
    Leer PE
    Si PE <= 0:
        Escribir "Por favor, ingrese un número válido"
    Si no:
        Definir Presion[NLL] como arreglo numérico
        Para i = 1 hasta i = NLL:
            Escribir "Ingrese la presión actual (en psi) de la llanta {i}"
            Leer DATO
            Presion[i] = DATO
            i = i + 1
            Escribir "Las presiones ingresadas son:"
            Para j = 1 hasta j = NLL:
                Escribir "La presión en la llanta {j} es de: {DATO}"
                j = j + 1
            Fin para
            Mostrar "Seleccione 1 si los valores ingresados son correctos, 0 si no lo son."
            Leer VC
            Si VC = 0:
                (Repetir el proceso anterior)
            Si no:
                Si VC = 1
                    Definir Nitrogeno[NLL] como arreglo numérico
                    Para j = 1 hasta j = NLL:
                        NIT = PE - DATO
                    Mientras NIT != 0:
                        Escribir "La llanta {NLL} requiere una presión de {NIT}"
                        Escribir "Ingrese la presión actual (en psi) de la llanta {i}"
                        Leer DATO
                        Presion[i] = DATO
                        i = i + 1
                Si no:
                    Mostrar "Por favor, ingrese una opción válida."
                    Fin para
                Fin si
            Fin si
        Fin para
Escribir "Oprima "R" si desea ver el reporte actual de la presión o "N" si no es así"
Leer RF
Si RF = R:
    Para k = 1 hasta k = NLL:
        Mostrar "El reporte actual de la presión es:"
        Mostrar "La presión en la llanta {k} es de: {DATO}"
    Fin para
Si no:
    Si RF = N:
        Mostrar "No se mostrará el reporte."
    Si no: 
        Mostrar "Por favor, ingrese una opción válida."
    Fin si
Fin si
FIN


            

```
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



