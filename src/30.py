''' Realiza un algoritmo con PSEUDOCÓDIGO y pásalo a un programa en Python que pida un número de inicio, un incremento y un total de la serie.
El incremento y el total deben ser mayor que cero, sino el programa debe finalizar con un error u obligar a que introduzcan un valor correcto de ambos (os lo dejo a vuestra elección, la primera opción es más fácil, aunque el mundo está lleno de valientes)
Por ejemplo, si introducen los valores 1, 1 y 10, el programa mostrará en consola exactamente lo siguiente: SERIE => 1-2..3..4..5..6..7..8..9-10
El pseudocódigo debes incluirlo como comentarios en el programa de Python.'''

'''
Inicio
    Escribir "Dime un numero de inicio, uno de incremento, y otro del total de la serie: "
    Leer nInicio, nIncr, nTotal
    Serie = "Serie => " + nInicial + "-"
    cont = 1
    Mientras (cont < nTotal) entonces
        nInicio = nInicio + nIncr
        cont = cont + 1
        Si (cont < (nTotal -1)) entonces
            serie = serie + 1 + ".."
        Si no
            Si (cont == nTotal) entonces
                serie = serie + nInicial
            Si no
                serie = serie + nInicial + "-"
Fin
'''


nInicio = int(input("Introduce numero de inicio: \n"))
nIncr = int(input("Introduce numero de incremento: \n"))
nTotal = int(input("Introduce numero total: \n"))

serie = "Serie => " + str(nInicio) + "-"
cont = 1

while (cont < nTotal):
    nInicio = nInicio + nIncr
    cont = cont + 1
    if cont < (nTotal - 1):
        serie = serie + str(nInicio) + ".."
    else:
        if cont == nTotal:
            serie = serie + str(nInicio)
        else:
            serie = serie + str(nInicio) + "-"
print(serie)
    
