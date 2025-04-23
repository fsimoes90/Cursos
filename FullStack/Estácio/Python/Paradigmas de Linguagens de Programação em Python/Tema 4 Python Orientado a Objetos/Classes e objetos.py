# Definição de classe
class Conta:
    pass

# Construtores e self
# 1
class Conta:
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo

def main():
    c1 = Conta(1,1,"Joao",1000) # Objeto sendo instanciado
    print (f"Nome do titular da conta: {c1.nomeTitular}")
    print (f"Número da conta: {c1.numero}")
    print (f"CPF do titular da conta: {c1.cpf}")
    print (f"Saldo da conta: {c1.saldo}")
    

# Quando um script python é executado, a variável reservada
# NAME referente a ele tem valor igual a "__main__".
# Nesse caso, a condição do IF a seguir será TRUE.
# Então o que está no corpo do IF será executado. No caso,
# é um chamado ao método main do script

if __name__ == "__main__": 
    main()
    
# 2
class A():
    def f(self):
        print("foo")


def main():
    obj_A = A() # Objeto sendo instanciado
    obj_A.f()

if __name__ == "__main__": 
    main()
    
# Métodos
def __depositar__(self,valor):
     self.saldo += valor
     
class Conta:
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo
        
    def depositar(self, valor):
        self.saldo += valor
        
    def sacar(self, valor):
        self.saldo -= valor
        
    def gerar_extrato(self):
        print(f"numero: {self.numero} \n cpf: {self.cpf}\nsaldo: {self.saldo}")     

def main():
    c1 = Conta(1,1,"Joao",0)
    c1.depositar(300)
    c1.sacar(100)
    c1.gerar_extrato()

if __name__ == "__main__": 
    main()
    
# Métodos com retorno
class Conta():
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo
        
    def depositar(self, valor):
        self.saldo += valor
        
    def sacar(self,valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            return True
            
    def gerar_extrato(self):
        print(f"numero: {self.numero}\n cpf: {self.cpf}\nsaldo: {self.saldo}")     
        
def main():
    c1 = Conta(1,1,"Joao",0)
    c1.depositar(300)
    saque = c1.sacar(400)
    c1.gerar_extrato()
    print(f"O saque foi realizado? {saque}")
    

if __name__ == "__main__": 
    main()

    