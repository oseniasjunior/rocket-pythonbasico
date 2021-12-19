class Carro:
    def __init__(self) -> None:
        self.modelo = None
        self.cor = None

    def acelerar(self):
        print(self.cor)

    def __str__(self) -> str:
        return f'{self.modelo} - {self.cor}'


carro1 = Carro()
carro1.modelo = 'Corola'
carro1.cor = 'preto'

print(carro1.modelo)
print(carro1.cor)
print(carro1)