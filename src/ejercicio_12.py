usuario = int(input("escriba numero: "))
factorial = 1
temp_usuario = usuario  

while temp_usuario > 0:
   
    factorial = factorial * temp_usuario
    
    temp_usuario = temp_usuario - 1

print("El factorial de", usuario, "es:", factorial)
