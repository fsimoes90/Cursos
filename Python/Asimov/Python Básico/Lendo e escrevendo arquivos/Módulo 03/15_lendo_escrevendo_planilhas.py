# pip install pandas
# pip install openpyxl
import pandas as pd
from pathlib import Path

pasta_aula = Path(__file__).parent

# ##### Lendo tabelas com DataFrame #####
# tabela_clientes = pd.read_excel(pasta_aula / "planilhas" / "clientes.xlsx")
# print(tabela_clientes.head(10))

# Lendo aba específica
# tabela_clientes = pd.read_excel(pasta_aula / "planilhas" / "clientes.xlsx", sheet_name="SC")
# print(tabela_clientes.head(10))

# ##### Modificando headers #####
# tabela_clientes = pd.read_excel(pasta_aula / "planilhas" / "clientes.xlsx", sheet_name="SC", header=0)
# print(tabela_clientes.head(10))

# ##### Adicionando coluna de index #####
# tabela_clientes = pd.read_excel(pasta_aula / "planilhas" / "clientes.xlsx", sheet_name="SC", header=0, index_col=0)
# print(tabela_clientes.head(10))

# ##### Lendo colunas específicas #####
# tabela_clientes = pd.read_excel(pasta_aula / "planilhas" / "clientes.xlsx", sheet_name="SC", usecols="A:B") # podemos usar [0,1]
# print(tabela_clientes.head(10))

# ##### Comentários sobre decimals e thousands #####
# tabela_clientes = pd.read_excel(pasta_aula / "planilhas" / "clientes.xlsx", thousands=".")
# print(tabela_clientes.head(10))

# tabela_clientes = pd.read_excel(pasta_aula / "planilhas" / "clientes.xlsx", decimal=".", thousands=".")
# print(tabela_clientes.head(10))

# ##### Escrevendo planilha #####
tabela_clientes = pd.read_excel(pasta_aula / "planilhas" / "clientes.xlsx")
tabela_clientes.to_excel(pasta_aula / "planilhas" / "clientes_copia.xlsx", index=False)
print(tabela_clientes.head(10))

# ##### Escrevendo planilha com multiplas abas #####
with pd.ExcelWriter(pasta_aula / "planilhas" / "clientes_copia.xlsx") as writer:
    tabela_clientes.to_excel(writer, sheet_name="SC")
    tabela_clientes.to_excel(writer, sheet_name="RS")





    












