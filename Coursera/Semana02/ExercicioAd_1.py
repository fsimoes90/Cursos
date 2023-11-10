# Solicita ao usuário as informações
nome_cliente = input("Digite o nome do cliente: ")
dia_vencimento = input("Digite o dia de vencimento: ")
mes_vencimento = input("Digite o mês de vencimento: ")
valor_fatura = input("Digite o valor da fatura: ")

# Formata a saída com as informações fornecidas
mensagem = f"Olá, {nome_cliente}"
mensagem += f"\nA sua fatura com vencimento em {dia_vencimento} de {mes_vencimento} no valor de R$ {valor_fatura} está fechada."

# Imprime a mensagem formatada
print(mensagem)
