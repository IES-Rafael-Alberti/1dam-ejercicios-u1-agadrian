'''1.5 => recibe el importe del artículo sin iva y el tipo de iva a aplicar, pero no retorna nada, sino que se imprime desde dentro de la función.'''
def precio(sinIva, iva):
    precioFinal = sinIva + (sinIva * (iva/100))
    print(f"Precio sin iva: {sinIva}, IVA: {iva}, precio final: {precioFinal}")
    
sinIva = float(input("Precio sin iva: \n"))
iva = float(input("Iva a aplicar: \n"))

precio(sinIva, iva)

