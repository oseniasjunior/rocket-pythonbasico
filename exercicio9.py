funcionarios = []
soma_mulheres = 0
soma_homens = 0

while True:
    print('1 - Cadastrar funcionário')
    print('2 - Soma do salário dos homens')
    print('3 - Soma do salário das mulheres')
    print('4 - Imprimir a lista dos funcionários')
    print('0 - Sair do programa')

    opcao = int(input('Escolha sua opção: '))

    if opcao == 1:
        nome = input('Digite seu nome: ')
        sexo = input('Digite seu sexo: ')
        salario = float(input('Digite seu salário: '))

        funcionarios.append({'nome': nome, 'sexo': sexo, 'salario': salario})

        if sexo == 'M':
            soma_homens += salario
        else:
            soma_mulheres += salario
    elif opcao == 2:
        print(f'Soma do salário dos homens é {soma_homens}')
    elif opcao == 3:
        print(f'Soma do salário das mulheres é {soma_mulheres}')
    elif opcao == 4:
        print(funcionarios)
    elif opcao == 0:
        break
    else: 
        print('Opção inválida')