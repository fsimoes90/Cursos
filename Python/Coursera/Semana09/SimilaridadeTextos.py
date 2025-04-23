import re

def le_assinatura():
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")
    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho médio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    return frase.split()

def n_palavras_unicas(lista_palavras):
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
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def calcula_assinatura(texto):
    sentencas = separa_sentencas(texto)
    frases = [separa_frases(sentenca) for sentenca in sentencas]
    palavras = [separa_palavras(frase) for frase in frases]

    num_palavras = sum(len(frase) for frase in palavras)
    num_sentencas = len(sentencas)
    num_frases = sum(len(sentenca) for sentenca in frases)

    tamanho_medio_palavra = num_palavras / num_palavras
    type_token = n_palavras_diferentes([palavra for frase in palavras for palavra in frase]) / num_palavras
    hapax_legomena = n_palavras_unicas([palavra for frase in palavras for palavra in frase]) / num_palavras
    tamanho_medio_sentenca = num_palavras / num_sentencas
    complexidade_sentenca = num_frases / num_sentencas
    tamanho_medio_frase = num_palavras / num_frases

    return [tamanho_medio_palavra, type_token, hapax_legomena, tamanho_medio_sentenca, complexidade_sentenca, tamanho_medio_frase]

def compara_assinatura(as_a, as_b):
    grau_similaridade = 0
    for i in range(6):
        grau_similaridade += abs(as_a[i] - as_b[i])

    return grau_similaridade / 6

def avalia_textos(textos, ass_cp):
    similaridades = [compara_assinatura(calcula_assinatura(texto), ass_cp) for texto in textos]
    indice_texto = similaridades.index(min(similaridades)) + 1

    return indice_texto

if __name__ == "__main__":
    assinatura_cp = le_assinatura()
    textos = le_textos()
    texto_infectado = avalia_textos(textos, assinatura_cp)
    print(f"O autor do texto {texto_infectado} está infectado com COH-PIAH")