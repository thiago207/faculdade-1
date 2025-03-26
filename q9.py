while True: 
    r1 = float(input('Resistor 1: '))
    r2 = float(input('Resistor 2: '))
    r3 = float(input('Resistor 3: '))
    if r1 > 0 and r2 > 0 and r3 > 0:
        pode = True
        re = 1 /( (1 / r1) + ( 1 / r2) + ( 1 / r3) )
        print(f'A resistencia é {re:.2f}')
    else:
        print('Os valores nao pode ser 0, tente novamente..')
        pode = False
    if pode:
        break
    
