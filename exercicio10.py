def somar(*numeros):
    acumulador = 0 
    for n in numeros:
        acumulador += n
    return acumulador

numeros = [10, 20, 30]

resultado1 = somar(*numeros)
resultado2 = somar(10, 20, 30)

print(resultado1)







