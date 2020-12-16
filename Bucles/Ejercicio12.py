# Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.


frase = input('Ingrese una frase: ')
letra = input('Ingrese la letra a consultar: ')
cont = 0

for i in frase:
    if letra == i:
        cont += 1

print(f'La letra {letra} se repite {cont} veces')