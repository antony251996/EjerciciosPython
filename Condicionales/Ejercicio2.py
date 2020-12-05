#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

password = 'AntonyCa11148596'

password_input == intput('Ingresa la contraseña: ')

if password.lower() == password_input.lower():
    print('Contraseña correcta!')
else:
    print('Contrase incorrecta!')