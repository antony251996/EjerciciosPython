#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.


contraseña = 'contraseña'

correcto = False

while correcto == False:
    password = input('Ingrese un contraseña: ')
    if password.lower() == contraseña.lower():
        print('Contraseña Correcta')
        correcto = True
    else:
        print('Contraseña Incorrecta')