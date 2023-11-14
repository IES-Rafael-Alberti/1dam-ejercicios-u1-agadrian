'''
# Ejercicio 1.35 - Pide dos números. Después pide un tercer número del 1 al 4, dependiendo de este número el algoritmo debe hacer lo siguiente:
#	
#	- Si no es un número correcto, escribir un mensaje de error.
#	- Si es un 1, escribir la suma de los dos primeros números.
#	- Si es un 2, escribir la resta de los dos primeros números.
#	- Si es un 3, escribir la multiplicación de los dos primeros números.
#	- Si es un 4, escribir la división de los dos primeros números, siempre que el segundo no sea un 0. Si el segundo número es un 0 escribe un mensaje de error "división por cero no es posible".
	
> Introduce dos números:
> 5
> 7
> Introduce una opción (1 = Suma / 2 = Resta / 3 = Multiplicación / 4 = División): 3
> 5 * 7 = 35

> Introduce dos números:
> 8
> 0
> Introduce una opción (1 = Suma / 2 = Resta / 3 = Multiplicación / 4 = División): 4
> La división por cero no es posible

Inicio

	Escribe "Introduce dos números: "
	Lee n1
	Lee n2
	
	opcion = 0
	Mientras (opcion < 1 or opcion > 4) hacer
		Escribe "Introduce una opción (1 = Suma / 2 = Resta / 3 = Multiplicación / 4 = División): "
		Lee opcion
		Si (opcion < 1 or opcion > 4) entonces
			Escribe "Error - No es una opción correcta (1-4)"
	
	Segun (opcion) entonces
		1:
			Escribe n1 + " + " + n2 + " = " + (n1+n2)
		2:
			Escribe n1 + " - " + n2 + " = " + (n1-n2)
		3:
			Escribe n1 + " * " + n2 + " = " + (n1*n2)
		4:
			Si (n2 == 0) entonces
				Escribe "La división por cero no es posible"
			Sino
				Escribe n1 + " / " + n2 + " = " + (n1/n2)
	
Fin4
'''

n1 = int(input("Introduce un numero: \n"))
n2 = int(input("Introduce otro numero: \n"))
opc = int(input("Introduce una opción (1 = Suma / 2 = Resta / 3 = Multiplicación / 4 = División): \n"))


while (opc < 1) or (opc > 4):
    print("Error - La opcion debe ser 1-4: \n")
    opc = int(input("Introduce una opción (1 = Suma / 2 = Resta / 3 = Multiplicación / 4 = División): "))

if opc == 1:
    print(f"La suma de {n1} y {n2} es:", n1 + n2 )
elif opc == 2:
    print(f"La resta de {n1} y {n2} es:", n1 - n2 )
elif opc == 3:
    print(f"La multiplicacion de {n1} y {n2} es:", n1 * n2 )
else:
    print(f"La division de {n1} y {n2} es:", n1 / n2 )

