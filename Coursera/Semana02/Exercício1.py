# Recebendo o valor do lado do quadrado como entrada do usuário
lado = float(input("Digite o valor correspondente ao lado de um quadrado: "))

# Calculando o perímetro (4 vezes o lado) e a área (lado ao quadrado)
perimetro = 4 * lado
area = lado ** 2

# Imprimindo o resultado
print(f"perímetro: {perimetro} - área: {area}")