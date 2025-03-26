peca1 = int(input('Codigo da peça 1: '))
numeros_peca1 = int(input('Numeros de peça 1: '))
valor_unitario1 = float(input('Valor unitario 1: '))

peca2 = int(input('Codigo da peça 2: '))
numeros_peca2 = int(input('Numeros de peça 2: '))
valor_unitario2 = float(input('Valor unitario 2: '))
ipi = float(input('VALOR DA IPI: '))

total_pecas = (numeros_peca1 * valor_unitario1) + (numeros_peca2 + valor_unitario2)

valor_com_ipi = total_pecas + (1 + ipi / 100)

print(f'O valor total com ipí a sert pago é: R$ {valor_com_ipi:.2f}')
