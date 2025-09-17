'''
#Ejercicio 1
numero = 1
while numero <= 99:
    print (numero)
    numero += 2 #numero = numero + 2

#Ejercicio 2
numero = 100
while numero > 0:
    print (numero)
    numero -= 5
'''

#Ejercicio 3
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

while numero1 <= numero2:
    residuo = numero1 % 2
    if residuo == 0:
        print(numero1)
        numero1 = numero1 + 2
    else: 
        numero1 = numero1 + 1
