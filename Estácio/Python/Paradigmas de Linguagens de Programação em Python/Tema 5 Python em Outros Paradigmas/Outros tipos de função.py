# Funções de ordem superior

# script funcao5.py
def multiplicar_por(multiplicador):
    def multi(multiplicando):
        return multiplicando * multiplicador
    return multi

def main():
    multiplicar_por_10 = multiplicar_por(10)
    print(multiplicar_por_10(1))
    print(multiplicar_por_10(2))
 
    multiplicar_por_5 = multiplicar_por(5)
    print(multiplicar_por_5(1))
    print(multiplicar_por_5(2))

if __name__ == "__main__":
    main()

def multi(multiplicando):
    return multiplicando * 10

def multi(multiplicando):
    return multiplicando * 5

# Funções lambda
# Considere a função para multiplicar dois números a seguir:
def multiplicar(a, b):
    return a*b
# A função lambda equivalente é:
lambda a, b: a*b