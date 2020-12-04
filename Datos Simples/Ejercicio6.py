#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

horas_trabajadas = float(input('Ingrese el numero de horas trabajadas: '))
coste_hora = float(input('Ingrese el coste por hora: '))
print(f'Le corresponde un pago de {round(horas_trabajadas*coste_hora,2)} por las {horas_trabajadas} horas trabajadas')