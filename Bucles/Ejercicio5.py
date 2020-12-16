#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

cant = float(input('Ingrese una cantidad a invertir: '))
interes_anual = float(input('Ingrese el interes anual: '))
años = int(input('Ingrese el numero de años a invertir: '))

for i in range(años):
    cant *= 1 + interes_anual / 100
    print(f"Capital tras {años} años: {round(cant,2)}")