'''1.1 => recibe un nombre y retorna una cadena de caracteres con el resultado.'''

def saludo(nom):
    return "Hola, " + nom

nombre = input("Nombre: \n")
print(saludo(nombre))