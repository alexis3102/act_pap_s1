import random
aleatorio = random.randint(1,10)
while True:
    usuario = int(input("adivina el numero: "))
    if (usuario == aleatorio) == True:
        print("felicidades, ganaste")
        break
    elif (usuario == aleatorio) == False:
        print("fallaste intentalo otra vez")
        continue