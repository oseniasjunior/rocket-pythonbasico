funcionarios = [
    {'nome': 'OZZY', 'salario': 1000},
    {'nome': 'IZZIE', 'salario': 2000},
]

def fn(item : dict):
    return item.get('salario')

salarios = map(fn, funcionarios)

soma = sum(salarios)

print(soma)



