# Receber 3 números inteiros na entrada
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
num3 = int(input("Digite o terceiro número inteiro: "))

# Verificar se os números estão em ordem crescente e imprimir a resposta
if num1 < num2 < num3:
    print("crescente")
else:
    print("não está em ordem crescente")
