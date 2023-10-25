'''Ejercicio 1.32 - Lee dos números y crea la serie que los une de 1 en 1...
#

> Introduce un número: 4
> Introduce otro: 8
> 4-5-6-7-8

> Introduce un número: 12
> Introduce otro: 3
> 3-4-5-6-7-8-9-10-11-12

Inicio

	Escribe "Introduce un número: "
	Lee x
	Escribe "Introduce otro: "
	Lee y
	
	Si (x >= y) entonces
		numIni = x - 1  #si x es mayor que y, no puede ser el numIni el mas grande, o bien habria que darle un step negativo (-1)
		numFin = y
	Sino
		numIni = y - 1
		numFin = x
		
	Para i en (numIni...numFin) hacer
		Escribe i + 
		Si (numIni != numFin) entonces
			Escribe "-"

Fin'''


x = int(input("Introduce un numero: \n"))
y = int(input("Introduce otro numero: \n"))

if (x <= y):  
    numIni = x - 1
    numFin = y
else:
    numIni = y - 1
    numFin = x


for i in range(numIni, numFin):
    print(i+1, end="")
    numIni +=1 #para que en algun momento numIni != numFin
    
    if numIni != numFin:
        print("-",end='')