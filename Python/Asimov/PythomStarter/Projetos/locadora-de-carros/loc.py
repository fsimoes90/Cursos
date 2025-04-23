import os
carros = [
        ('Fiat Uno', 60), 
        ('Fiat Mobi', 70), 
        ('Hyundai HB20', 85), 
        ('Chevrolet Onix', 90), 
        ('Chevrolet Tracker', 120), 
        ('Hyundai Tucson', 120), 
        ('Fiat Pulse', 130),
        ('Chevrolet Spin', 150)
]

alugados = []
def lista_carros(lista_de_carros):
    for i, carros in enumerate(lista_de_carros,1):
        print(f'[{i}] {carros[0]} R${carros[1]} /dia')
        
def Lista_alugados(lista_de_alugados):
    for i, alugados in enumerate(lista_de_alugados,1):
        print(f'[{i}] {alugados[0]}')
        
while True:
#    os.system("cls")
    print("Bem vindo à locadora de carros!")
    print("O que deseja fazer?")
    print("\n[1] - Mostrar portifólio \n[2] - Alugar um carro \n[3] - Devolver um carro \n[4] - Sair")
    op = int(input())
    while op not in [1,2,3,4]:
        print("\nOpção inválida.\n[1] - Mostrar portifólio \n[2] - Alugar um carro \n[3] - Devolver um carro \n[4] - Sair")
    
    
    if op == 1:
        print('Lista dos carros:')
        lista_carros(carros)
    
    elif op == 2:
        print('Lista dos carros:\n')
        lista_carros(carros)
        print('\nEscolha o codigo do carro:')
        escolha = int(input())
        while escolha <= 0 or escolha > len(carros) :
            print("\nOpção inválida, escolha o codigo do carro:")
            escolha = int(input())
        else:
            print('Informe quantos dias de aluguel: ' )
            dias = int(input())
            valor = float(carros[escolha-1][1] * dias)
            conf = (f'Voce escolheu o carro {carros[escolha-1][0]} por R${carros[escolha-1][1]} /dia por {dias} dias')
            conf += (f'\nO valor final da locacao sera de R$ {valor}')
            print(conf)
            print('Confirma o aluguel?\n[1] - Sim\n[2] - Nao')
            conf_alg = int(input())
            while conf_alg not in [1,2]:
                print('Opcao invalida, confirma o aluguel?\n[1] - Sim\n[2] - Nao')
                conf_alg = int(input())
            if conf_alg == 1:
                alugados.append(carros.pop(escolha-1))
                print('Aluguel confirmado!, te aguardamos para a retirada do veiculo.\n')
            else: continue
            
    elif op == 3:
        if len(alugados) == 0:
            print('Voce nao tem carros a devolver!')
            continue
        else:
            print('Lista de carros alugados:\n')
            Lista_alugados(alugados)
            print('Informe o codigo do carro para devolucao:')
            escolha = int(input())
            while escolha <= 0 or escolha > len(alugados):
                print("\nOpção inválida, informe o codigo do carro para devolucao:")
                escolha = int(input())
        print(f'Devolucao escolhida para o carro: {alugados[escolha-1][0]}' )
        print('Estamos te aguardando!\n')
        carros.append(alugados.pop(escolha-1))
        continue
    
    elif op == 4:
        print('Foi um prazer falar com voce. Ate breve!')
        break
        