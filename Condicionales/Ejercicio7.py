#Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

# Renta	Tipo impositivo
# Menos de 10000€	5%
# Entre 10000€ y 20000€	15%
# Entre 200000€ y 35000€	20%
# Entre 350000€ y 60000€	30%
# Más de 60000€	45%

#Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.

renta_anual = float(input('Ingresa tu renta anual: '))

if renta_anual < 10000:
    print('El tipo impositivo es del 5%')
elif 10000 <=renta_anual < 20000:
    print('El tipo impositivo es del 15%')
elif 20000 <= renta_anual < 35000:
    print('El tipo impositivo es del 20%')
elif 35000 <= renta_anual < 60000:
    print('El tipo impositivo es del 30%')
elif renta_anual >= 60000:
    print('El tipo impositivo es del 45%')
else:
    print('TU renta anual no tiene tipo impositivo')