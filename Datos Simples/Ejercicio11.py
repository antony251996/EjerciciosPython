#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.

INTERES = 0.04
monto = float(input('Ingresa el monto de la cuenta: '))
balance1 =round(monto*(1 + INTERES),2)
balance2 =round(balance1*(1 + INTERES),2)
balance3 =round(balance2*(1 + INTERES),2)
print(f'El primer año es {balance1}, el segundo año es {balance2} y el tercer año es {balance3}')