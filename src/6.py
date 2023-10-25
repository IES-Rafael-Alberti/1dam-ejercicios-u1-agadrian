importe = float(input("Introduzca importe final: "))

sinIva = (importe / 1.10)
ivaPagado = importe - sinIva

print("Precio sin iva: ", sinIva, "\n", "IVA pagado:", ivaPagado)