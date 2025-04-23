# Dado duas listas, printe todos os valores que aparecerem
# duplicados nas duas listas.

# Dado duas listas, printe uma mensagem dizendo se existe
# algum elemento em comum entre elas ou não.

valores1 = [2 , 4, 6]
valores2 = [1 , 2, 6, 8]
elemento_em_comum = False

for valor1 in valores1:
    for valor2 in valores2:
        if valor1 == valor2:
            print(f'Valor {valor1} está nas duas listas.')
            elemento_em_comum = True
if elemento_em_comum:
    print(f'As listas possuem elementos em comum')
else:
    print(f'As listas não possuem elementos em comum')
    