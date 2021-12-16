frase = input('Digite uma frase ou nome: ')
vogais = ('a', 'e', 'i', 'o', 'u', )
contador_vogais = 0

for f in frase:
    if f.lower() in vogais:
        contador_vogais += 1

print(f'Quantidade de vogais {contador_vogais}')

