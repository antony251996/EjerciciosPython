#Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

age = int(input('Ingresa tu edad: '))
ingresos = float(input('Coloca tus ingresos: '))

if age > 16 and ingresos >= 1000:
    print('Debes tributar')
else:
    print('No debes tributar')