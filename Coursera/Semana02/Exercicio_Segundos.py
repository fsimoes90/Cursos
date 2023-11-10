# Solicita ao usuário o número de segundos
segundos_totais = int(input("Por favor, entre com o número de segundos que deseja converter: "))

# Calcula os dias, horas, minutos e segundos
dias = segundos_totais // 86400  # 1 dia tem 86400 segundos
segundos_restantes = segundos_totais % 86400
horas = segundos_restantes // 3600  # 1 hora tem 3600 segundos
segundos_restantes %= 3600
minutos = segundos_restantes // 60  # 1 minuto tem 60 segundos
segundos = segundos_restantes % 60

# Formata a saída
saida = f"{dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos."

# Imprime a saída formatada
print(saida)
