#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

age = int(input('Ingrese su edad: '))

for i in range(1,age+1):
    if i == 1:
        print(f'Haz cumplido {i} año')
    else:
        print(f'Haz cumplido {i} años')