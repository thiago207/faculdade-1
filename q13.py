numero_estoque = int(input('Numero de itens em estoque: '))
itens_fornecer = int(input('Quantos itens vai fornecer: '))
da = numero_estoque - itens_fornecer
if numero_estoque > itens_fornecer:
    print(f'Novo estoque {da}')
else:
    print(f'Nao a estoque suficiente para atender a nescessidade de itens')