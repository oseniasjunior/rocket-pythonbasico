from datetime import date, datetime

class Pessoa:
    def __init__(self) -> None:
        self.nome = None
        self.salario = None
        self.data_aniversario = None

    def __str__(self) -> str:
        return f'{self.nome} - {self.salario}'

    @property
    def idade(self):
        agora = datetime.now().date()
        diff = agora - self.data_aniversario
        return int(diff.days / 365)

p1 = Pessoa()
p1.nome = 'Osenias'
p1.salario = 1000
p1.data_aniversario = date(year=1987, month=10, day=28)
print(p1.idade)

p2 = Pessoa()
p2.nome = 'Izzie'
p2.salario = 2000
p2.data_aniversario = date(year=2019, month=3, day=27)


