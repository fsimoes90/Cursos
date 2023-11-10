# Subprogramas
escolha = input("Escolha uma opção de função: 1 ou 2\n")
if escolha == "1":
    def func1(x):
        return x + 1
    s = func1(10)

else:
    def func2(x):
        return x + 2
    s = func2(10)

print(s)

# Parametros
def taximetro(distancia, multiplicador=1):
    largada = 3
    km_rodado = 2
    valor = (largada + distancia * 
    km_rodado) * multiplicador
    return valor

pagamento = taximetro(3.5)
print(pagamento)

# Funções
def func1(x):
    x = 10
    print(f'Função func1 - x = {x}')

def func2(x):
    x = 20
    print(f'Função func2 - x = {x}')

x = 0
func1(x)
func2(x)
print(f'Programa principal - x = {x}')

# Variáveis locais

def func1():
    global x
    x = 10
    print(f'Função func1 - x = {x}')

def func2():
    global x
    x = 20
    print(f'Função func2 - x = {x}')

x = 0
func1()
func2()
print(f'Programa principal - x = {x}')

# Subprogramas aninhados
def taximetro(distancia):
    def calculaMult():
        if distancia < 5:
            return 1.2
        else:
            return 1

    multiplicador = calculaMult()
    largada = 3
    km_rodado = 2
    valor = (largada + distancia * km_rodado) * multiplicador
    return valor

dist = eval(input("Entre com a distancia a ser percorrida em km: \n"))
pagamento = taximetro(dist)
print(f'O valor a pagar é R$ {pagamento}')

# Recursividade
def regressiva(x):
   print(x)
   regressiva(x - 1)
   
def regressiva(x):
   if x <= 0:
        print("Acabou")
#    else:
        print(x)
        regressiva(x-1)
        
# A função recursiva fatorial
def fatorial(n):
    if n == 0 or n == 1:
         return 1
    else:
         return n*fatorial(n-1)
    
def fatorial(n):
    fat = 1
    if n == 0 or n == 1:
        return fat
    else:
        for x in range(2, n + 1):
               fat = fat*x
        return fat
    
#A sequência de Fibonacci
def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)
    
# Documentação de funções – Docstrings
# Docstrings
#Determina o n-ésimo termo da        sequência de Fibonacci
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

print(help(fibo))


