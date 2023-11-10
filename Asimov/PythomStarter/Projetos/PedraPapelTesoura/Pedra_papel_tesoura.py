import random
import os

move_list = ['Papel', 'Pedra', 'Tesoura']
player_count = 0
computer_count = 0

print('Bem vindo ao Pedra, Papel ou Tesoura')

def main_print():
    print('Placar:')
    print('Você: {}'.format(player_count))
    print('Computador: {}'.format(computer_count))
    print('\n')
    print('Escolha sua jogada:')
    print('[1] - Papel\n[2] - Pedra\n[3] - Tesoura')

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def select_move():
    return random.choice(move_list)

def get_player_move():
    while True:
        try:
            player_move = int(input())
            if player_move not in [1, 2, 3]:
                raise Exception("Escolha inválida. Digite 1 para Papel, 2 para Pedra ou 3 para Tesoura.")
            return move_list[player_move - 1]
        except Exception as e:
            print(e)

def select_winner(p_move, c_move):
    global player_count, computer_count

    if p_move == "Papel":
        if c_move == "Pedra":
            player_count += 1
            return "p"
        elif c_move == "Tesoura":
            computer_count += 1
            return "c"
        else:
            return "d"

    if p_move == "Pedra":
        if c_move == "Tesoura":
            player_count += 1
            return "p"
        elif c_move == "Papel":
            computer_count += 1
            return "c"
        else:
            return "d"

    if p_move == "Tesoura":
        if c_move == "Papel":
            player_count += 1
            return "p"
        elif c_move == "Pedra":
            computer_count += 1
            return "c"
        else:
            return "d"

again = 1
while again == 1:
    clear_screen()
    main_print()
    player_move = get_player_move()
    computer_move = select_move()
    winner = select_winner(player_move, computer_move)

    print("Sua jogada: {}".format(player_move))
    print("Jogada do computador: {}".format(computer_move))

    if winner == "p":
        print('Você venceu!')
    elif winner == "c":
        print('Você perdeu!')
    else:
        print('Empate!')
        
    print('Placar:')
    print('Você: {}'.format(player_count))
    print('Computador: {}'.format(computer_count))

    print('Jogar novamente?\n[1] - Sim\n[2] - Não')
    next_game = int(input())
    if next_game == 2:
        again = 0
    elif next_game != 1:
        print('Escolha inválida. Encerrando o jogo.')
        again = 0

clear_screen()