funcionarios = []

while True:
    nome = input('Digite o nome: ')
    sexo = input('Digite o sexo: ')
    salario = float(input('Digite o salário: '))

    funcionarios.append({
        'nome': nome, 
        'salario': salario, 
        'sexo': sexo
    })

    opcao = input('S para continuar: ')

    if not opcao == 'S':
        salarios = [f.get('salario') for f in funcionarios]
        print(salarios)
        print(sum(salarios))
        break