#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.

PRECIO = 3.49
DESCUENTO = 0.6

barras_nodia = int(input('Ingrese las barras de pan vendidas que no fueron del dia: '))
precio_habitual = barras_nodia * PRECIO
precio_nodia = barras_nodia * PRECIO *(1 - DESCUENTO)

print(f'El precio habitual es {precio_habitual} y el precio a pagar con descuento es {precio_nodia}')
