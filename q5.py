reais = float(input('Preço do produto em real: '))
taxa = float(input('Taxa de conversao: '))
dolar = reais / taxa
print(f'Em dolar: {dolar:.1f}')