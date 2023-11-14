def sumaPositivo(num1, num2):
    if num1 < 0:
        num1 = 0
    if num2 < 0:
        num2 = 0
    return num1 + num2

n1 = int(input("Numero: \n"))
n2 = int(input("Numero: \n"))

print(sumaPositivo(n1, n2))

