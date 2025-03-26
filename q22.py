
preco_A = float(input("Digite o preço unitário do ovo A (em reais): "))
preco_B = float(input("Digite o preço unitário do ovo B (em reais): "))
preco_C = float(input("Digite o preço unitário do ovo C (em reais): "))

tipo_ovo = input("Digite o tipo de ovo desejado (A, B ou C): ").upper()
quantidade = int(input("Digite a quantidade desejada de ovos: "))

limite_A = 50
limite_B = 30
limite_C = 20

if tipo_ovo == 'A':
    preco_unitario = preco_A
    limite_maximo = limite_A
elif tipo_ovo == 'B':
    preco_unitario = preco_B
    limite_maximo = limite_B
elif tipo_ovo == 'C':
    preco_unitario = preco_C
    limite_maximo = limite_C
else:
    print("Tipo de ovo inválido!")
    exit()

if quantidade > limite_maximo:
    print(f"Pedido não pode ser integralmente atendido. Serão fornecidos apenas {limite_maximo} unidades do ovo {tipo_ovo}.")
    quantidade = limite_maximo

total_reais = preco_unitario * quantidade

taxa_conversao = 5
total_dolares = total_reais / taxa_conversao

print(f"Total a ser pago: R$ {total_reais:.2f}")
print(f"Equivalente em dólares: ${total_dolares:.2f}")
