from pathlib import Path
import os

# Retornando caminho do diretório de trabalho atual
print(Path.cwd())


# Esse caminho é absoluto
print(Path.cwd().is_absolute())


# Retornando caminho da primeira pasta
print(Path('primeira_pasta'))


# Esse caminho é absoluto
print(Path('primeira_pasta').is_absolute())


# Transformando o caminho em absoluto
print(Path.cwd() / 'primeira_pasta')
print((Path.cwd() / 'primeira_pasta').exists())

os.chdir(Path.home())
print(Path.cwd() / 'primeira_pasta')
print((Path.cwd() / 'primeira_pasta').exists())


# Garantindo que estamos retornando o caminho para a pasta do script
print(__file__)
print(Path(__file__).is_absolute())
print(Path(__file__).parent)

print(Path(__file__).parent / 'primeira_pasta')
print((Path(__file__).parent / 'primeira_pasta').exists())


# Trabalhando com partes de caminho
caminho_arquivo = Path(__file__)

print(caminho_arquivo)
print(caminho_arquivo.anchor)
print(caminho_arquivo.parent)
print(caminho_arquivo.name)
print(caminho_arquivo.stem)
print(caminho_arquivo.suffix)
print(caminho_arquivo.drive)

print(caminho_arquivo.parent)
print(caminho_arquivo.parents[3])
