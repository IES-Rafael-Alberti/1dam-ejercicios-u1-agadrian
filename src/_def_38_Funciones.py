'''1.2 => recibe horas y coste y retorna el importe total.'''
def importe(hora,coste):
    return "Importe total: " + str(hora*coste)

hora = int(input("Horas: \n"))
coste = int(input("Coste: \n"))

print(importe(hora,coste))