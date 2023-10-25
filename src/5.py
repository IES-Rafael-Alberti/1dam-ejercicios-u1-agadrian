importe = float(input("Introduzca importe sin IVA: "))
iva = float(input("IVA a aplicar: "))

print("Precio final:", importe + (importe * (iva / 100)))