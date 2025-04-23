numero = input("Digite um número inteiro: ")
tem_adjacente_igual = False

# Verifica dígitos adjacentes iguais
for i in range(len(numero) - 1):
    if numero[i] == numero[i + 1]:
        tem_adjacente_igual = True
        break

if tem_adjacente_igual:
    print("sim")
else:
    print("não")
