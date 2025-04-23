# Módulo math
# Função	Retorno
# sqrt(x)	Raiz quadrada de x
# ceil(x)	Menor inteiro maior ou igual a x
# floor(x)	Maior inteiro menor ou igual a x
# cos(x)	Cosseno de x
# sin(x)	Seno de x
# log(x, b)	Logaritmo de x na base b
# pi	Valor de Pi (3.141592...)
# e	Valor de e (2.718281...)

# Módulo random

#Distribuições de valores reais
# Função	Retorno
# random()	Número de ponto flutuante no intervalo (00,0, 1,0)
# uniform(a, b)	Número de ponto flutuante N tal que a ≤ N ≤ b
# gauss(mu, sigma)	Distribuição gaussiana. mu é a média e sigma é o desvio padrão.
# normalvariate(mu, sigma)	Distribuição gaussiana. mu é a média e sigma é o desvio padrão.

#Funções para números inteiros
# Função	Retorno
# randrange(stop)	Um elemento selecionado aleatório de range(start, stop, step), mas sem construir um objeto range.
# randrange(start, stop, [step])	
# randint(a, b)	Número inteiro N tal que a ≤ N ≤ b

#Funções para sequências
# Função	Retorno
# choice(seq)	Elemento aleatório de uma sequência não vazia seq.
# shuffle(x[, random])	Embaralha a sequência x no lugar.
# sample(pop, k)	Uma sequência de tamanho k de elementos escolhidos da população pop, sem repetição. Usada para amostragem sem substituição.

# Módulo SMTPLIB
#import dos pacotes necessários
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

#criação de um objeto de mensagem
msg = MIMEMultipart()
texto = "Estou enviando um email com Python"

#parâmetros
senha = "SUA SENHA"
msg['From'] = "SEU E-MAIL"
msg['To'] = "E-MAIL DESTINO"
msg['Subject'] = "ASSUNTO"

#criação do corpo da mensagem
msg.attach(MIMEText(texto, 'plain'))

#criação do servidor
server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls()

#Login na conta para envio
server.login(msg['From'], senha)

#envio da mensagem
server.sendmail(msg['From'], msg['To'], msg.as_string())

#encerramento do servidor
server.quit()

print('Mensagem enviada com sucesso')

# Módulo time
# Função	Retorno
# time()	Número de segundos passados desde o início da contagem (epoch). Por padrão, o início é 00:00:00 do dia 1 de janeiro de 1970.
# ctime(segundos)	Uma string representando o horário local, calculado a partir do número de segundos passado como parâmetro.
# gmtime(segundos)	Converte o número de segundos em um objeto struct_time descrito a seguir.
# localtime(segundos)	Semelhante à gmtime(), mas converte para o horário local.
# sleep(segundos)	A função suspende a execução por determinado número de segundos.

import time

x = time.time()
print(f'Local time: {time.ctime(x)}')

# Índice	Atributo	Valores
# 0	tm_year	Por exemplo, 2020
# 1	tm_mon	range [1, 12]
# 2	tm_mday	range [1, 31]
# 3	tm_hour	range [0, 23]
# 4	tm_min	range [0, 59]
# 5	tm_sec	range [0, 61]
# 6	tm_wday	range [0, 6] Segunda-feira é 0
# 7	tm_yday	range [1, 366]
# 8	tm_isdst	0,1 ou -1
# N/A	tm_zone	Abreviação do nome da timezone

# Módulo tkinter
from tkinter import *

janelaPrincipal = Tk()
janelaPrincipal.mainloop()


janelaPrincipal = Tk()
texto = Label(master = janelaPrincipal, text = "Minha janela exibida")
janelaPrincipal.mainloop()


def funcClicar():
    print("Botão pressionado")

janelaPrincipal = Tk()
texto = Label(master = janelaPrincipal, text = "Minha janela exibida")
texto.pack()

pic = PhotoImage(file="logoEstacio.gif")
logo = Label(master = janelaPrincipal, image = pic)
logo.pack()

botao = Button(master = janelaPrincipal, text = 'Clique', command = funcClicar)
botao.pack()

janelaPrincipal.mainloop()

# Pacotes externos
# Nome do módulo	Pra que serve?
# numpy	Cálculos, operações matemáticas e simulações
# pandas	Manipulaçao de dados
# scikit-learn	Modelos de aprendizado de máquina
# matplotlib	Visualização de dados
# requests	Biblioteca de comandos de comunicação pelo protocolo HTTP
# flask	Construção de aplicações web