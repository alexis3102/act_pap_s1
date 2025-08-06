resultado = 0

while True:
    usuario = (int(input("escriba un numero: ")))
    if usuario == 0:
        break
    
    else:
        resultado += usuario
        continue
print("la suma total seria",resultado)