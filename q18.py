municipios = []
temperaturas = []
for c in range (5):
    municipios.append(str(input('MUNICIPIOS: ')))
    temperaturas.append(int(input('TEMPERATURA: ')))
media = sum(temperaturas) / 5
print('-'*40)
print(f'MEDIA DE TEMPERATURA: {media}')
print('-'*40)
print(' ')
print('-'*40)
print(f'TEMPERATURAS ABAIXO DE DE 10C: ')
print('-'*40)
for c in range(5):
    if temperaturas[c] < 10:
        print(f'{municipios[c]} - {temperaturas[c]}C')
    
print(' ')
print('-'*40)
print(f'TEMPERATURAS ACIMA DE DE 30C: ')
print('-'*40)
for c in range(5):
    if temperaturas[c] > 30:
        print(f'{municipios[c]} - {temperaturas[c]}C')
    