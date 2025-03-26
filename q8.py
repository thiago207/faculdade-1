custo_fabrica = float(input('Qual o custo de fabrica? '))
distribuidor = (custo_fabrica * 28 /100) + custo_fabrica
imposto = (distribuidor * 45 / 100) + distribuidor
print(f'O custo ja com impostos e custos {imposto}')