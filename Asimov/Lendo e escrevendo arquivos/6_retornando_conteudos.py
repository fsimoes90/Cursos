from pathlib import Path
import os

# listando arquivos de uma pasta
print(os.listdir(Path.cwd()))
# print(Path.cwd().glob('*'))
# print(Path.cwd().glob('**/*'))
# print(Path.cwd().glob('**/*.txt'))
# print(Path.cwd().glob('*.py'))

print(Path.home().exists())

print(Path(__file__).is_file())
print(Path(__file__).parent.is_file())
print(Path(__file__).parent.is_dir())
