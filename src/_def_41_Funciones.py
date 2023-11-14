'''1.11 => recibe un número y retorna una cadena de caracteres con el resultado de la función.'''
def resultado(n):
    sumar = (n*(n+1)) / 2
    return str(sumar)

num = int(input("Numero: \n"))
print(resultado(num))