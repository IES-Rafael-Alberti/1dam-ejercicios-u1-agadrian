def factorial(num: int):
    if num <= 1:  # si queremos calcular 0! o 1! , return1 y se acaba la funciion
        return 1
    total = 1
    while num > 1:
        total = total * num
        num = num - 1
    return total

numero = int(input("Numero: \n"))
print(str(numero) + "!: " + str(factorial(numero)))




def factorialStr(num: int):
    '''## 8! => 8x7x6x5x4x3x2x1 = x'''
    resultado = str(num) + "! => " + str(num)
    
    if num <= 1:
        return resultado + "x" + str(num) + " = " + str(num)
    
    multiplicacion = 1
    while num > 1:
        if num > 1:
            resultado = resultado + "x"
        multiplicacion = multiplicacion * num
        num -=1
        resultado = resultado + str(num)
        
    resultadoFinal = resultado + " = " + str(multiplicacion)
    return resultadoFinal

numero = int(input("Numero: \n"))
print(factorialStr(numero))