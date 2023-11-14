precio = input("Introduce precio producto en euros y dos decimales: \n")

euros, cents = precio.split(".")

print(f"El pruducto cuesta {euros}€ y {cents}cents")