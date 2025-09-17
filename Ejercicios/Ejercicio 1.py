## Ejercicio 1 - Unidad 3

Nombre = input("Ingrese su nombre:")
print ("Bienvenido,", Nombre,".")

#Cálculo Índice de Masa Corporal (IMC)

print ("Para calcular su Índice de Masa Corporal (IMC), se solicitan los siguientes datos")
Peso = input("Ingrese su peso en kilogramos:")
Peso = float(Peso)

Estatura = input("Ingrese su estatura en metros:")
Estatura = float(Estatura)

print ("Los datos ingresados son: Peso =", Peso,"Kg.", "Estatura =", Estatura,"m")
print ("Se calculará su índice de Masa Corporal (IMC) como: Peso [Kg] / (Estatura)^2")

IMC = Peso/(Estatura)**2
IMC = float(IMC)

print (f"Su índice de masa corporal es {IMC:0.2f}")

if IMC >= 40:
    print (f"Paciente {Nombre}, según la OMS, tienes obesidad extrema tipo III.")
else:
    if IMC >= 35:
        print (f"Paciente {Nombre}, según la OMS, tienes obesidad extrema tipo II.")
    else:
        if IMC >= 30:
            print (f"Paciente {Nombre}, según la OMS, tienes obesidad extrema tipo I.")
        else:
            if IMC >= 25:
                print (f"Paciente {Nombre}, según la OMS, tienes sobrepeso.")
            else:
                if IMC >= 18.5:
                    print (f"Paciente {Nombre}, según la OMS, estás en un peso adecuado.")
                else:
                    print (f"Paciente {Nombre}, según la OMS, tienes bajo peso.")
 
