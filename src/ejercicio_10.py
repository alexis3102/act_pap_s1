lista = []

print("para frenar el ciclo escribe fin")
while True:
    usuario = (input(">"))
    if ("fin" in usuario) == True:
        break
    
    else:
        lista.append(usuario)
        continue

print("su lista es: ", lista)