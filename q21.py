
hora_inicio = int(input("Digite a hora de início: "))
minuto_inicio = int(input("Digite os minutos de início: "))


hora_fim = int(input("Digite a hora de término: "))
minuto_fim = int(input("Digite os minutos de término: "))


inicio_em_minutos = hora_inicio * 60 + minuto_inicio
fim_em_minutos = hora_fim * 60 + minuto_fim


if fim_em_minutos < inicio_em_minutos:
    fim_em_minutos += 24 * 60  

duracao_em_minutos = fim_em_minutos - inicio_em_minutos


duracao_horas = duracao_em_minutos // 60
duracao_minutos = duracao_em_minutos % 60


print(f"Duração do jogo: {duracao_horas} horas e {duracao_minutos} minutos")
