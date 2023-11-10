import os

def somar(num1, num2):
    return num1 + num2

def subtrair(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Erro: Divisão por zero"

def potencia(num1, num2):
    return num1 ** num2

while True:
    os.system("cls")

    print("\n******************* Calculadora em Python *******************")
    print("Operacoes disponiveis:")
    print('1 - Soma')
    print('2 - Subtracao')
    print('3 - Multiplicacao')
    print('4 - Divisao')
    print('5 - Potencia')
    print('6 - Sair')
    escolha = input('Escolha uma operacao (1/2/3/4/5/6): ')

    if escolha == '6':
        print('Calculadora finalizada')
        break
    
    else:

        num1 = float(input('Escolha o primeiro número: '))
        num2 = float(input('Escolha o segundo número: '))

        if escolha == '1':
            resultado = somar(num1, num2)
        elif escolha == '2':
            resultado = subtrair(num1, num2)
        elif escolha == '3':
            resultado = multiplicar(num1, num2)
        elif escolha == '4':
            resultado = dividir(num1, num2)
        elif escolha == '5':
            resultado = potencia(num1, num2)
        else:
            print('Opcao invalida')
            continue

        print('Resultado:', resultado)
        
        print("Deseja fazer outra operação? 1 - SIM, 2 - NÃO")
        refazer = int(input())
        
        while refazer not in [1,2]:
            print("Deseja fazer outra operação? 1 - SIM, 2 - NÃO")
            refazer = int(input())
        if refazer == 2:
            print('Calculadora finalizada')
            break
        else:
            continue