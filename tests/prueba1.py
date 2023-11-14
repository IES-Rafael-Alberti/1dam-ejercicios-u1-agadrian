'''
Desarrolla una función en prueba1.py que reciba dos números y retorne el mayor número de los dos o 0 si son iguales. Realiza las pruebas unitarias y ejecútalas con pytest desde la terminal (puedes hacerlo en la terminal dentro de Visual Studio Code).
'''

def numeroMayor(num1, num2):
    '''
    Lee los dos numeros y te devuelve el mayor, o en caso de ser iguales, 0

    Retorna: float
    '''
    if num1 > num2:
        mayor = num1
    elif num1 < num2:
        mayor = num2
    else:
        mayor = 0

    return mayor


def pedirNumero():

    num = input("Introduce un numero: \n")

    return float(num)


def main():
    resultado = numeroMayor(pedirNumero(), pedirNumero())

    if resultado == 0:
        print("Los numeros son iguales")
    else:
        print("El numero mayor es " + str(resultado))
    



if __name__ == "__main__":
    main()



