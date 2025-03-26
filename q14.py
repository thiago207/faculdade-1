while True:
    import math
    print('-=-'*20)
    print('QUAL OPERAÇAO VAI QUERER:')
    print('1. ÁREA DA CIRCUNFERENCIA')
    print('2. PERIMETRO DA CIRCUFERENCIA')
    print('-=-'*20)
    opcao = int(input('Sua Opcao: '))
    if opcao == 1:
        raio = int(input( 'Digite o raio: '))
        area = math.pi * raio ** 2
        print(f'A area é {area:.2f}')
        break
    elif opcao == 2:
        raio = int(input( 'Digite o raio: '))
        perimetro = 2 * math.pi * raio
        print(f'O perimetro é {perimetro:.2f}')
        break
    else:
        print('Insira uma valor opçao valida')
