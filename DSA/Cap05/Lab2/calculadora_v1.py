# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

print("\n******************* Calculadora em Python *******************")

# Funções para as operações
def soma(a,b):
    return a+b

def subtracao(a,b):
    return a-b

def multiplicacao(a,b):
    return a*b

def divisao(a,b):
    if b == 0:
        return('Erro: Divisão por zero')
    return a/b

def perguntaNumero(operacao):
    num1 = float(input('Escolha o primeiro número: '))
    num2 = float(input('Escolha o segundo número: '))
    
    if operacao == '1':
        return soma(num1,num2)
    
    elif operacao == '2':
        return subtracao(num1, num2)
    
    elif operacao == '3':
        return multiplicacao(num1, num2)
    
    elif operacao == '4':
        return divisao(num1, num2)
    
    elif operacao == '5':
        return 'Calculadora finalizada'    
    else: 
        return 'Opcao invalida'


print("Operacoes disponiveis")
print('1 - Soma')
print('2 - Subtracao')
print('3 - Multiplicacao')
print('4 - Divisao')
print('5 - Sair')

escolha = input('Escolha uma operacao (1/2/3/4/5): ')
print('Resultado: ',perguntaNumero(escolha))
print('Fim')