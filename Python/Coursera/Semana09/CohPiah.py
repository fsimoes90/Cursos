import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    ''' Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    soma = 0
    for i in range(len(as_a)):
        soma += abs(as_a[i] - as_b[i])
    
    return soma/6

def calcula_assinatura(texto):
    ''' Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    wal = tamanho_medio_palavras(texto)
    ttr = relacao_type_token(texto)
    hlr = razao_hapax_legomana(texto)
    sal = tamanho_medio_sentenca(texto)
    sac = complexidade_sentenca(texto)
    pal = tamanho_medio_frases(texto)

    return [wal, ttr, hlr, sal, sac, pal]

def avalia_textos(textos, ass_cp):
    ''' Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    as_b = calcula_assinatura(textos[0])
    menor_valor = compara_assinatura(ass_cp,as_b)
    posicao = 0
    for i in range(len(textos)):
        as_b = calcula_assinatura(textos[i])
        correspondencia_ass = compara_assinatura(ass_cp,as_b)
        if correspondencia_ass < menor_valor:
            menor_valor = correspondencia_ass
            posicao = i
    
    return posicao+1

def tamanho_medio_palavras(texto):
    ''' Essa função recebe um texto e retorna o tamanho médio das palavras
        desse texto.
    '''
    soma = 0
    count = 0
    sentencas = separa_sentencas(texto)
    for i in sentencas:
        frases = separa_frases(i)
        for j in frases:
            palavras = separa_palavras(j)
            for k in palavras:
                soma += len(k)
                count += 1

    return soma/count

def relacao_type_token(texto):
    ''' Essa função recebe um texto e retorna o número de palavras
        diferentes dividido pelo total de palavras.
    '''
    
    count = 0
    list_palavras = []
    sentencas = separa_sentencas(texto)
    for i in sentencas:
        frases = separa_frases(i)
        for j in frases:
            palavras = separa_palavras(j)
            for k in palavras:
                list_palavras.append(k)
                count += 1

    return n_palavras_diferentes(list_palavras)/count



def razao_hapax_legomana(texto):
    ''' Essa função recebe um texto e retorna o número de palavras
        utilizadas uma única vez divido pelo número total de palavras.
    '''
    
    count = 0
    list_palavras = []
    sentencas = separa_sentencas(texto)
    for i in sentencas:
        frases = separa_frases(i)
        for j in frases:
            palavras = separa_palavras(j)
            for k in palavras:
                list_palavras.append(k)
                count += 1

    return n_palavras_unicas(list_palavras)/count


def tamanho_medio_sentenca(texto):
    ''' Essa função recebe um texto e retorna o tamanho médio das sentenças
        desse texto.
    '''

    tamanho_sentenca = 0
    sentencas = separa_sentencas(texto)
    qtd_sentencas = len(sentencas)
    for i in sentencas:
        tamanho_sentenca += len(i)

    return tamanho_sentenca/qtd_sentencas

def complexidade_sentenca(texto):
    ''' Essa função recebe um texto e retorna a média da quantidade de 
        frases em cada sentença nesse texto.
    '''
    soma = 0
    qtd_frases = 0
    sentencas = separa_sentencas(texto)
    qtd_sentencas = len(sentencas)
    for i in sentencas:
        frases = separa_frases(i)
        qtd_frases += len(frases)

    return qtd_frases/qtd_sentencas


def tamanho_medio_frases(texto):
    ''' Essa função recebe um texto e retorna o tamanho médio das frases
        desse texto.
    '''
    tamanho_frases = 0
    qtd_frases = 0
    sentencas = separa_sentencas(texto)
    for i in sentencas:
        frases = separa_frases(i)
        qtd_frases += len(frases)
        for j in frases:
            tamanho_frases += len(j)

    return tamanho_frases/qtd_frases


def main():
    ass_a = le_assinatura()
    textos = le_textos()
    infectado = avalia_textos(textos,ass_a)
    print("O autor do texto",infectado,"está infectado com COH-PIAH")