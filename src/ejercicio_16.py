contador = 0
print("00:00")
while True:
    contador += 1
    time=(contador >=10 and contador <=59)
    if (time==True):
        print("00:",contador)
    elif (contador < 10)==True:
        print ("00:0",contador)
    else:
        break