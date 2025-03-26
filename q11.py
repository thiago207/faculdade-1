horas = int(input('Digite a hora: '))
minuto = int(input('Digite o minuto: '))
segundo = int(input('Digite os segundos: '))
intervalo = (horas * 3600) + (minuto * 60) + segundo
print(f'Seu tempo em segundos foi: {intervalo}')