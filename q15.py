valor = float(input('Qual valor da compra: '))
print('1. Para funcionarios')
print('2. Para clientes especiais')
print('3. Cliente comum')
opcao = int(input('Digite aqui sua opcao: '))
if opcao == 1:
    desconto = valor - (valor * 5 / 100)
    print(f'Valor a ser pago {desconto}')
elif opcao == 2:
    desconto = valor - (valor * 10 / 100)
    print(f'O valor a ser pago é de {desconto}')
else:
    print(f'Valor a ser pago {valor}')