# Funções puras
# script funcao1.py
valor = 20

def multiplica(fator):
    global valor
    valor = valor * fator
    print("Resultado", valor)

def main():
    numero =int(input())
    multiplica(numero)
    multiplica(numero)
 
# Quando um script python é executado, a variável reservada
# NAME referente a ele tem valor igual à "__main__".
# Nesse caso, a condição do IF a seguir será TRUE,
# então o que está no corpo do IF será executado. 
# No caso, é um chamado ao método main do script
 
if __name__ == "__main__":
    main()

# script funcao2.py
valor = 20

def multiplica(valor, fator):
    valor = valor * fator
    return valor

def main():
    numero = int(input())
    print("Resultado", multiplica(valor, numero))
    print("Resultado", multiplica(valor, numero))

if __name__ == "__main__":
    main()

# Dados imutáveis

# script funcao3.py
# captando os valores do campo Input
valores = input() 
# separando os valores pelo espaço em branco e 
# transformando-os em uma lista de inteiros
valores = [int(i) for i in valores.split()]

def altera_lista(lista):
    lista[2] = lista[2] + 10
    return lista

def main():
    print("Nova lista", altera_lista(valores))
    print("Nova lista", altera_lista(valores))

if __name__ == "__main__":
    main()
    
# script funcao4.py

# captando os valores do campo Input

valores = input()

# separando os valores pelo espaço em branco e

# transformando-os em uma lista de inteiros

valores = [int(i) for i in valores.split()]



def altera_lista(lista):

    nova_lista = list(lista)

    nova_lista[2] = nova_lista[2] + 10

    return lista



def main():

        print("Nova lista", altera_lista(valores))

        print("Nova lista", altera_lista(valores))

if __name__ == "__main__":

        main()
        

