# Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.


eco = True

while eco == True:
    palabra = input('Ingrese una palabra: ')
    palabra = palabra.lower()
    if palabra == 'salir':
        eco = False
    else:
        print(palabra)
