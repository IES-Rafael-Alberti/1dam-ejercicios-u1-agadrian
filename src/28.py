'''Realiza un algoritmo con PSEUDOCÓDIGO y pásalo a un programa en Python que lea dos números enteros, muestre cuál es el menor de los dos y cuantos números existen entre ellos dos.
El segundo número no puede ser igual, si es así, debe mostrar el error: "Los números no pueden ser iguales".
Si los números son diferentes, por ejemplo 5 y 12 debe mostrar la frase "El número menor es el 5 y entre ellos existen 7 números enteros".
El pseudocódigo debes incluirlo como comentarios en el programa de Python.'''



'''
Inicio
    Escribe "Introduce dos numeros enteros: "
    Leer n1,n2
    Si (n2 == n1) entonces
        Escribe "Los números no pueden ser iguales"
    Si no
        Si (n1 < n2) entonces
            Escribe "El numero menor es: " + n1 + " y entre ellos hay " + n2 - n1 + " numeros de diferencia"
        Si no
            Escribe "El numero menor es: " + n2 + " y entre ellos hay " + n1 - n2 + " numeros de diferencia"
Fin
'''

n1 = int(input("Introduce un numero entero: \n"))
n2 = int(input("Introduce otro numero entero: \n"))

if n1 == n2:
    print("Los números no pueden ser iguales")
else:
    if n1 < n2:
        print("El numero menor es", n1, "y entre ellos hay", n2 - n1, "numeros de diferencia") 
    if n2 < n1:
        print("El numero menor es", n2, "y entre ellos hay", n1 - n2, "numeros de diferencia") 





