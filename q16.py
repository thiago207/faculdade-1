produtos = []
precos = []

for c in range (0,5):
    produtos.append(str(input('Nome do produto: ')))
    precos.append(float(input('Preço do prroduto: R$ ')))
media = sum(precos) / len(produtos)
print('-'*40)
print('Os produtos com preço acima de 20 reais: ')
print('-'*40)

for c in range (0,5):
    if precos[c] > 20:
        print(f'{produtos[c]} - R$ {precos[c]}')

print('-'*40)
print('Os produtos com preço abaixo de 10 reais: ')
print('-'*40)

for c in range (0,5):
    if precos[c] < 10:
        print(f'{produtos[c]} - R$ {precos[c]}')
print('-'*40)
print(f'A media de preços foi de: {media}')
print('-'*40)
print('E os produdos abaixo da media foram: ')
for c in range (0,5):
    if precos[c] < media:
        print(f'{produtos[c]} - R$ {precos[c]}')

