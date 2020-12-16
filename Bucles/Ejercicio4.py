#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

num = int(input('Ingrese un numero entero positivo: '))

while num >= 0:
    if num == 0:
        print(num)
    else:
        print(num, end=',')
    num -= 1