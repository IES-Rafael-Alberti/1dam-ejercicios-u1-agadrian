peso = float(input("Introduce tu peso(en kg): \n"))
estatura = float(input("Introduce tu estatura(en metros): \n"))

imc = (peso / (estatura**2))

print("Tu índice de masa corporal es: ", round(imc,2))
