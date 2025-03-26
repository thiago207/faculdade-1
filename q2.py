n1 = float(input('Nota 1: '))
n2 = float(input( 'Nota 2: '))
n3 = float(input('Nota 3: '))
media = (n1 + n2 + n3) / 3
if media >= 9:
    print('Otima nota!')
elif  9 > media >= 7.5:
    print('Boa nota')
elif 7.5 > media >=6:
    print('Na media!')
elif media < 6:
    print('Abaixo')
print(f'{media:.2f}')