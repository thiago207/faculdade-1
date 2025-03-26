
nota = int(input("Digite a nota do aluno (inteira): "))
if nota < 3:
    conceito = "E"
elif 3 <= nota <= 5:
    conceito = "D"
elif 6 <= nota <= 7:
    conceito = "C"
elif 8 <= nota <= 9:
    conceito = "B"
elif nota == 10:
    conceito = "A"
else:
    conceito = "Nota inválida"

print(f"O conceito do aluno é: {conceito}")
