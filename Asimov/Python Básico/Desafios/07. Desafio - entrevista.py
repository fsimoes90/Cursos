# Desafio - crie um programa que:
# - Pede pelo seu nome e idade
# - Dá oi para você
# - Conta quantas letras seu nome possui
# - Fala quantos anos você terá daqui a 5 anos

nome  = input('Qual seu nome?:')
Idade = int(input('Qual sua idade?:'))
print(f"Olá {nome}")
print("seu nome tem", len(nome), "Letas.")
print("Daqui 5 anos voce tera", Idade + 5, "Anos.")