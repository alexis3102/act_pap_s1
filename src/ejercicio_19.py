
frase = "programacion es divertida"
contador_a = 0


for letra in frase:
    
    if letra == 'a' or letra == 'A':
        contador_a += 1


if contador_a > 0:
    print(f"El número total de 'a' y 'A' es: {contador_a}")
else:
    print("No hay 'a' o 'A' en la frase.")
            