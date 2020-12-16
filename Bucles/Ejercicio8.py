#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.


num = int(input('Ingrese un numero entero como base: '))

ultimo_valor = 1

for i in range(1,num+1):
    for j in range(ultimo_valor,0,-2):
        print(j, end=' ')
    ultimo_valor += 2
    print(' ')