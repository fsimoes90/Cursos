from pathlib import Path

caminho = Path.home()

def encontra_arquivo(caminho, nome_do_arquivo):
    for arquivo in caminho.glob('**/*'):
        if arquivo.is_file():
            if arquivo.name == 'encontra_arquivo':
            #if arquivo.stem == 'encontra_arquivo':
                print(arquivo)
                
encontra_arquivo(Path.cwd(),"arquivo2")