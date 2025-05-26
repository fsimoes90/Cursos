from pathlib import Path
import shutil
import os

'''
# copiando arquico com copyfile
pasta_atual = Path(__file__).parent
caminho_arquivo = pasta_atual / 'texto.txt'
caminho_arquivo_destino = pasta_atual / 'destino1' / 'texto.txt'

shutil.copyfile(caminho_arquivo, caminho_arquivo_destino)
'''
'''
# copiando arquivo com copy
pasta_atual = Path(__file__).parent
caminho_arquivo = pasta_atual / 'texto.txt'
caminho_pasta_destino = pasta_atual / 'destino2'

shutil.copy(caminho_arquivo, caminho_pasta_destino)
'''
'''
# copiando arquivo com copy2
pasta_atual = Path(__file__).parent
caminho_arquivo = pasta_atual / 'texto.txt'
caminho_pasta_destino = pasta_atual / 'destino3'

shutil.copy2(caminho_arquivo, caminho_pasta_destino)
'''
'''
# movendo arquivos
pasta_atual = Path(__file__).parent
caminho_arquivo = pasta_atual / 'texto.txt'
caminho_pasta_destino = pasta_atual / 'destino1'

shutil.move(caminho_arquivo, caminho_pasta_destino)
'''

# deletando arquivos
pasta_atual = Path(__file__).parent
caminho_arquivo = pasta_atual / 'texto.txt'
caminho_arquivo_destino = pasta_atual / 'destino3' / 'texto.txt'

if caminho_arquivo_destino.exists():
    os.remove(caminho_arquivo_destino)
else:
    print('Arquivo não existe')