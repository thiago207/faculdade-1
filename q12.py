valor_diaria = float(input('Valor da diaria: '))

valor_promocional = valor_diaria - (valor_diaria * 25 / 100)

valor_total_80 = (75 * 80 / 100) * valor_promocional

valor_total_50_sem_promocao = (75 * 50 / 100) * valor_diaria

diferenca = valor_total_80 - valor_total_50_sem_promocao

print(f'O valor da diaria com a promoçao ficou: {valor_promocional}')

print(f'Valor total arrecado com 80% da ocupaçao e diaria promocional: {valor_total_80}')

print(f'Valor total com 50% de ocupaçao sem promacao {valor_total_50_sem_promocao}')

print(f'A diferença foi de {diferenca}')
