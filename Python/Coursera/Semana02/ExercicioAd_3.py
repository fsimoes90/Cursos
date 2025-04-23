# Solicita ao usuário um número inteiro
numero = int(input("Digite um número inteiro: "))

# Calcula o dígito das dezenas usando a operação de divisão inteira e módulo
digito_dezenas = (numero // 10) % 10

# Imprime o resultado
print(f"O dígito das dezenas é {digito_dezenas}")
