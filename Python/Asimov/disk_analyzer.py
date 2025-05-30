import os
import hashlib
import winreg
from pathlib import Path
from collections import defaultdict
import datetime

# Função para calcular o hash de um arquivo
def calculate_file_hash(filepath, block_size=65536):
    try:
        hasher = hashlib.md5()
        with open(filepath, 'rb') as f:
            for block in iter(lambda: f.read(block_size), b''):
                hasher.update(block)
        return hasher.hexdigest()
    except (PermissionError, FileNotFoundError, IOError):
        return None

# Função para formatar tamanho de arquivo em MB
def format_size(size_bytes):
    return f"{size_bytes / (1024 * 1024):.2f} MB"

# Função para obter programas instalados do Registro do Windows
def get_installed_programs():
    installed = set()
    try:
        reg_path pastries r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path) as key:
            for i in range(winreg.QueryInfoKey(key)[0]):
                try:
                    subkey_name = winreg.EnumKey(key, i)
                    with winreg.OpenKey(key, subkey_name) as subkey:
                        try:
                            display_name, _ = winreg.QueryValueEx(subkey, "DisplayName")
                            installed.add(display_name.lower())
                        except FileNotFoundError:
                            pass
                except (PermissionError, FileNotFoundError):
                    continue
    except Exception:
        pass
    return installed

# Função principal para varrer o disco
def scan_disk(root_dir="C:\\", min_size_mb=100, top_folders=50):
    # Estruturas para armazenar dados
    folder_sizes = defaultdict(int)  # Tamanho total por pasta
    file_hashes = defaultdict(list)  # Hash -> Lista de arquivos
    all_files = []  # Lista de todos os arquivos com detalhes
    suspicious_folders = []  # Pastas potencialmente residuais

    # Locais comuns para verificar resíduos
    program_folders = [
        Path("C:\\Program Files"),
        Path("C:\\Program Files (x86)"),
        Path("C:\\Users\\All Users"),
        Path(os.path.expanduser("~\\AppData\\Local")),
        Path(os.path.expanduser("~\\AppData\\Roaming"))
    ]

    # Obter programas instalados
    installed_programs = get_installed_programs()

    # Varredura recursiva
    for root, dirs, files in os.walk(root_dir, topdown=True):
        try:
            folder_size = 0
            for file in files:
                filepath = Path(root) / file
                try:
                    file_size = filepath.stat().st_size
                    folder_size += file_size
                    file_hash = calculate_file_hash(filepath)
                    if file_hash:
                        file_hashes[file_hash].append(str(filepath))
                    all_files.append({
                        'path': str(filepath),
                        'size': file_size,
                        'hash': file_hash
                    })
                except (PermissionError, FileNotFoundError):
                    continue
            folder_sizes[root] = folder_size
        except (PermissionError, FileNotFoundError):
            continue

        # Verificar pastas suspeitas
        folder_path = Path(root)
        if any(folder_path.is_relative_to(p) for p in program_folders):
            folder_name = folder_path.name.lower()
            if folder_name not in installed_programs and folder_name not in ('', 'windows', 'microsoft', 'common files'):
                suspicious_folders.append((str(folder_path), format_size(folder_sizes[root])))

    # Filtrar pastas por tamanho mínimo (em bytes)
    min_size_bytes = min_size_mb * 1024 * 1024
    filtered_folders = [(folder, size) for folder, size in folder_sizes.items() if size >= min_size_bytes]
    sorted_folders = sorted(filtered_folders, key=lambda x: x[1], reverse=True)[:top_folders]

    # Identificar duplicatas
    duplicates = {hash_val: paths for hash_val, paths in file_hashes.items() if len(paths) > 1}

    # Gerar relatório em Markdown
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report = f"# Relatório de Análise do Disco C: ({current_time})\n\n"
    
    # Seção: Estrutura de Diretórios
    report += f"## Estrutura de Diretórios (Top {top_folders} pastas com tamanho >= {min_size_mb} MB)\n"
    if sorted_folders:
        for folder, size in sorted_folders:
            report += f"- **{folder}**: {format_size(size)}\n"
    else:
        report += f"Nenhuma pasta encontrada com tamanho >= {min_size_mb} MB.\n"
    
    # Seção: Arquivos Duplicados
    report += "\n## Arquivos Duplicados\n"
    if duplicates:
        for hash_val, paths in duplicates.items():
            total_size = sum(Path(p).stat().st_size for p in paths if Path(p).exists())
            report += f"### Hash: {hash_val}\n"
            report += f"Tamanho total: {format_size(total_size)}\n"
            for path in paths:
                report += f"- {path}\n"
    else:
        report += "Nenhum arquivo duplicado encontrado.\n"

    # Seção: Possíveis Resíduos de Programas
    report += "\n## Possíveis Resíduos de Programas Desinstalados\n"
    if suspicious_folders:
        for folder, size in suspicious_folders[:top_folders]:
            report += f"- **{folder}**: {size}\n"
    else:
        report += "Nenhum resíduo identificado.\n"

    # Seção: Recomendações
    report += "\n## Recomendações de Limpeza\n"
    report += "- **Arquivos Duplicados**: Revise os arquivos listados e mantenha apenas uma cópia, preferencialmente na pasta mais relevante.\n"
    report += "- **Resíduos de Programas**: Pesquise as pastas listadas para confirmar se pertencem a programas desinstalados antes de excluir.\n"
    report += f"- **Pastas Grandes**: Analise as {top_folders} pastas listadas para identificar arquivos desnecessários, como downloads, backups ou instaladores antigos.\n"
    report += "- **Cuidados**: Mova arquivos para a Lixeira e teste o sistema antes de excluir permanentemente. Evite apagar pastas do sistema como `C:\\Windows`.\n"
    report += "- **Ferramentas Adicionais**: Considere usar o Liberador de Espaço em Disco do Windows ou CCleaner para arquivos temporários.\n"

    # Salvar relatório
    with open("estrutura.md", "w", encoding="utf-8") as f:
        f.write(report)

    return report

# Executar a varredura
if __name__ == "__main__":
    try:
        print("Iniciando varredura do disco C:...")
        report = scan_disk(min_size_mb=100, top_folders=50)
        print("Relatório gerado com sucesso em 'estrutura.md'.")
    except Exception as e:
        print(f"Erro durante a varredura: {e}")