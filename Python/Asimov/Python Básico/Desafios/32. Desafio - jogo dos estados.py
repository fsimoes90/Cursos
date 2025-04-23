import random

estados_e_capitais = {
    'São Paulo': 'São Paulo',
    'Rio de Janeiro': 'Rio de Janeiro',
    'Ceará': 'Fortaleza',
    'Mato Grosso': 'Cuiabá',
    'Minas Gerais': 'Belo Horizonte',
    'Rio Grande do Sul': 'Porto Alegre',
    'Amazonas': 'Manaus',
    'Paraná': 'Curitiba',
    'Pará': 'Belém',
    # ... Preencha com todos os estados aqui!
}

estados = list(estados_e_capitais.keys())
random.shuffle(estados)

quer_continuar = True
rodadas = 0
acertos = 0

for estado in estados:
    if not quer_continuar:
        break

    rodadas += 1
    capital = estados_e_capitais[estado]
    print(f'\n -> Qual a capital do estado {estado}?')

    resposta = input('Sua resposta: ')
    if resposta.lower() == capital.lower():
        print('Resposta correta!')
        acertos += 1
    else:
        print(f'Resposta errada! O correto seria {capital}')

    while True:
        opcao = input('Deseja continuar? (s/n)').lower()
        if opcao not in ['s', 'n']:
            print('Responda apenas com "s" para sim ou "n" para não.')
            continue
        elif opcao == 'n':
            quer_continuar = False
        break

porc = acertos / rodadas * 100

print(f'Você acertou {acertos} de {rodadas}')
print(f'Porcentagem de acertos: {porc:.2f}%')
