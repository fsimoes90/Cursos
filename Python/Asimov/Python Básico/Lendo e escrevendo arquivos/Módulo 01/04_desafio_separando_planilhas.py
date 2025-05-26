from pathlib import Path
import pandas as pd

pasta_atual = Path(__file__).parent

tabela_clientes_dict = pd.read_excel(pasta_atual / 'planilhas' / 'clientes.xlsx', sheet_name=None)
for nome_aba, tabela in tabela_clientes_dict.items():
    tabela.to_excel(pasta_atual / 'planilhas' / 'planilhas_separadas' / f'{nome_aba}.xlsx', index=False)


with pd.ExcelWriter(pasta_atual / 'planilhas' / 'planilha_consolidada' / 'clientes.xlsx') as consolidada:
    for arquivo in Path(pasta_atual / 'planilhas' / 'planilhas_separadas').glob('*.xlsx'):
        tabela = pd.read_excel(arquivo)
        tabela.to_excel(consolidada, sheet_name=arquivo.stem, index=False)

