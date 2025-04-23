# Desafio - crie um programa que:
# - Escolhe um número secreto.
# - Pede por um chute do usuário.
# - Indica se o usuário acertou ou não.
# - Se não acertou, dá uma dica, dizendo
#   - se o número é mais alto ou mais baixo.
# - Repete isso até 3 vezes!
import random
numero_secreto = random.randint(0, 10)

    # while
#tentativas = 0
#max_tentativas = 3  # Defina o número máximo de tentativas desejado
#while tentativas < max_tentativas:
#    chute = int(input('Digite um número entre 0 e 10: '))
#    if chute == numero_secreto:
#        print(f'Parabéns, você acertou o número secreto, que é {numero_secreto}!')
#        break
#    elif chute < numero_secreto:
#        print('Chute baixo, o número é maior.')
#    elif chute > numero_secreto:
#        print('Chute alto, o número é menor.')
#    tentativas += 1
#if tentativas == max_tentativas:
#    print(f'Você esgotou suas {max_tentativas} tentativas. O número secreto era {numero_secreto}.')
    
    # For
#acertos = False
#for tentativas in range (3):
#    if not acertos: 
#        chute = int(input('Digite um número entre 0 e 10: '))
#        if chute > numero_secreto:
#            print('Chute alto, o número é menor.')
#        elif chute < numero_secreto:
#            print('Chute baixo, o número é maior.')
#        else:
#            acertos = True
#if acertos:
#    print(f'Parabéns, você acertou o número secreto, que é {numero_secreto}!')
#else:
#    print(f'Você esgotou suas tentativas. O número secreto era {numero_secreto}.')