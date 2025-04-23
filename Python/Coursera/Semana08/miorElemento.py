def maior_elemento(lista):
    maior = lista[0]
    for numero in lista:
        if numero > maior:
            maior = numero
    return maior
