def cuenta_regresiva(n):
    while n > 0:
        yield  n
        n-=1
    #bueno el rol de ese = en n-=1, es que si simplemente es n-1, python hace la operacion pero no tiene donde guardarla, y el ciclo se repite pero no disminuye, pero si le ponemos un = le decimis a python que no solo reste, sino que reste y guarde el resultado en la misma variable, sobreescriba.

respuesta = cuenta_regresiva(10)
print(next(respuesta))
print(next(respuesta))
print(next(respuesta))
print(next(respuesta))
print(next(respuesta))
print(next(respuesta))
print(next(respuesta))
print(next(respuesta))
print(next(respuesta))
print(next(respuesta))