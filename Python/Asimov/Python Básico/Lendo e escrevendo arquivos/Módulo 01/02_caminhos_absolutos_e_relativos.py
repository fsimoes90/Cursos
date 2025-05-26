from pathlib import Path
import os

# O local onde Python está sendo rodado
print(Path.cwd())

# Conseguimos encontrar a pasta 'primeira_pasta'?
print(Path('primeira_pasta').exists())

# É a forma de mudar de local pelo Python
# Com isto vamos lá para nossa pasta home e nosso cwd muda
os.chdir(Path.home())

# Novo local onde Python está sendo rodado
print(Path.cwd())

# E agora, conseguimos encontrar a 'primeira_pasta'?
print(Path('primeira_pasta').exists())