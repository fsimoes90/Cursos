from pathlib import Path
caminho = Path('Lendo e escrevendo arquivos')
print (caminho)

for nome in ['arquivo1.txt', 'arquivo2.txt', 'arquivo3.txt']:
    caminho_arquivo = caminho / nome
    print(caminho_arquivo)
    
print(Path.home())
print(Path.home() / 'documents' / 'assim por diante')