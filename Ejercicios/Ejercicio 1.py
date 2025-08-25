## Ejercicio 1 - Unidad 3

Nombre = input("Ingrese su nombre:")
print ("Bienvenido,", Nombre,".")

#Cálculo Índice de Masa Corporal (IMC)

print ("Para calcular su Índice de Masa Corporal (IMC), se solicitan los siguientes datos")
Peso = input("Ingrese su peso en kilogramos:")
Peso = float(Peso)

Estatura = input("Ingrese su estatura en metros:")
Estatura = float(Estatura)

print ("Los datos ingresados son: Peso =", Peso,"Kg.", "Estarura =", Estatura,"m")
print ("Se calculará su índice de Masa Corporal (IMC) como: Peso [Kg] / (Estatura)^2")

IMC = Peso/(Estatura)**2
IMC = float(IMC)

print ("Su índice de masa corporal (IMC) es:", IMC)


