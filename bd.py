import os

class Funcionario:
    def __init__(self) -> None:
        self.nome = None
        self.salario = None
        self.sexo = None

    def __repr__(self) -> str:
        return f'{self.nome} - {self.salario} - {self.sexo}'

class BancoDados:
    def __init__(self) -> None:
        self.registros = []
        self.listar()

    def salvar(self, funcionario : Funcionario):
        with open('banco.txt', 'a') as arquivo:
            arquivo.write(f'{funcionario.nome}|{funcionario.salario}|{funcionario.sexo}\n')

    def listar(self):
        if os.path.exists('banco.txt'):
            with open('banco.txt', 'r') as arquivo:
                self.registros = [self.transformar(linha) for linha in arquivo.readlines()]

    def transformar(self, linha : str) -> Funcionario:
        campos = linha.split('|')
        funcionario = Funcionario()
        funcionario.nome = campos[0]
        funcionario.salario = float(campos[1])
        funcionario.sexo = campos[2]
        return funcionario
    



