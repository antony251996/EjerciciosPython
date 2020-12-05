#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.

dividendo = float(input('Ingresa el dividendo: '))
divisor = float(input('Ingresa el divisor: '))

if divisor == 0:
    print('Error!! el divisor no puede ser 0')
else:
    print(f'La division da {dividendo/divisor}')