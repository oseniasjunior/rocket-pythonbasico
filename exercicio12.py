def calcular(**parametros):
    op = parametros.get('operacao', '+')
    v1 = parametros.get('valor1', 0)
    v2 = parametros.get('valor2', 0 if not op == '/' else 1)

    conta = f'{v1} {op} {v2}'

    return eval(conta)

# resultado = calcular(operacao='+', valor1=10, valor2=20)

p = {
    'valor1': 10,
    'valor2': 20,
    'operacao': '+'
}

print(calcular(**p))
