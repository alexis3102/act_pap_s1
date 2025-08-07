usuario = (input("escriba un numero:"))

suma_total = 0


for indice in range(len(usuario)):
    
    digito = usuario[indice]

    suma_total += int(digito)

print("La suma de los dígitos es:", suma_total)