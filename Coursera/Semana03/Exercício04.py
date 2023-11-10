# Receber um número inteiro na entrada
numero = int(input("Digite um número inteiro: "))

# Verificar se o número é divisível por 3 e 5
if numero % 3 == 0 and numero % 5 == 0:
    print("FizzBuzz")
else:
    print(numero)
