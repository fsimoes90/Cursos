# script threads_var.py
from threading import Thread, Lock
from multiprocessing import Process
import time

minha_lista = []
 
def funcao_a(indice):
    for i in range(100000):
        minha_lista.append(1)
        print("Termino thread ", indice)

def main():
    tarefas = []
    for indice in range(10):
        tarefa = Thread(target=funcao_a, args=(indice,))
        tarefas.append(tarefa)
        tarefa.start()

    print("Antes de aguardar o termino!", len(minha_lista))

    for tarefa in tarefas:
        tarefa.join()

    print("Após aguardar o termino!", len(minha_lista))

if __name__ == "__main__":
        main()


# script processos_var.py
from threading import Thread, Lock
from multiprocessing import Process
import time

minha_lista = []
 
def funcao_a(indice):
    for i in range(100000):
        minha_lista.append(1)
        print("Termino thread ", indice)

def main():
    tarefas = []
for indice in range(10):
        tarefa = Process(target=funcao_a, args=(indice,))
        tarefas.append(tarefa)
        tarefa.start()
print("Antes de aguardar o termino!", len(minha_lista))

for tarefa in tarefas:
    tarefa.join()

print("Após aguardar o termino!", len(minha_lista))

if __name__ == "__main__":
    main()
    
# Travas (Lock)

# script threads_inc.py
from threading import Thread, Lock
from multiprocessing import Process
import time

contador = 0
 
def funcao_a(indice):
    global contador
    for i in range(1000000):
        contador += 1
    print("Termino thread ", indice)

def main():
    tarefas = []
    for indice in range(10):
        tarefa = Thread(target=funcao_a, args=(indice,))
        tarefas.append(tarefa)
        tarefa.start()
 
    print("Antes de aguardar o termino!", contador)

    for tarefa in tarefas:
        tarefa.join()

    print("Após aguardar o termino!", contador)

if __name__ == "__main__":
    main()



# Compartilhando variáveis entre processos
# script processos.py
from threading import Thread
from multiprocessing import Process, Value

def funcao_a(indice, cont):
    for i in range(100000):
        with cont.get_lock():
            cont.value += 1
    print("Termino processo ", indice)

def main():
    contador = Value('i', 0)
    tarefas = []
    for indice in range(10):
        tarefa = Process(target=funcao_a, args=(indice, contador))
        tarefas.append(tarefa)
        tarefa.start()

    print("Antes de aguardar o termino!", contador.value)

    for tarefa in tarefas:
        tarefa.join()

    print("Após aguardar o termino!", contador.value)

if __name__ == "__main__":
    main()

