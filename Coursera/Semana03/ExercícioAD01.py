# Receber as coordenadas dos dois pontos
x1 = float(input("Digite a coordenada x do primeiro ponto: "))
y1 = float(input("Digite a coordenada y do primeiro ponto: "))
x2 = float(input("Digite a coordenada x do segundo ponto: "))
y2 = float(input("Digite a coordenada y do segundo ponto: "))

# Calcular a distância entre os dois pontos usando a fórmula da distância euclidiana
distancia = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

# Verificar se a distância é maior ou igual a 10 e imprimir a resposta
if distancia >= 10:
    print("longe")
else:
    print("perto")
