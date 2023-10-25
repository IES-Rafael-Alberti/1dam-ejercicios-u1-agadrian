'''
# Ejercicio 1.36 - Calcula la media de las notas de un curso.
# Píde el número de notas que va a introducir al principio.
# El número de notas no puede ser un número superior a 100, o inferior a 1.
# Si no introduce un número de notas correcto escribimos el mensaje "Error - el número de notas debe ser un número entero entre 1 y 100"
#

> ¿Cuántas notas vas a introducir? 0
> Error - el número de notas debe ser un número entero entre 1 y 100
> ¿Cuántas notas vas a introducir? 187
> Error - el número de notas debe ser un número entero entre 1 y 100
> ¿Cuántas notas vas a introducir? 3
> Dame las 3 notas del curso:
> 9
> 7.5
> 10
> La media es 8.83

Inicio

	Escribe "¿Cuántas notas vas a introducir? "
	Lee total
	
	Mientras (total < 1 o total > 100) hacer
		Escribe "Error - el número de notas debe ser un número entero entre 1 y 100"
		Escribe "¿Cuántas notas vas a introducir? "
		Lee total

	Escribe "Dame las " + total + " notas del curso: "
	
	media = 0
	cont = 1
	Mientras (cont <= 10) hacer
		Lee nota
		media = media + nota
		cont = cont + 1

	media = media / total
	Escribe "La media es " + media
	
Fin
'''

numnotas = int(input("Introduce cuantas notas vas a intriducir: \n"))

while (numnotas < 0) and (numnotas > 100):
    print("Error - el número de notas debe ser un número entero entre 1 y 100")
    numnotas = int(input("Introduce cuantas notas vas a introducir: \n"))

print(f"Dame las {numnotas} notas del curso: \n")

cont = 0
sumanotas = 0
while cont < numnotas:
    nota = int(input("Dame nota: \n"))
    sumanotas = nota + sumanotas
    cont += 1

print(f"Tu nota media es de: ", round((sumanotas/numnotas),2))


