
edad_maxima = 0

print("Ingresa edades una a una. Escribe -1 para terminar.")

while True:
    try:
        edad = int(input("Ingresa una edad: "))
    except ValueError:
        print("Entrada no válida. Por favor, ingresa un número entero.")
        continue

    if edad == -1:
        break

    
    if edad > edad_maxima:
        edad_maxima = edad
        

if edad_maxima > 0:
    print(f"\nLa edad mayor ingresada es: {edad_maxima}")
else:
    print("No se ingresaron edades.")