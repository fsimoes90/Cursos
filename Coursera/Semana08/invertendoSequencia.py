lista = []
while True:
    valor = int(input("Digite um número: "))
    if valor == 0:
        break
    lista.append(valor)

i = -1
for i in range(-1, (len(lista)*-1)-1, -1):
    print(lista[i])