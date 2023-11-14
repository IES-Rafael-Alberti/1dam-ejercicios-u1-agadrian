'''1.4 => NO recibe parámetros y retorna la temperatura convertida en grados Celsius. Dentro de la función se pedirá al usuario los grados Farenheit.'''
def farenToCelsius():
    farenheit = float(input("Introduce grados farenheit: \n"))
    celsius = (farenheit - 32) * (5/9)
    return round(celsius,3)

print("Grados celsius: " + str(farenToCelsius()))