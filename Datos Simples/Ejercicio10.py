#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.

PESO_PAYASO = 112
PESO_MUÑECA = 75

num_payasos = int(input('Ingrese el numero de payasos: '))
num_muñecas = int(input('Ingrese el numero de muñecas: '))

print(f'El peso final del paquete es de {(PESO_MUÑECA*num_muñecas) + (PESO_PAYASO*num_payasos)}g')