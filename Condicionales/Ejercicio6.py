#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

sex = input('Ingresa tu sexo (M o F): ')
name = input('Ingresa tu nombre: ')

if sex.upper() == 'F' and name[0].lower() < 'm' or sex.upper() == 'M' and name[0].lower() > 'n':
    print('Pertenece al grupo A')
else:
    print('Pertenece al grupo B')