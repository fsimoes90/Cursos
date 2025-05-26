from pathlib import Path
import os

print((Path.cwd()/ 'Lendo e escrevendo arquivos').exists())
print(Path.cwd())

os.chdir(Path.home())

print(__file__)
print(Path(__file__))
print(Path(__file__).parent)
print(Path(__file__).parent / 'Lendo e escrevendo arquivos')
