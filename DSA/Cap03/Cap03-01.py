print("Bem-vindo a cauculadora")
num1 = float(input("Insira o primeiro número: "))
num2 = float(input("Insira o segundo número: "))
operador = input('Informe o operador (+, -, /, *): ')
if operador == "+": 
    resultado = num1 + num2
    print("O reultado é: ", resultado) 
elif operador == "-":
    resultado = num1 - num2
    print("O reultado é: ", resultado) 
elif operador == "/":
    resultado = num1 / num2
    print("O reultado é: ", resultado) 
elif operador == "*":
    resultado = num1 * num2
    print("O reultado é: ", resultado) 
else: print("Operação inválida")
    
    