#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés porcentual anual y el número de años, y muestre por pantalla el capital obtenido en la inversión redondeado con dos decimales.

monto = float(input('Ingresa el monto a invertir: '))
interes = float(input('Ingresa el interes anual: '))
años = int(input('Ingresa la cantidad de años a invertir: '))

print(f'El capital obtenido es {round(monto * (interes / 100 + 1) ** años, 2)}')