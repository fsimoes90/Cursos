import os

os.getcwd()

# Agrega uma pasta a um caminho. Retorna uma string
os.path.join('\\fernando.simoes\\Documents\\Python Scripts\\Estudo\\Asimov\\PythomStarter\\5. Modulo OS\\Pasta', 'pasta')


# Retorna o nome da pasta final de um caminho completo.
os.path.basename('\\fernando.simoes\\Documents\\Python Scripts\\Estudo\\Asimov\\PythomStarter\\5. Modulo OS\\Pasta')


# Separa caminho da pasta. Retorna ambos segregados.
os.path.split()


# Retorna a raiz do diretório especificado.
os.path.dirname('\\fernando.simoes\\Documents\\Python Scripts\\Estudo\\Asimov\\PythomStarter\\5. Modulo OS\\Pasta')


# Retorna o tempo da última atualização do diretório
curr_dir = os.getcwd()
lt = os.path.getmtime(curr_dir)
# getatime retorna o tempo do último acesso.
from datetime import datetime
datetime.utcfromtimestamp(lt)


# Pergunta se determinado caminho é um arquivo
os.path.isfile(curr_dir) 
# Pergunta se determinado caminho é uma pasta
os.path.isdir(curr_dir) 

