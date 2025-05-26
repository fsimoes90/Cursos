# pip install pandas
# pip install openpyxl
from pathlib import Path
import pandas as pd

pasta_atual = Path(__file__).parent

# Lendo tabelas com DataFrame
tabela_clientes = pd.read_excel(pasta_atual / 'planilhas' / 'clientes.xlsx')
print(tabela_clientes.head(10))


# Lendo aba específica
tabela_clientes = pd.read_excel(pasta_atual / 'planilhas' / 'clientes.xlsx', sheet_name='SC')
print(tabela_clientes.head(10))


# Modificando header
tabela_clientes = pd.read_excel(pasta_atual / 'planilhas' / 'clientes.xlsx', sheet_name='SC', header=0)
print(tabela_clientes.head(10))


# Adicionando coluna de index
tabela_clientes = pd.read_excel(pasta_atual / 'planilhas' / 'clientes.xlsx', sheet_name='SC', index_col=0)
print(tabela_clientes.head(10))


# Lendo colunas específicas
tabela_clientes = pd.read_excel(pasta_atual / 'planilhas' / 'clientes.xlsx', sheet_name='SC', usecols=[0, 1])
print(tabela_clientes.head(10))
tabela_clientes = pd.read_excel(pasta_atual / 'planilhas' / 'clientes.xlsx', sheet_name='SC', usecols="A:B")
print(tabela_clientes.head(10))


# Comentários sobre decimals e thousands
tabela_clientes = pd.read_excel(pasta_atual / 'planilhas' / 'clientes.xlsx', decimal='.')
print(tabela_clientes.head(10))

tabela_clientes = pd.read_excel(pasta_atual / 'planilhas' / 'clientes.xlsx', thousands='.')
print(tabela_clientes.head(10))


# Escrevendo planilha
tabela_clientes = pd.read_excel(pasta_atual / 'planilhas' / 'clientes.xlsx')
tabela_clientes.to_excel(pasta_atual / 'planilhas' / 'copia_clientes.xlsx')


# Escrevendo diversas abas
tabela_clientes_rs = pd.read_excel(pasta_atual / 'planilhas' / 'clientes.xlsx', sheet_name='RS')
tabela_clientes_sc = pd.read_excel(pasta_atual / 'planilhas' / 'clientes.xlsx', sheet_name='SC')

with pd.ExcelWriter(pasta_atual / 'planilhas' / 'copia_clientes.xlsx') as nova_planilha:
    tabela_clientes_rs.to_excel(nova_planilha, sheet_name='RS', index=False)
    tabela_clientes_sc.to_excel(nova_planilha, sheet_name='SC', index=False)
