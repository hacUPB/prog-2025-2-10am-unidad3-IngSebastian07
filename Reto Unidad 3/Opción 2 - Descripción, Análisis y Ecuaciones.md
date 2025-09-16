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