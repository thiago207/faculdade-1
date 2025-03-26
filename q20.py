preco_vista = float(input("Digite o preço à vista do produto: R$ "))
parcelas = int(input("Digite o número de parcelas (3 ou 5): "))

if parcelas == 3:
# Acréscimo de 10% para parcelamento em 3 vezes
    preco_total = preco_vista * 1.10
    prestacao_mensal = preco_total / 3
elif parcelas == 5:
# Acréscimo de 20% para parcelamento em 5 vezes
    preco_total = preco_vista * 1.20
    prestacao_mensal = preco_total / 5
else:
    print('digite um valor valido')


print(f"\nPreço total a pagar: R$ {preco_total:.2f}")
print(f"Valor da prestação mensal: R$ {prestacao_mensal:.2f}")
