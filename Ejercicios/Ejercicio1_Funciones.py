# Funciones.

# Sección de las funciones.

def suma(a, b):
	resultado = a + b
	return resultado

def resta(N1, N2):
	resultado = N1 - N2
	return resultado

# Sección para el programa principal.
# Llamando a las funciones.

numero1 = 5
numero2 = 3
# Las variables pertenecen al contexto donde fueron creadas.
resultado_suma = suma(numero1, numero2)
print(f"{numero1} + {numero2} = {resultado_suma}")
print(suma(9898,564))
suma(45, 78)

numero3 = 9
numero4 = 3
# Las variables pertenecen al contexto donde fueron creadas.
resultado_resta = resta(numero3, numero4)
print (f"{numero3} - {numero4} = {resultado_resta}")


