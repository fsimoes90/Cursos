from pathlib import Path

# Construindo caminhos relativos
caminho = Path('primeira_pasta/segunda_pasta')

for nome in ['arquivo1.txt', 'arquivo2.txt', 'arquivo3.txt']:
    caminho_arquivo = caminho / nome
    print(caminho_arquivo)

# Construindo caminhos completos
caminho = Path('C:\\Users\\avsoares\\Documents\\courses-main\\courses-main\\Lendo e Escrevendo Arquivos\\scripts\\caminhos')

for nome in ['arquivo1.txt', 'arquivo2.txt', 'arquivo3.txt']:
    caminho_arquivo = caminho / nome
    print(caminho_arquivo)

# Construindo caminhos para home
print(Path.home())