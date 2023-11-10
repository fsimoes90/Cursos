# Crie um código que implementa a "Cifra de César", isto é, que
# transforma um string movendo cada letra um certo número de
# passos no alfabeto. O número de passos é dado por uma chave.
# Letra com acentos, espaços e pontuação permanecem iguais.

# Exemplos:
# "abc" com chave 1 = "bcd"
# "ABCDE" com chave 2 = "CDEFG"
# "Cachorro" com chave -1 = "Bzbgnqqn"
# "Olá Mundo!" com chave 3 = "Roá Pxqgr!"

# DICA: construa 2 strings com as letras do alfabeto em ordem,
# um para letra minúsculas e outra para as maiúsculas, e use este
# string para guiar as substituições.

def cifrar_caractere(caractere, seq, chave):
    indice_atual = seq.index(caractere)
    novo_indice = indice_atual + chave
    while novo_indice >= len(seq): # retorna a contagem para o inicio da lista
        novo_indice = novo_indice - len(seq)
    while novo_indice <= len(seq): # retorna a contagem para o final da lista
        novo_indice = novo_indice - len(seq)
        
    return seq[novo_indice]

texto = 'ABCDE'
chave = 2

minusculas = 'abcdefghijklmnopqrstuvwxyz'
maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

cifra  = ''

for caractere in texto:
    if caractere in minusculas:
        caracter_cifra = cifrar_caractere(caractere, minusculas, chave)
    if caractere in maiusculas:
        caracter_cifra = cifrar_caractere(caractere, minusculas, chave)
    else:
        caractere_cifra = caractere
    cifra += caracter_cifra
    
print(cifra)