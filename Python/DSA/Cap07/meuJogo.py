import random
from os import system, name

# Limpa tela
def limpa_tela():
    
    # windows
    if name == 'nt':
        _= system('cls')
        
    # Mac ou Linux
    else:
        _= system('clear')
        
# Função
def game():
    
    limpa_tela()
    
    print('\nBem-vindo(a) ao jogo da forca!')
    print('Adivinhe a palavra abaixo:\n')
    
    # Listas de palavras
    palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']

    # Escolha da palavra randomicamente
    palavra = random.choice(palavras)

    letras_descobertas = ['_' for letra in palavra]

    # Chances
    palavraMultiplicada = palavra*2
    chances = len(palavraMultiplicada)

    # Letras erradas
    letras_erradas = []

    while chances > 0:

        print(''.join(letras_descobertas))
        print('\nChances restantes', chances)
        print('Letras erradas:', ''.join(letras_erradas))

        tentativa = input('\nDigite uma letra:'.lower())

        # Condicional 1 
        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)

        # Condicional 2
        if '_' not in letras_descobertas:
            print('\nVocê venceu, a palavra era:', palavra)
            break
        
    if '_' in letras_descobertas:
        print('\nVocÊ perdeu, a palavra era:', palavra)

if __name__ == "__main__":
    game()
    print('\nParabéns. você está aprendendo Python na DSA')