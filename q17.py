clientes = []
valor = []
for c in range (0,5):
    clientes.append(str(input('NOME: ')))
    valor.append(float(input('VALOR DA COMPRA: ')))

total = sum(valor)   
print(f'VALOR TOTAL PAGO PELOS 5 CLIENTES: {total:.2f}')

media = total / 5
print(f'A media de valores das compras {media:.2f}')

print('-'*40)
print('COMPRAS ACIMA DE 20 REAIS: ')
print('-'*40)
for c in range (0,5):
    if valor[c] > 20:
        print(f'{clientes[c]} - R$ {valor[c]}')

print('-'*40)
print('COMPRAS INFERIORES A 50 REAIS: ')
print('-'*40)
for c in range (0,5):
    if valor[c] < 50:
        print(f'{clientes[c]} - R$ {valor[c]}')