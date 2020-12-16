# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

num = int(input('Ingrese un numero entero: '))

cont = 0

for i in range(1,num+1):
    if num % i == 0:
        cont +=1

if num == 1 or cont > 2:
    print('El numero no es primo')
else:
    print('El numero es primo') 