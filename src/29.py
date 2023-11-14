'''Realiza un algoritmo con PSEUDOCÓDIGO y pásalo a un programa en Python que solicite un nombre y una edad.
Si el nombre está vacío, debes utilizar el valor "Desconocido". La edad debe pedirla hasta que introduzca una edad comprendida entre 0 y 125 años.
El programa mostrará la siguiente frase: "Te llamas Pepito y tienes 20 años, te quedan aún 105 años por cumplir".
El pseudocódigo debes incluirlo como comentarios en el programa de Python.'''

'''
Inicio
    Escribe "Introduce nombre y edad"
    Leer nom, edad
    Si (nom == "") entonces
        nom = "Desconocido"
    Mientras (edad < 0) y (edad > 125) hacer
        Escribir "La edad debe estar comprendida entre 0-125 años"
        Leer edad
    Escribir "Te llamas " + nom + " y tienes " + edad + " años, te quedan aun " + (125 - edad) + " por cumplir"
Fin
'''

nom = input("Introduce nombre: \n")
edad = int(input("Introduce edad: \n"))
if nom == '':
    nom = "Desconocido"
while (edad < 0) and (edad > 125):
    print("La edad debe estar comprendida entre 0-125 años")
    edad = int(input("Introduce edad: \n"))
print("Te llamas", nom, "y tienes", edad, "años, te quedan aun", (125 - edad), "por cumplir")
    
