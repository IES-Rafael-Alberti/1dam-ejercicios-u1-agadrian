fecha = input("Introduce fecha en formato(dd/mm/aaaa): \n")

dia, mes, año = fecha.split("/")

if len(dia) == 0:
    dia = "0" + dia # se pondra el 0 delante

if len(mes) == 0:
    mes = "0" + mes

print(f"La fecha introducida es el dia {dia}, mes {mes} y año {año}")

