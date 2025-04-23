# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random
import os
limpa_tela = os.system('cls')

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

	# Método Construtor
     def __init__(self, palavra):
          self.palavra = palavra
          self.letras_erradas = []
          self.letras_escolhidas = []
          
	# Método para adivinhar a letra
     def guess(self, letra):
          if letra in self.palavra and letra not in self.letras_escolhidas:
               self.letras_escolhidas.append(letra)
          elif letra not in self.palavra and letra not in self.letras_erradas:
               self.letras_erradas.append(letra)
          else:
               return False
          return True
      
	# Método para verificar se o jogo terminou
     def hangman_over(self):
          return self.hangman_won() or (len(self.letras_erradas) == 6 )

	# Método para verificar se o jogador venceu
     def hangman_won(self):
          if '_' not in self.hide_palavra():
               return True
          return False
      
     # Método para não mostrar a letra no board
     def hide_palavra(self):
          rtn = ''
          for letra in self.palavra:
               if letra not in self.letras_escolhidas:
                    rtn += '_'
               else:
                    rtn += letra
          return letra
               
	# Método para checar o status do game e imprimir o board na tela
     def print_game_status(self):
          print(board[len(self.letras_erradas)])
          print(f'\nPalavra: {self.hide_palavra()}')
          print('\nLetras erradas: ',)
          for letra in self.letras_erradas:
               print(letra,)
          print('\nLetras corretas: ',)
          for letra in self.letras_escolhidas:
               print(letra,)

# Método para ler uma palavra de forma aleatória do banco de palavras
def rand_palavra():
     # Lista de palavras
     palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']
     # Escolhe randomicamente as palavas
     palavra = random.choice(palavras)
     return palavra

# Método Main - Execução do programa
def main():
     limpa_tela
     # Cria o objeto e seleciona uma palavra randomica
     game = Hangman(rand_palavra())
     # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a litura do caracter
     while not game.hangman_over():
          # Status do game
          game.print_game_status()
          # Recebe o input
          user_input = input('\nDigite uma letra: ')
          # Verifica se a letra digitada faz parte da palavra
          game.guess(user_input)
     # Verifica o status do jogo
     game.print_game_status()
     # Imprime de acordo com status
     if game.hangman_won():
          print('\nParabéns, você ganhou!')
     else:
          print('\nGame over. Você perdeu!')
          print(f'A palavra era: {game.palavra}')

# Executa o programa
if __name__ == '__main__':
     main()