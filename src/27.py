'''Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.'''

nombre = input("Introduce nombre: ")
precio = float(input("Introduce precio: "))
unidades = int(input("Introduce num unidades: "))

print(f"Producto: {nombre}\nPrecio/u:", "{:09.2f}".format(precio),"\nUnidades: " "{:03}".format(unidades), "\nCoste total: {:011.2f}".format((precio*unidades)))
