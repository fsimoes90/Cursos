from pathlib import Path
import os

caminho_arquivo = Path(__file__)

print(caminho_arquivo)
print(caminho_arquivo.anchor)
print(caminho_arquivo.parent)
print(caminho_arquivo.parent.parent)
print(caminho_arquivo.stem)
print(caminho_arquivo.suffix)
print(caminho_arquivo.drive)
print(caminho_arquivo.parents[0]) #[0],[1],[2]...