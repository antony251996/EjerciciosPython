# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.


tipo_pizzas =  int(input('''Bienvenido a la pizzería Bella Napoli
Elige una opcion:
[1] Pizza vegetariana
[2] Pizza no vegetariana\n'''))

if tipo_pizzas == 1:
    adicional = int(input(''' Elige un adicional
    [1] Pimiento
    [2] Tofu\n'''))
    if adicional == 1:
        print('Elegiste una pizza vegetariana con mozzarella, tomate y pimiento')
    elif adicional == 2:
        print('Elegiste una pizza vegetariana con mozzarella, tomate y tofu')
    else:
        print('Elegiste una opcion que no es correcta!')
    
elif tipo_pizzas == 2:
    adicional = int(input(''' Elige un adicional
    [1] Peperoni
    [2] Jamón
    [3] Salmón\n'''))
    if adicional == 1:
        print('Elegiste una pizza vegetariana con mozzarella, tomate y peperoni')
    elif adicional == 2:
        print('Elegiste una pizza vegetariana con mozzarella, tomate y Jámon')
    elif adicional == 3:
        print('Elegiste una pizza vegetariana con mozzarella, tomate y Salmón')
    else:
        print('Elegiste una opcion que no es correcta!')
else:
    print('Ingresaste una opcion incorrecta')