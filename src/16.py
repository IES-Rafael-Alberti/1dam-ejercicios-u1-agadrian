barrasMalas = int(input("Cuantas barras vendidas no son del dia?: \n"))

pHabitual = 3.49

print(f"El precio habitual por barra es de {pHabitual}. Al no ser fresca se le hace un descuento del 60%; \nel coste total de todas las barras no frescas es de:", round(( ( pHabitual - (pHabitual*0.6) ) * barrasMalas),2))