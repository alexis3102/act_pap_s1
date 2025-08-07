numeros_originales = list(range(1, 29))
numeros_filtrados = []

x = 0

for numero in numeros_originales:
    x=x+1
    if x % 3 != 0:
        numeros_filtrados.append(numero)

print("nuemros filtrados: ")

for numero_final in numeros_filtrados:
    print(numero_final)