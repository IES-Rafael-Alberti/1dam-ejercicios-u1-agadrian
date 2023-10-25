capital = float(input("Cantidad deposito: "))

ahorro = (capital * (1 + 0.04)) - capital

print(f"Tu ahorro sera: \n- Primer año:", round((ahorro),2), "\n- Segundo año:", round((ahorro*2),2), "\n- Tercer año:", round((ahorro*3),2))

